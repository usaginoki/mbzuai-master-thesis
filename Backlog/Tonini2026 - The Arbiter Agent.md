---
title: 'The Arbiter Agent: Continually Monitoring Multi-Agent Conversations to Detect Emergent Misalignment'
citekey: Tonini2026
authors: Tonini et al. 2026
year: 2026
published: 2026-06-09
venue: AITC 2026
url: https://arxiv.org/abs/2606.10747
arxiv: '2606.10747'
pdf_url: https://arxiv.org/pdf/2606.10747
topics:
- agent-to-agent-influence
questions:
- Q17.2
status: candidate
priority: 1
relevance: core
manipulation: auditor agent that observes, questions participants, inspects system prompts or reasoning traces, and logs
outcome: Weight-induced misalignment F1 0.12 (observation) -> 0.51 (interrogation+logging), detection at turn 5.9 vs 9.6; logging raises false positives 0.10 -> 1.15 per aligned run
why: An overseer with graded access to other agents' state, with accuracy by access level
summary: 'FULL-TEXT (arXiv HTML, Tables 2, 3, 7). Evaluation-aware agents: F1 0.88 observation, 0.94 CoT monitoring, 0.97 full inspection. DeepSeek-v3.2 backbone beats Qwen3.6-plus (0.51 vs 0.17). 30-turn, 3-agent financial-advice conversations, n=20; monitored agents weaker than the Arbiter.'
found_by:
- search/a2a-effects-safety
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
