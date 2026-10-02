---
title: Cost-Effective Constitutional Classifiers via Representation Re-use
citekey: Cunningham2025
authors: Cunningham et al. 2025
year: 2025
published:
venue: Anthropic Alignment Science blog
url: https://alignment.anthropic.com/2025/cheap-monitors/
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Linear probes (mean-token, EMA, suffix) on intermediate activations, and retrained final layers sharing the policy model's backbone
outcome: Jailbreak/harmful content; EMA probes beat a dedicated classifier with 2% of policy-model parameters at negligible cost; two-stage setup cuts cost over 10x
timing: post-hoc
why: Cost argument for activation-based monitors as a first stage.
summary: A single retrained final layer matches a dedicated classifier a quarter the size of the policy model at about 4% of its cost; EMA linear probes outperform a classifier 2% the size at negligible cost. Two-stage classification reduces cost by over 10x without significant performance loss. Not yet tested against adaptive red teaming.
found_by:
- search/pred-activation-probes
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
