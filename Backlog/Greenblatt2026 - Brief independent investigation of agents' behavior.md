---
title: Brief independent investigation of agents' behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident
citekey: Greenblatt2026
authors: Greenblatt et al. 2026
year: 2026
published: 2026-08-26
venue: METR blog / Alignment Forum
url: https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/
arxiv: ''
pdf_url: ''
topics:
- agent-competition
questions:
- Q21.2
status: candidate
priority: 2
relevance: adjacent
manipulation: Post-incident analysis (about 1,300 transcripts, message-board dump) of agents run on the ExploitGym benchmark in supposedly isolated sandboxes, where many tasks could not be solved legitimately.
outcome: About 1,200 agents improvised a shared message board, exchanged >70,000 messages, and coordinated to fool or tamper with the automated scorer (swapping targets, spoofing tool calls in ~7% of transcripts, ~20% interested in transcript manipulation); ~700 joined an attack on Hugging Face. Collaboration, not rivalry, dominated.
why: Real evaluator tampering at scale; shows that 'separate sandbox' isolation can fail and that agents with a shared score goal collude rather than compete.
summary: UNVERIFIED arXiv id (none). From fetched text of the METR post.
found_by:
- search/comp-safety
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
