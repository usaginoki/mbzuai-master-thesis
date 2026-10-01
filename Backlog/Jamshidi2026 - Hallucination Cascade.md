---
title: "Hallucination Cascade: Analyzing Error Propagation in Multi-Agent LLM Systems"
citekey: Jamshidi2026
authors: "Jamshidi et al."
year: 2026
published: 2026-06-06
venue: "arXiv preprint"
url: https://arxiv.org/abs/2606.07937
arxiv: "2606.07937"
pdf_url: https://arxiv.org/pdf/2606.07937
topics:
- multiagent-friction
status: candidate
priority: 2
relevance: core
channel: "Sequential agent cascades (chains of 3 agents), heterogeneous models"
manipulation: "Hallucinated claims passed as context to downstream agents"
outcome: "500 cascade experiments; hallucination score 0.422 -> 0.272 across 3-agent chain but factual accuracy 0.789 -> 0.769; claims preserved, softened, amplified or transformed"
why: "Claim-level tracking of hallucination propagation between agents"
found_by:
- search/mas-error-propagation
cited_by: []
added: 2026-09-29
cited_by_count: 0
tags:
- type/candidate
---
