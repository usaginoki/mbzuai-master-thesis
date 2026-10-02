---
title: Can LLMs Reliably Self-Report Adversarial Prefills, and How?
citekey: Nguyen2026
authors: Nguyen et al. 2026
year: 2026
published: 2026-06-22
venue: EMNLP 2026 (Main)
url: https://arxiv.org/abs/2606.23671
arxiv: '2606.23671'
pdf_url: https://arxiv.org/pdf/2606.23671
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: Asks the model whether a prior harmful response was its own intent or was forced by a prefill attack. Mechanism checked white-box by orthogonalising weights against the refusal direction.
outcome: No model reliably recognises its compromised outputs; models claim intent on prefilled responses 25.3% of the time on average; ablating the refusal direction collapses the prefilled-vs-natural gap to near zero; introspection training improves accuracy but raises attack success rate on most models.
safety_use: direct
why: Direct test of 'does the model notice it has been jailbroken?' - mostly no, and the signal is refusal reasoning rather than a dedicated self-monitor; training for it can backfire.
summary: Ten open-weight models from 3B to 70B on four safety benchmarks. The introspective signal stems mainly from reasoning about safety and refusal; framing the question as internal intention versus external tampering elicits qualitatively different answers; introspection training does not transfer to the tampering probe.
found_by:
- search/intro-capability
- search/intro-safety-uses-and-risks
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
