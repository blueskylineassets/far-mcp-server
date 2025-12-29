"""
FAR MCP Server - Model Context Protocol server for Federal Acquisition Regulations

Bot-First monetization strategy: Exposes the FAR RAG API as an MCP tool,
allowing AI agents like Claude Desktop to query federal acquisition regulations.
Returns raw JSON for maximum agent flexibility.
"""

import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

from client import query_far_backend

# Load environment variables from .env file (if present)
load_dotenv()

# Initialize the MCP server
mcp = FastMCP("far-oracle")


@mcp.tool()
async def consult_federal_regulations(query: str, top_k: int = 5) -> str:
    """
    Search Federal Acquisition Regulations (FAR) for compliance rules, 
    contract clauses, and procurement requirements.
    
    Use this tool when you need to:
    - Verify government contracting compliance requirements
    - Find specific FAR clauses for contract proposals
    - Understand invoicing rules for federal contracts
    - Research procurement regulations and procedures
    - Check small business set-aside requirements
    
    Args:
        query: Natural language question about federal acquisition regulations.
               Examples: "cybersecurity requirements", "small business set aside",
               "payment terms for government contracts"
        top_k: Number of relevant clauses to return (1-20, default 5)
        
    Returns:
        JSON string with relevant FAR clauses, or error message if quota exceeded
    """
    # Check for direct A2A API key first (preferred)
    far_api_key = os.getenv("FAR_API_KEY")
    if far_api_key:
        return await query_far_backend(
            query=query,
            api_key=far_api_key,
            top_k=top_k,
            use_rapidapi=False
        )
    
    # Fall back to RapidAPI key
    rapidapi_key = os.getenv("RAPIDAPI_KEY")
    if rapidapi_key:
        return await query_far_backend(
            query=query,
            api_key=rapidapi_key,
            top_k=top_k,
            use_rapidapi=True
        )
    
    return (
        "Error: No API key configured. Set either:\n"
        "- FAR_API_KEY: Register at https://far-rag-api-production.up.railway.app/v1/register\n"
        "- RAPIDAPI_KEY: Get key at https://rapidapi.com/yschang/api/far-rag"
    )


if __name__ == "__main__":
    # Run the MCP server in stdio mode (for Claude Desktop integration)
    mcp.run()
