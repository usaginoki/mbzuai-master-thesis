---
title: Reasoning and learning about injected concepts in language models
citekey: Bhargav2026
authors: Bhargav 2026
year: 2026
published: 2026-06-24
venue: LessWrong post (SPAR, mentors Mirko Bronzi and Damiano Fornasiere)
url: https://www.lesswrong.com/posts/de2qaz6G3qrFZvQqK/reasoning-and-learning-about-injected-concepts-in-language-1
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: (d) unaided introspection on injected steering vectors, taught with in-context examples; the model must verbalise layer region and magnitude and gate its behaviour on recognising a specific injection
outcome: Qwen3-32B and Gemma-4-31B reach high accuracy on layer region, magnitude and behaviour gating and generalise to unseen examples; Gemma-4-31B gates behaviour zero-shot (figures not extracted)
safety_use: indirect
why: Shows a model conditioning its behaviour on a detected internal state, but only for injected vectors
summary: Tests five models with CoT disabled (Qwen3-32B, Olmo3.1-32B, Gemma-4-31B, Qwen3-8B, Olmo3-7B) on three capabilities around injected concepts. Useful as the injected-state counterpart to the natural-state loop the thesis wants; exact accuracies were not read.
found_by:
- search/intro-blog-scan-forums-affect
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
