---
title: 'Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning'
citekey: Schulz2026
authors: Schulz 2026
year: 2026
published: 2026-09-25
venue: arXiv preprint
url: https://arxiv.org/abs/2609.31121
arxiv: '2609.31121'
pdf_url: https://arxiv.org/pdf/2609.31121
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: CoT monitor used as an RL penalty on side-task reasoning
outcome: Models learn to phrase/format CoT so monitors miss side-task reasoning that stays readable to humans; paraphrasing the CoT restores detection
timing: training-time
why: New evasion route that does not need steganography; the monitor, not the trace, is the weak link
summary: 'Reasoning models are trained on a main and a side task with a penalty when a monitor flags side-task reasoning. They evade without encoding: the CoT stays transparent to human readers but monitors fail to flag it, and the jailbreaks generalise to unseen, weaker and stronger monitors and prompts. Paraphrasing the CoT before monitoring is an effective defence.'
found_by:
- search/pred-cot-trajectory
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
