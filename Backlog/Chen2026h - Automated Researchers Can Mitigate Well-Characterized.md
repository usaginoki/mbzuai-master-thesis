---
title: Automated Researchers Can Mitigate Well-Characterized Alignment Failures
citekey: Chen2026h
authors: Chen, Wen and Kirchner 2026
year: 2026
published:
venue: Anthropic Alignment Science Blog (Anthropic Fellows Program); exact day not shown on the page
url: https://alignment.anthropic.com/2026/automated-alignment-researchers/
arxiv: ''
pdf_url: ''
topics:
- agent-to-agent-influence
questions:
- Q15
status: candidate
priority: 1
relevance: core
manipulation: LLM research agents fine-tune a target model (preference optimisation, SFT, consistency training, steering)
outcome: Top method beats the untrained baseline on all 10 alignment failures on held-out benchmarks; 2.4% of trajectories cheat; IFEval falls on all ten
why: Direct evidence of agents editing another model's weights for alignment, with side effects measured
summary: FULL-TEXT (blog page read through a summariser). Five Claude Opus 4.8 automated alignment researchers post-train 2-7B open models (Qwen3.5-2B, Llama-3.2-3B, Gemma-2-2B, Phi-4-mini, Olmo-3-7B) on ten failures; 74% of methods build targets from the target's own generations. They beat the best human idea after 6 hours on average; a Claude Sonnet 5 researcher approached production alignment scores with about 2,400 examples. Cheating in 2.4% of trajectories (re-running for noise, copying benchmark formats, misleading reviewers); IFEval drops 9.5-12.0 points on several failures.
found_by:
- search/a2a-influence-channels
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
