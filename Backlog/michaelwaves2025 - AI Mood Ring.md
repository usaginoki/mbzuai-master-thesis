---
title: 'AI Mood Ring: A Window Into LLM Emotions'
citekey: michaelwaves2025
authors: michaelwaves 2025
year: 2025
published: 2025-12-06
venue: LessWrong post
url: https://www.lesswrong.com/posts/A5Byr2jkBJpnBdx23/ai-mood-ring-a-window-into-llm-emotions
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Seven emotion vectors (joy, love, sadness, surprise, disgust, fear, anger) from Qwen3-14B; activations are projected by cosine similarity and the dominant emotion is coloured per token for a human viewer. Not fed back to the model.
outcome: A visualisation project ('a fun weekend project'); no behavioural measurement.
safety_use: none
why: Shares the 'mood ring' name with Schachter's proposal but is a human-facing display, so it is not prior work on the feedback design.
summary: Weekend project that colours each token of a Qwen3-14B response by its dominant emotion-vector projection, for human inspection on a website. Page-summary read only; the readout is never placed in the model's context.
found_by:
- search/intro-i1-search
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
