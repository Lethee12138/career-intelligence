import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'tests/fixtures/real-source-connector-synthetic.json').read_text())


def test_official_source_can_be_verified():
    source = DATA['source']
    assert source['type'] == 'official'
    assert source['authority'] == 'HIGH'
    assert source['status'] == 'OPEN_VERIFIED'


def test_third_party_source_requires_verification():
    source = DATA['invalid_source']
    assert source['type'] == 'third_party'
    assert source['status'] == 'NEEDS_VERIFY'
