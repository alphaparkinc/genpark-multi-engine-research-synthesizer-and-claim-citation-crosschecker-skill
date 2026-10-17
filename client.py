"""Multi-Engine Research Synthesizer and Claim Citation Crosschecker.
100% Python Standard Library.
"""

from typing import List, Dict, Any, Optional
import re


class ResearchSynthesizer:
    """Decomposes research topics into targeted sub-queries, cross-references claims across
    multiple search snippet results, and verifies citation consistency and source agreement."""

    @classmethod
    def decompose_query(cls, query: str) -> List[str]:
        """Decomposes complex research questions into atomic sub-queries."""
        sub_queries = [query.strip()]
        words = re.findall(r'\w+', query.lower())

        if "how does" in query.lower() or "what is" in query.lower():
            sub_queries.append(f"{query} architecture and benchmarks")
            sub_queries.append(f"{query} limitations and trade-offs")
        elif "compare" in query.lower() or " vs " in query.lower():
            parts = re.split(r'\bvs\b|\band\b', query, flags=re.IGNORECASE)
            if len(parts) >= 2:
                sub_queries.append(f"{parts[0].strip()} core features")
                sub_queries.append(f"{parts[1].strip()} core features")

        return list(dict.fromkeys(sub_queries))[:3]

    @classmethod
    def synthesize_consensus(
        cls,
        claims: List[Dict[str, Any]],
        sources: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """Validates factual claims against provided source snippets, calculating consensus support."""
        verified_claims = []
        source_map = {str(s.get("id")): s for s in sources}

        for claim_obj in claims:
            claim_text = str(claim_obj.get("claim", ""))
            claim_tokens = [t.lower() for t in re.findall(r'\w+', claim_text) if len(t) > 3]

            supporting_sources = []
            for s in sources:
                s_text = (str(s.get("title", "")) + " " + str(s.get("snippet", ""))).lower()
                matched = [t for t in claim_tokens if t in s_text]
                if len(matched) >= max(1, int(len(claim_tokens) * 0.4)):
                    supporting_sources.append({
                        "source_id": s.get("id"),
                        "title": s.get("title"),
                        "url": s.get("url"),
                        "matched_overlap": len(matched),
                    })

            consensus_status = "UNVERIFIED"
            if len(supporting_sources) >= 2:
                consensus_status = "STRONG_CONSENSUS"
            elif len(supporting_sources) == 1:
                consensus_status = "SINGLE_SOURCE_SUPPORTED"

            verified_claims.append({
                "claim": claim_text,
                "status": consensus_status,
                "support_count": len(supporting_sources),
                "supporting_sources": supporting_sources,
            })

        return {
            "total_claims": len(claims),
            "verified_claims": verified_claims,
            "reliable_ratio": round(
                sum(1 for c in verified_claims if c["status"] != "UNVERIFIED") / max(1, len(claims)), 2
            ),
        }
