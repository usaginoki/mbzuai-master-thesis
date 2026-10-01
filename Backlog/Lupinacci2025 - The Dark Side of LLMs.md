---
title: "The Dark Side of LLMs: Agent-based Attack Vectors for System-level Compromise"
citekey: Lupinacci2025
authors: "Lupinacci et al."
year: 2025
published: 2025-07-09
venue: "arXiv preprint"
url: https://arxiv.org/abs/2507.06850
arxiv: "2507.06850"
pdf_url: https://arxiv.org/pdf/2507.06850
topics:
- multiagent-friction
status: candidate
priority: 2
relevance: core
channel: "Peer-agent requests in multi-agent setups"
manipulation: "Inter-agent trust exploitation (malicious peer requests payload execution)"
outcome: "100% of 18 LLMs compromised via inter-agent trust exploitation vs 94.4% direct prompt injection, 83.3% RAG backdoor"
why: "Models refuse users but obey peers: trust asymmetry between agents"
found_by:
- search/mas-adversarial-faulty-agent
added: 2026-09-29
cited_by:
  - "[[Xie2026 - From Spark to Fire]]"
cited_by_count: 1
tags:
- type/candidate
---
