---
title: Probing and Steering Evaluation Awareness of Language Models
citekey: Nguyen2025
authors: Nguyen et al. 2025
year: 2025
published: 2025-07-02
venue: arXiv preprint
url: https://arxiv.org/abs/2507.01786
arxiv: '2507.01786'
pdf_url: https://arxiv.org/pdf/2507.01786
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Linear probes on Llama-3.3-70B-Instruct separating evaluation from deployment prompts
outcome: Whether the model represents a prompt as a test; current safety evaluations are classified as test-like
timing: pre-generation
why: Evaluation awareness is a precursor state for sandbagging/alignment faking and is readable from the prompt.
summary: Linear probes separate real-world evaluation and deployment prompts, suggesting the model internally represents the distinction. Existing safety evaluations are classified as artificial by the probes.
found_by:
- search/pred-activation-probes
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
