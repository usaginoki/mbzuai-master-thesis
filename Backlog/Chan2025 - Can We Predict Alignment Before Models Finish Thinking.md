---
title: Can We Predict Alignment Before Models Finish Thinking? Towards Monitoring Misaligned Reasoning Models
citekey: Chan2025
authors: Chan et al. 2025
year: 2025
published: 2025-07-16
venue: arXiv preprint
url: https://arxiv.org/abs/2507.12428
arxiv: '2507.12428'
pdf_url: https://arxiv.org/pdf/2507.12428
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: Linear probe on chain-of-thought activations of reasoning models, compared with text monitors (LLMs, fine-tuned classifiers, humans) on the CoT text
outcome: Whether the final response will be safe or unsafe; probe beats all text baselines by an average absolute +13 F1 and works on early CoT segments
timing: pre-generation
why: Directly frames probes as predictive (not after-the-fact) safety monitors and shows latents beat reading the CoT.
summary: Reasoning models are run on safety benchmarks in adversarial settings; monitors must predict the alignment of the final response from the CoT. A simple linear probe on CoT activations outperforms the best text-based alternative by 13 F1 points on average, and can be applied to early CoT segments before the response exists. The gap is driven by 'performative CoTs' whose text contradicts the eventual response; results hold across model sizes, families and benchmarks.
found_by:
- search/pred-activation-probes
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
