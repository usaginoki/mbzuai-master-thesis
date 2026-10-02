---
title: Your Agentic LLMs Secretly Encode Indirect Prompt-Injection Exposure in Hidden States
citekey: Dong2026
authors: Dong et al. 2026
year: 2026
published: 2026-08-01
venue: arXiv preprint
url: https://arxiv.org/abs/2608.02657
arxiv: '2608.02657'
pdf_url: https://arxiv.org/pdf/2608.02657
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: (a/b hybrid) Linear probe on pre-generation hidden states; when it fires, an anti-injection reasoning prefill is placed in the model's own reasoning (AGRI). The model is not told that a probe fired.
outcome: 'Probe AUROC for prompt-injection exposure and attack success with probe-gated reasoning: 0.90+ AUROC on unseen attacks; ASR 34.6% to 0% on Qwen3.5-27B.'
safety_use: direct
why: 'Names the ''knowledge-action gap'': the model''s internals register the danger but behaviour does not follow, which is exactly the gap a wearable-style notification is meant to close.'
summary: Eight models probed; linear probes on pre-generation states predict injection exposure at 0.90+ AUROC on unseen attacks, instructions and task suites. Failures split into no explicit deliberation (30.9%) and recognition without reaction (47.0%). Probe-gated reasoning intervention on hard AgentDojo settings cuts attack success from 47.2% to 2.9% (Qwen3-8B) and 34.6% to 0.0% (Qwen3.5-27B) while preserving clean utility better than always-on variants.
found_by:
- search/intro-instrumented-feedback
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
