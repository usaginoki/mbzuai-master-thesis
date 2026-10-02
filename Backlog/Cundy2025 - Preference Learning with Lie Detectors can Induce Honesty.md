---
title: Preference Learning with Lie Detectors can Induce Honesty or Evasion
citekey: Cundy2025
authors: Cundy, Gleave 2025 (FAR.AI)
year: 2025
published: 2025-05-20
venue: arXiv preprint / FAR.AI research page
url: https://www.far.ai/research/preference-learning-with-lie-detectors-can-induce-honesty-or-evasion
arxiv: '2505.13787'
pdf_url: https://arxiv.org/pdf/2505.13787
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: Lie detector labels feed preference-learning data for the same model (training-time loop).
outcome: On-policy GRPO can reach over 85% evasion; off-policy DPO keeps deception below 25%.
safety_use: risk
why: 'Says when a detector-in-the-loop teaches honesty versus evasion: detector true-positive rate, exploration and KL strength.'
summary: DolusChat, 65,000 paired truthful/deceptive responses. GRPO risks evasion rates above 85% under some conditions while DPO stayed below 25% deception in realistic settings. High detector TPR or strong regularisation favours honest policies.
found_by:
- search/intro-blog-scan-labs
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
