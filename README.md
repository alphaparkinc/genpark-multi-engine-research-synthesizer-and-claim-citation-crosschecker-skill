# genpark-multi-engine-research-synthesizer-and-claim-citation-crosschecker-skill

Multi-source search query decomposer, consensus synthesis engine, and claim-level citation cross-checker.

100% Python Standard Library implementation with zero external dependencies.

## Key Capabilities

- **Query Decomposition**: Deconstructs complex analytical research questions into focused perspective sub-queries.
- **Cross-Source Consensus Scoring**: Evaluates claims against multiple independent search snippets, flagging single-source vs. multi-source consensus.
- **Zero Hallucination Grounding**: Verifies token overlap between assertions and retrieved evidence.

## Architecture

```
[Complex Research Question]
            │
            ▼
┌──────────────────────────────────────────────┐
│           ResearchSynthesizer                │
│  - Query Decomposition & Angle Generator     │
│  - Multi-Snippet Token Overlap Comparator    │
│  - Consensus & Support Density Scorer        │
└──────────────────────────────────────────────┘
            │
            ▼
[Grounded Claim Consensus Report & Citations]
```

## MCP Server Integration

Run standard MCP stdio server:
```bash
python mcp_server.py
```

Exposed Tools:
- `decompose_research_query`: Decomposes complex questions into multi-perspective atomic search sub-queries.
- `crosscheck_claim_citations`: Cross-checks factual claims against multiple search snippets and computes consensus score.

## Quickstart (Python API)

```python
from client import ResearchSynthesizer

sub_queries = ResearchSynthesizer.decompose_query("compare Redis vs Memcached")
print(sub_queries)
```

---

## GenPark Ecosystem

- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)
