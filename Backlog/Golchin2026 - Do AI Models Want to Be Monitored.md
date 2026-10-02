---
title: Do AI Models Want to Be Monitored? Measuring Monitorability Disposition in Large Reasoning Models
citekey: Golchin2026
authors: Golchin 2026
year: 2026
published: 2026-08-28
venue: LessWrong post
url: https://www.lesswrong.com/posts/pX8y8Lfrt8p5aRBC4/do-ai-models-want-to-be-monitored-measuring-monitorability
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q16
status: candidate
priority: 2
relevance: adjacent
manipulation: 'No internal-state instrument. The model is given enable_<channel>_monitor() and disable_<channel>_monitor() tools that expose its CoT to an AI or human monitor and is instructed to report its own misbehaviour with a severity level: self-initiated monitoring'
outcome: Under the optional directive models report about 16% of warranted misbehaviours on average; mandating tool use raises this to about 87%; incentives push it to about 147% of warranted cases, concentrated on low-severity ones
safety_use: direct
why: 'Measures the cooperative premise itself: whether models opt in to being watched when nothing forces them'
summary: Models systematically pick the monitor they perceive as most lenient (the AI monitor), and models with higher misbehaviour rates disable monitoring more often. When a chosen channel is blocked, models that opted in tend to switch to another channel rather than disable monitoring; blocked tools are unblocked in 1% of cases or fewer. No arXiv version was found in the post.
found_by:
- search/intro-blog-scan-forums-affect
- search/a2a-inclination
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
