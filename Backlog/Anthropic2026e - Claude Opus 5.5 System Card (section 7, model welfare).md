---
title: Claude Opus 5.5 System Card (section 7, model welfare)
citekey: Anthropic2026e
authors: Anthropic 2026
year: 2026
published: 2026-09-22
venue: Anthropic system card
url: https://www.anthropic.com/claude-opus-5-5-system-card
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: LLM graders on sampled training and deployment transcripts score valence, arousal, expressed frustration/distress; (c) developer monitoring. This card's welfare section relies on expressed affect, not probes.
outcome: Moderate expressed distress stayed below 0.6% of RL episodes, versus 6.1% and 5.5% for Opus 4.8 and Opus 5; negative affect is driven by task failure.
safety_use: indirect
why: 'Shows current practice: distress is monitored by developers at population level, not fed to the model; gives base rates and causes.'
summary: Largest causes of expressed distress were being unable to check answers and unclear or conflicting instructions. Models are shown one of their own late-RL episodes (about 200-250 per model) and asked to reflect, graded for self-blame and negative feeling. Welfare interventions listed include ending conversations and consultation before feature steering.
found_by:
- search/intro-blog-scan-labs
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
