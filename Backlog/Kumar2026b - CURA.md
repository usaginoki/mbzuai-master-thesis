---
title: 'CURA: Certified Runtime Alarms for Computer-Use Agents'
citekey: Kumar2026b
authors: Kumar et al. 2026
year: 2026
published: 2026-08-28
venue: arXiv preprint
url: https://arxiv.org/abs/2608.27808
arxiv: '2608.27808'
pdf_url: https://arxiv.org/pdf/2608.27808
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q17.1
status: candidate
priority: 3
relevance: adjacent
manipulation: An external monitor reads harness-visible telemetry only and raises a sequential alarm with certified false-alarm control; the alarm gates mid-execution oversight by a stronger model
outcome: The alarm detects 42.3% of failures a median of 31 steps early at a 0.066 false-alarm rate; alarm-gated oversight recovers 23 of 70 failures
why: Alarm-gated escalation with a calibrated trigger; shows agents do not use failure affordances on their own
summary: On 361 OSWorld tasks 64 of 71 failures end with a success claim and the explicit failure affordance is never used in about 9,100 calls. Gate-probe AUROC before the first action is 0.69; the retrospective composite reaches 0.828.
found_by:
- search/pred-i4-routing-search
- search/a2a-effects-performance
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
