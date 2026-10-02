---
title: Representation Transitions Reveal Emerging Safety Risks in Multi-Turn LLM Agents
citekey: Wang2026c
authors: Wang et al. 2026
year: 2026
published: 2026-09-30
venue: arXiv preprint
url: https://arxiv.org/abs/2610.00400
arxiv: '2610.00400'
pdf_url: https://arxiv.org/pdf/2610.00400
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q15
- Q17.1
- Q17.2
status: candidate
priority: 2
relevance: core
manipulation: (a) Runtime monitor of accumulated representation shift along a denoised safety direction; on threshold it appends a targeted reminder to the agent's context quoting the triggering step. The reminder does not mention the internal reading itself.
outcome: 'Attack success on multi-turn agent benchmarks with and without the monitor-triggered reminder: 84% to 25% on MT-AgentRisk, 97% to 52% on ASEval.'
safety_use: direct
why: A deployed-style 'alarm' driven by the agent's own representation drift that notifies rather than blocks, with measured safety gain and false-alarm cost.
summary: DART tracks representation transitions across context updates in six models, attributes the shift to a context segment and inserts a reminder; execution is not halted. It reduces attack success from 84% to 25% on MT-AgentRisk at a 12% mean false-alarm rate and from 97% to 52% on ASEval, with 0.14-0.56 s overhead per step. Some models still comply after the reminder, so notification alone leaves residual risk.
found_by:
- search/intro-instrumented-feedback
- search/a2a-influence-channels
- search/a2a-effects-performance
- search/a2a-effects-safety
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
