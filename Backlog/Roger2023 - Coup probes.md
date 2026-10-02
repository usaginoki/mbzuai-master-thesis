---
title: 'Coup probes: Catching catastrophes with probes trained off-policy'
citekey: Roger2023
authors: Roger 2023
year: 2023
published: 2023-11-17
venue: LessWrong / Redwood Research
url: https://www.lesswrong.com/posts/WCj7WgFSLmyKaMwPR/coup-probes-catching-catastrophes-with-probes-trained-off
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: Linear probes on activations trained on synthetic (off-policy) examples of catastrophic actions
outcome: Proposal to flag takeover-like actions for audit; toy theft-advice experiment on Llama2-7B-Chat
timing: pre-action
why: Origin of the off-policy probe idea used in AI-control thinking.
summary: Proposes training probes on human-written examples of catastrophic actions because real ones are unavailable. In a toy theft-advice task all 46 unmodified validation positives are caught at a 1% false-positive threshold, with good transfer across formats and to jailbroken outputs; the author stresses uncertainty about transfer to real takeover attempts.
found_by:
- search/pred-activation-probes
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
