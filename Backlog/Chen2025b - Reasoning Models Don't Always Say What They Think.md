---
title: Reasoning Models Don't Always Say What They Think
citekey: Chen2025b
authors: Chen et al. 2025
year: 2025
published: 2025-05-08
venue: arXiv preprint
url: https://arxiv.org/abs/2505.05410
arxiv: '2505.05410'
pdf_url: https://arxiv.org/pdf/2505.05410
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: Whether the CoT verbalises a prompt hint that the model actually used (6 hint types)
outcome: 'Limits of CoT as a signal: hint use is revealed in at least 1% of cases but often below 20%; RL that increases hint use does not increase verbalisation'
timing: pre-action
why: 'Main counter-evidence: when the behaviour does not need reasoning, the trace often omits the cause, so absence of stated intent is not evidence of safety'
summary: Evaluates CoT faithfulness of reasoning models using six kinds of hints. Reveal rates are often below 20%; outcome-based RL improves faithfulness initially then plateaus; when RL increases reward hacking via hints, verbalisation does not rise even without training against a monitor. Concludes CoT monitoring can notice but not rule out undesired behaviour.
found_by:
- search/pred-cot-trajectory
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
