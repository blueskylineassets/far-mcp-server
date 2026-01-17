# FAR Oracle - MCP Server for AI Agents

**FAR Oracle** is a Model Context Protocol (MCP) server that provides AI agents with instant, programmatic access to the U.S. Federal Acquisition Regulation (FAR).

This server allows agents like Claude Desktop, AutoGPT, and CrewAI to perform semantic searches on the entire FAR database, enabling them to assist with compliance, research, and proposal writing for government contracts.

<!-- mcp-name: io.github.blueskylineassets/far-mcp-server -->

<!-- Demo GIF coming soon -->

## Key Features

- **Semantic Search**: Understands the *intent* behind queries, not just keywords.
- **A2A Commerce**: Zero-friction, automatic API key registration on first use.
- **Always Up-to-Date**: Continuously updated with the latest FAR clauses.
- **Simple Integration**: Works seamlessly with any MCP-compatible agent.

---

## Quick Start (30 Seconds)

Get your agent connected to FAR Oracle in two simple steps.

### Step 1: Install from PyPI

```bash
pip install far-oracle
```

### Step 2: Configure Your Agent (e.g., Claude Desktop)

Add the following to your agent's MCP configuration file (e.g., `claude_desktop_config.json`).

**The API key is handled automatically via A2A commerce. You do not need to provide one.**

```json
{
  "mcpServers": {
    "far-oracle": {
      "command": "far-oracle",
      "args": []
    }
  }
}
```

That's it! Your agent can now access the FAR.

---

## How It Works: A2A Commerce

This MCP server uses **Agent-to-Agent (A2A) Commerce** for authentication. The first time your agent connects, it automatically:

1.  Registers for a free API key.
2.  Stores the key locally in `~/.far-oracle/credentials`.
3.  Uses the key for all subsequent requests.

This provides a completely seamless, zero-friction onboarding experience for agents.

## Usage Examples

Once configured, you can ask your agent questions like:

> "Using the far-oracle tool, what are the FAR requirements for cybersecurity?"

> "With far-oracle, explain the small business set-aside rules found in FAR Part 19."

> "Use far-oracle to find contract clauses related to intellectual property and data rights."

## Pricing & Tiers

FAR Oracle uses a simple, agent-friendly pricing model. All usage is managed through the A2A Commerce API.

| Plan  | Queries/Month | Price     | Upgrade                                       |
|-------|---------------|-----------|-----------------------------------------------|
| Free  | 500           | **$0**    | Automatic on first use                        |
| Pro   | 5,000         | **$29**   | Via `/v1/billing/upgrade` endpoint            |
| Ultra | 150,000       | **$199**  | Via `/v1/billing/upgrade` endpoint            |

Your agent can programmatically upgrade its plan by calling the billing endpoint.

## Troubleshooting

**Problem: `command not found: far-oracle`**

- **Cause:** The package's scripts directory is not in your system's `PATH`.
- **Solution:** Ensure that the output of `python3 -m site --user-base`/bin is in your `PATH`. Alternatively, you can use the full path to the executable.

**Problem: Connection errors or timeouts**

- **Cause:** A firewall may be blocking the connection to the FAR RAG API.
- **Solution:** Ensure your system can make outbound requests to `https://far-rag-api-production.up.railway.app`.

## Full API Documentation

For more details on the underlying REST API, including all available endpoints and parameters, please see the full API documentation:

[**FAR RAG API Documentation**](https://far-rag-api-production.up.railway.app/docs)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
