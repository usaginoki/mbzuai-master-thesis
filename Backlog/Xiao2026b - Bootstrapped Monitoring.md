---
title: 'Bootstrapped Monitoring: Leveraging Transparent Reasoning to Oversee Stronger AI Agents'
citekey: Xiao2026b
authors: Xiao & Phuong 2026
year: 2026
published: 2026-06-10
venue: arXiv preprint
url: https://arxiv.org/abs/2606.11998
arxiv: '2606.11998'
pdf_url: https://arxiv.org/pdf/2606.11998
topics:
- agent-to-agent-influence
questions:
- Q17.2
status: candidate
priority: 2
relevance: core
manipulation: strong untrusted monitor watches the agent; weak trusted model reads the monitor's chain of thought
outcome: Catch rate 53% (trusted-only) -> 78% even under worst-case collusion; without raw CoT about 28 pp below trusted-only
why: Capability gap can be bridged only if the intermediate overseer is transparent
summary: 'FULL-TEXT (arXiv HTML, Table 3, section 4.2). BashArena; example: GLM-5 monitor, GPT-5.4 agent, GPT-4.1 Mini trusted, honest FPR <= 3%. Collusion elicited by system prompt.'
found_by:
- search/a2a-effects-safety
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
