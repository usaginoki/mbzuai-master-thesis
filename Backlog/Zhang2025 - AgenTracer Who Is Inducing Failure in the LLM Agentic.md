---
title: "AgenTracer: Who Is Inducing Failure in the LLM Agentic Systems?"
citekey: Zhang2025
authors: "Zhang et al."
year: 2025
published: 2025-09-03
venue: "arXiv preprint"
url: https://arxiv.org/abs/2509.03312
arxiv: "2509.03312"
pdf_url: https://arxiv.org/pdf/2509.03312
topics:
- multiagent-friction
status: candidate
priority: 2
relevance: core
channel: "Multi-agent trajectories (TracerTraj, Who&When)"
manipulation: "Programmed fault injection and counterfactual replay of agent steps"
outcome: "Frontier LLMs <10% attribution accuracy; AgenTracer-8B >69% agent-level, 20% step-level; up to +18.18% over Gemini-2.5-Pro/Claude-4-Sonnet; 4.8-14.2% gains when fed back to MAS"
why: "Failure attribution: which agent's output causes downstream failure"
found_by:
- search/mas-error-propagation
cited_by: []
added: 2026-09-29
cited_by_count: 0
tags:
- type/candidate
---
