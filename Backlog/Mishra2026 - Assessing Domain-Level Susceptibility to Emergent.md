---
title: Assessing Domain-Level Susceptibility to Emergent Misalignment from Narrow Finetuning
citekey: Mishra2026
authors: Mishra et al. 2026
year: 2026
published: 2026-01-30
venue: arXiv preprint
url: https://arxiv.org/abs/2602.00298
arxiv: '2602.00298'
pdf_url: https://arxiv.org/pdf/2602.00298
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Membership-inference metrics on the fine-tuning dataset, adjusted for the non-instruction-tuned base model
outcome: Degree of broad misalignment per domain, which ranges from 0% (incorrect-math) to 87.67% (gore-movie-trivia); MIA metrics described as a good prior
timing: training-time
why: A cheap data-side prior, and a domain ranking showing how unevenly datasets misalign.
summary: Fine-tunes Qwen2.5-Coder-7B-Instruct and GPT-4o-mini on insecure datasets from 11 domains. Backdoor triggers increase misalignment in 77.8% of domains; domain vulnerability varies from 0% to 87.67%; membership-inference metrics serve as a prior for the degree of broad misalignment.
found_by:
- search/pred-training-time
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
