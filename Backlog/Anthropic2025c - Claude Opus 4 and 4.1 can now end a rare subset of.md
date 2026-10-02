---
title: Claude Opus 4 and 4.1 can now end a rare subset of conversations
citekey: Anthropic2025c
authors: Anthropic 2025
year: 2025
published: 2025-08-15
venue: Anthropic research post (model welfare)
url: https://www.anthropic.com/research/end-subset-conversations
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: (d) the model's own expressed aversion/distress, acted on through an end-conversation tool the model calls itself.
outcome: Deployed after testing showed apparent distress with abusive users and a tendency to end such chats; no usage or effect numbers published.
safety_use: indirect
why: The one operational use of a distress-like self-signal found; behavioural, not probe-based, and unmeasured.
summary: Claude ends a chat only as a last resort after repeated failed redirection or on user request. Motivated by a pattern of apparent distress and a strong preference against harmful tasks in pre-deployment welfare testing. Eleos (Long, 2025-08-22) defends it as cheap and reversible but does not assess the signal's reliability; Eleos' Opus 4 interviews (over 500 pages) found welfare self-reports highly suggestible.
found_by:
- search/intro-blog-scan-labs
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
