"""Example usage for Multi-Engine Research Synthesizer."""
from client import ResearchSynthesizer

if __name__ == "__main__":
    sub_queries = ResearchSynthesizer.decompose_query("compare LangChain vs LlamaIndex")
    print("Decomposed Queries:", sub_queries)

    claims = [
        {"claim": "LlamaIndex specializes in data indexing and retrieval augmentation"},
        {"claim": "LangChain provides flexible agentic chaining abstractions"},
    ]
    sources = [
        {"id": "s1", "title": "LlamaIndex Docs", "snippet": "LlamaIndex is a data framework for LLM-based applications focusing on data indexing and retrieval."},
        {"id": "s2", "title": "AI Comparison", "snippet": "LlamaIndex excels at retrieval augmentation and structured document indexing."},
        {"id": "s3", "title": "LangChain Overview", "snippet": "LangChain provides powerful composable agentic chaining abstractions."},
    ]

    consensus = ResearchSynthesizer.synthesize_consensus(claims, sources)
    print("\nReliable Ratio:", consensus["reliable_ratio"])
    for c in consensus["verified_claims"]:
        print(f"  [{c['status']}] {c['claim']} (Sources: {c['support_count']})")
