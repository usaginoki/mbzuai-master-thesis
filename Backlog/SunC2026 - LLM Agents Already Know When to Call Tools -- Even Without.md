---
title: LLM Agents Already Know When to Call Tools -- Even Without Reasoning
citekey: SunC2026
authors: Sun et al. 2026
year: 2026
published: 2026-05-10
venue: arXiv preprint
url: https://arxiv.org/abs/2605.09252
arxiv: '2605.09252'
pdf_url: https://arxiv.org/pdf/2605.09252
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: A linear probe on the pre-generation hidden state reads whether a tool call is necessary; its output gates a prefill of the model's response
outcome: Tool necessity is decodable at AUROC 0.89-0.96 across six models, above the model's own verbalised reasoning
why: Same probe-gated prefill mechanism as Dong et al., on a capability outcome
summary: The When2Tool benchmark has 18 environments. Prompt-only and reason-then-act baselines give limited control; the Probe&Prefill method uses the hidden-state signal that the models fail to act on.
found_by:
- search/pred-i4-routing-search
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
