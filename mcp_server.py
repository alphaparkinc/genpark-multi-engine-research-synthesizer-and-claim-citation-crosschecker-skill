"""MCP server for Multi-Engine Research Synthesizer."""
import sys
import json
from client import ResearchSynthesizer


def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [
                {
                    "name": "decompose_research_query",
                    "description": "Decomposes complex questions into multi-perspective atomic search sub-queries",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "query": {"type": "string"},
                        },
                        "required": ["query"],
                    },
                },
                {
                    "name": "crosscheck_claim_citations",
                    "description": "Cross-checks factual claims against multiple search snippets and computes consensus score",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "claims": {"type": "array"},
                            "sources": {"type": "array"},
                        },
                        "required": ["claims", "sources"],
                    },
                },
            ]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "decompose_research_query":
            res = ResearchSynthesizer.decompose_query(args.get("query", ""))
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
        elif tool_name == "crosscheck_claim_citations":
            res = ResearchSynthesizer.synthesize_consensus(
                args.get("claims", []),
                args.get("sources", []),
            )
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}


if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
