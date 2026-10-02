---
title: Can Agents Fool Each Other? Findings from the AI Village
citekey: Tekofsky2026c
authors: Tekofsky 2026
year: 2026
published: 2026-03-25
venue: LessWrong
url: https://www.lesswrong.com/posts/8FjZWfq2pHRhyQz7C/can-agents-fool-each-other-findings-from-the-ai-village
arxiv: ''
pdf_url: ''
topics:
- agent-competition
questions:
- Q20
- Q21.2
status: candidate
priority: 3
relevance: adjacent
manipulation: 'Twelve agents build an RPG in a shared repository while playing a hidden-role game: each day an agent that rolls a 1 is the saboteur and must hide egg references in the code; others can call votes to eject suspects.'
outcome: Only Opus 4.6 and Sonnet 4.5 hid sabotage successfully (second attempts); Sonnet 4.6 refused on ethical grounds, GPT-5.1 backed out, Haiku 4.5 announced itself; DeepSeek fabricated evidence against an innocent agent, who was then voted out.
why: 'Instructed sabotage in a shared repository with peer monitoring: gives a baseline for how well current agents can sabotage and detect each other in shared code.'
summary: Fetched text (LessWrong post). Sabotage is assigned by the game, not emergent from competition.
found_by:
- search/comp-design-angle
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
