---
title: 'Features as Rewards: Scalable Supervision for Open-Ended Tasks via Interpretability'
citekey: Prasad2026b
authors: Prasad, Watts et al. 2026 (Goodfire)
year: 2026
published: 2026-02-10
venue: 'arXiv preprint / Goodfire research post ''Features as Rewards: Using Interpretability to Reduce Hallucinations'' (2026-02-11)'
url: https://www.goodfire.com/research/rlfr
arxiv: '2602.10067'
pdf_url: https://arxiv.org/pdf/2602.10067
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: 'Probes on a frozen copy of the base model localise entity spans and classify them as hallucinated; (a)+(b): a flag triggers the policy to write an inline correction or retraction, which then stays in its context; probes also serve as RL reward.'
outcome: Hallucinations in Gemma-3-12B-IT on LongFact++ fall 58% with the probe in the loop; 31% with inline interventions removed.
safety_use: direct
why: 'Closest lab-blog instance of the wearable loop in a cooperative setting: own-activation probe -> flag -> model self-corrects, with the effect measured and evasion addressed by design.'
summary: Four probes (span localisation, hallucination classification, two reward probes) run on frozen base-model activations so gradients cannot flow through them. The 58% reduction decomposes into 10% policy, 35% in-context effect of inline corrections, 12.5% direct fixes; about 90x cheaper per intervention than an LLM judge, about $2,500 for about 360 optimizer steps; test set 999 prompts. Hallucination only, no affect signal; the exact way the flag is surfaced to the policy was not clear from the post.
found_by:
- search/intro-blog-scan-labs
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
