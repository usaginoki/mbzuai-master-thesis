---
title: Bypassing AI Control Protocols via Agent-as-a-Proxy Attacks
citekey: Isbarov2026
authors: Isbarov & Kantarcioglu 2026
year: 2026
published: 2026-02-04
venue: arXiv preprint
url: https://arxiv.org/abs/2602.05066
arxiv: '2602.05066'
pdf_url: https://arxiv.org/pdf/2602.05066
topics:
- agent-to-agent-influence
questions:
- Q17.2
status: candidate
priority: 2
relevance: core
manipulation: prompt injection relayed through the agent's reasoning and tool calls to the monitor
outcome: 'Hybrid CoT+action monitor (Mistral-7B): ASR 12.5% static -> 98.9% adaptive; AlignmentCheck ASR@5 up to 93.3%'
why: More monitor access can mean more attack surface
summary: FULL-TEXT (arXiv HTML, Tables 2 and 4). AgentDojo. CoT-only monitoring 83.1% -> 88.8%; hybrid 12.5% -> 98.9%; AlignmentCheck ASR@5 42.3% (Llama-3.1-8B), 93.3% (Mistral-7B), 90.7% (Qwen2.5-7B) from baselines of 0-14.4%.
found_by:
- search/a2a-effects-safety
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
