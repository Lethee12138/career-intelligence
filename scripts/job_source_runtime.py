"""Read-only public job source runtime for Career Intelligence.

Standard-library only. This module fetches public job pages and normalizes source
facts. It never logs in, submits applications, uploads files, or decides fit.
"""
from __future__ import annotations

import argparse
import html
import ipaddress
import json
import re
import socket
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen


MAX_BYTES = 5_000_000
USER_AGENT = "CareerIntelligence-JobScanner/0.3 (+public-read-only)"


@dataclass(frozen=True)
class AdapterSpec:
    name: str
    company: str
    verified_hosts: tuple[str, ...]
    runtime_status: str = "ACTIVE"


ADAPTERS = {
    "sap": AdapterSpec("sap", "SAP", ("jobs.sap.com", "careers.sap.com")),
    "tencent": AdapterSpec("tencent", "Tencent", ("join.qq.com",), "MAPPED"),
    # Kuaishou's official recruitment host is verified; a site-specific parser
    # remains disabled until its public page structure is mapped.
    "kuaishou": AdapterSpec("kuaishou", "Kuaishou", ("zhaopin.kuaishou.cn",), "MAPPED"),
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _normalize_space(value: str | None) -> str | None:
    if value is None:
        return None
    value = html.unescape(re.sub(r"<[^>]+>", " ", value))
    value = re.sub(r"\s+", " ", value).strip()
    return value or None


def _host_allowed(host: str, spec: AdapterSpec) -> bool:
    host = host.lower().rstrip(".")
    return any(host == allowed or host.endswith("." + allowed)
               for allowed in spec.verified_hosts)


def _validate_public_url(url: str, spec: AdapterSpec) -> None:
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.hostname:
        raise ValueError("Only public HTTPS URLs are supported")
    if not spec.verified_hosts:
        raise ValueError(f"{spec.name} live host is not verified yet")
    if not _host_allowed(parsed.hostname, spec):
        raise ValueError(f"Host is outside verified {spec.name} official hosts")
    try:
        ip = ipaddress.ip_address(parsed.hostname)
    except ValueError:
        ip = None
    if ip and (ip.is_private or ip.is_loopback or ip.is_link_local or
               ip.is_reserved or ip.is_multicast):
        raise ValueError("Private or reserved network targets are not allowed")


def fetch_public(url: str, spec: AdapterSpec, timeout: int = 20) -> tuple[str, str]:
    _validate_public_url(url, spec)
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html"})
    with urlopen(req, timeout=timeout) as response:
        final_url = response.geturl()
        _validate_public_url(final_url, spec)
        raw = response.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES:
            raise ValueError("Page exceeds read-only fetch size limit")
        charset = response.headers.get_content_charset() or "utf-8"
    return raw.decode(charset, "replace"), final_url


def _attr(tag: str, name: str) -> str | None:
    m = re.search(rf'\b{name}=["\']([^"\']+)["\']', tag, re.I)
    return html.unescape(m.group(1)) if m else None


def extract_sap_search(page: str, base_url: str, limit: int = 25) -> list[dict[str, Any]]:
    found: list[dict[str, Any]] = []
    seen: set[str] = set()
    for match in re.finditer(r"(<a\b[^>]*>)(.*?)</a>", page, re.I | re.S):
        tag, body = match.groups()
        classes = (_attr(tag, "class") or "").split()
        if not any("jobTitle-link" in c for c in classes):
            continue
        href = _attr(tag, "href")
        role = _normalize_space(body)
        if not href or not role:
            continue
        source_url = urljoin(base_url, href)
        source_url = html.unescape(source_url)
        if source_url in seen:
            continue
        seen.add(source_url)
        page_id = None
        m = re.search(r"/(\d+)/?$", urlparse(source_url).path)
        if m:
            page_id = m.group(1)
        found.append({
            "company": "SAP",
            "role": role,
            "source_url": source_url,
            "source_type": "official",
            "authority_level": "HIGH",
            "adapter_name": "sap",
            "source_page_id": page_id,
            "verification_status": "NEEDS_VERIFY",
        })
        if len(found) >= limit:
            break
    return found


def _sap_property(page: str, property_id: str) -> str | None:
    pattern = (
        rf'<span\b[^>]*data-careersite-propertyid=["\']'
        rf'{re.escape(property_id)}["\'][^>]*>(.*?)</span>'
    )
    m = re.search(pattern, page, re.I | re.S)
    return _normalize_space(m.group(1)) if m else None


def extract_sap_detail(page: str, source_url: str, captured_at: str | None = None) -> dict[str, Any]:
    title_match = re.search(r"<h1\b[^>]*>(.*?)</h1>", page, re.I | re.S)
    role = _normalize_space(title_match.group(1)) if title_match else None
    requisition_id = _sap_property(page, "facility")
    location = _sap_property(page, "location")
    department = _sap_property(page, "department")
    posted_date = _sap_property(page, "date")
    career_status = _sap_property(page, "customfield3")
    employment_type = _sap_property(page, "shifttype")
    lowered = _normalize_space(page) or ""
    lowered = lowered.lower()
    closed_markers = (
        "job is no longer available",
        "position is no longer available",
        "this job has expired",
    )
    closed = any(marker in lowered for marker in closed_markers)
    apply_cta = bool(re.search(r'id=["\']apply-CTA-container["\']', page, re.I))
    if not apply_cta:
        apply_cta = bool(re.search(r">\s*apply(?: now)?\s*<", page, re.I))

    if closed:
        status = "CLOSED"
    elif role and requisition_id and location and apply_cta:
        status = "OPEN_VERIFIED"
    else:
        status = "NEEDS_VERIFY"

    return {
        "source_identity": f"career-url:{source_url}",
        "company": "SAP",
        "url": source_url,
        "source_url": source_url,
        "source_type": "official",
        "authority_level": "HIGH",
        "captured_at": captured_at or utc_now(),
        "adapter_name": "sap",
        "extraction_method": "official-html",
        "external_job_id": requisition_id,
        "role": role,
        "location": location,
        "department": department,
        "posted_date": posted_date,
        "career_status": career_status,
        "employment_type": employment_type,
        "verification_status": status,
        "verification_evidence": {
            "detail_page_accessible": bool(role),
            "apply_cta_present": apply_cta,
            "closed_marker_present": closed,
        },
    }


def discover(adapter: str, url: str, limit: int = 25) -> dict[str, Any]:
    spec = ADAPTERS[adapter]
    page, final_url = fetch_public(url, spec)
    if adapter != "sap":
        raise NotImplementedError(f"{adapter} discovery parser is not live yet")
    items = extract_sap_search(page, final_url, limit=limit)
    return {
        "adapter": adapter,
        "source_url": final_url,
        "captured_at": utc_now(),
        "count": len(items),
        "candidates": items,
    }


def extract(adapter: str, url: str, captured_at: str | None = None) -> dict[str, Any]:
    spec = ADAPTERS[adapter]
    page, final_url = fetch_public(url, spec)
    if adapter != "sap":
        raise NotImplementedError(f"{adapter} detail parser is not live yet")
    return extract_sap_detail(page, final_url, captured_at=captured_at)


def adapter_map(adapter: str) -> dict[str, Any]:
    spec = ADAPTERS[adapter]
    return {
        "adapter": spec.name,
        "company": spec.company,
        "verified_hosts": list(spec.verified_hosts),
        "runtime_status": spec.runtime_status,
        "boundary": "SOURCE_FACTS_ONLY",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("discover", "extract", "map"))
    parser.add_argument("--adapter", required=True, choices=sorted(ADAPTERS))
    parser.add_argument("--url")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--captured-at")
    args = parser.parse_args()

    if args.action == "map":
        result = adapter_map(args.adapter)
    else:
        if not args.url:
            parser.error("--url is required for discover/extract")
        result = (discover(args.adapter, args.url, args.limit)
                  if args.action == "discover"
                  else extract(args.adapter, args.url, args.captured_at))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
