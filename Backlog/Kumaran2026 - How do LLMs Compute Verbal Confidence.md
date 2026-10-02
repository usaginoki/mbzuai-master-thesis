---
title: How do LLMs Compute Verbal Confidence
citekey: Kumaran2026
authors: Kumaran et al. 2026
year: 2026
published: 2026-03-18
venue: ICML 2026
url: https://arxiv.org/abs/2603.17839
arxiv: '2603.17839'
pdf_url: https://arxiv.org/pdf/2603.17839
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: activation steering, patching, noising, swap and attention-blocking experiments; linear probes at answer-adjacent positions (Gemma 3 27B, Qwen 2.5 7B, Magistral Small 24B)
outcome: Verbal confidence is computed automatically during answering, cached at the first post-answer position and retrieved later; the cached representation explains variance in stated confidence beyond token log-probabilities.
safety_use: indirect
why: 'Stated uncertainty is a readout of a real internal evaluative signal: the best-supported case of a self-report tracking a probe-readable state.'
summary: Convergent causal evidence for 'cached retrieval' of confidence across TriviaQA, BigMath and MMLU. Probing and variance partitioning show the cache carries answer-quality information beyond log-probs. Follow-up (arXiv 2604.22271) shows these post-answer activations predict error detection beyond verbal confidence and predict which errors the model can correct, replicated in Gemma 3 27B and Qwen 2.5 7B.
found_by:
- search/intro-capability
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
