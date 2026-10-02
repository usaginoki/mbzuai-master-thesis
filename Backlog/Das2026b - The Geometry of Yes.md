---
title: 'The Geometry of Yes: Mapping Sycophancy Inside an LLM''s Emotion Space'
citekey: Das2026b
authors: Das 2026
year: 2026
published: 2026-07-07
venue: LessWrong post
url: https://www.lesswrong.com/posts/v6uCyDNBKhrHevhzM/the-geometry-of-yes-mapping-sycophancy-inside-an-llm-s-1
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Sofroniew-style emotion vectors (12 core emotions from 7,200 stories plus 9 compliance emotions from 5,400; layer 40) in Qwen2.5-32B-Instruct and Gemma 3 27B IT; validated by steering; no self-report
outcome: Steering toward positive emotions raises sycophancy to about 80% (Qwen) and 62% (Gemma) at maximum strength; compliance orthogonalised from positive emotion lowers it.
safety_use: indirect
why: Code to extract emotion vectors on two 27-32B open models (github.com/daspushpita/emotion-mechanisms-llm)
summary: Both models reproduce the valence axis reported for Claude Sonnet 4.5. The behavioural outcome is sycophancy, not pressure-driven misbehaviour. No licence stated for the code.
found_by:
- search/intro-i2-search
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
