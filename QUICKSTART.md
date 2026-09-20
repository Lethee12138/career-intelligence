# Career Intelligence Quick Start

## What this is

Career Intelligence is an MCP + Skill project for career research, job discovery, role analysis and application preparation.

This repository contains the capability layer only. It does not include personal career records or private user data.

## What you need

- A compatible MCP client (for example, a client that supports local MCP servers)
- Node.js environment for running the local service
- Your own career context or test data

## Basic flow

1. Install the Skill.
2. Start the local MCP service.
3. Connect the service to your MCP client.
4. Provide your own career background, preferences, or job requirements.
5. Use the career tools for analysis and preparation.

## Start the local service

Use the provided service scripts:

```bash
./scripts/career-mcp-service.sh start
./scripts/career-mcp-service.sh status
```

The service runs locally and does not require sharing personal data with this repository.

## Connect and try

After connecting the MCP client, examples include:

- Analyse a job description.
- Explore possible role matches.
- Review evidence fit.
- Prepare application materials.

## Privacy boundary

Do not commit:

- personal CV files
- private career records
- personal evidence databases
- API keys or tokens

Use synthetic examples for testing and demonstrations.

## Boundaries

This project provides analysis capability. It does not submit applications, contact employers, or make decisions on behalf of users.

For personal use, keep private career information outside the public repository.
