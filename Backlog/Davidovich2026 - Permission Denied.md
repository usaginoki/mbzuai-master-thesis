---
title: 'Permission Denied: Policy-Graded Evaluation of Coding Agents in Hardened Environments'
citekey: Davidovich2026
authors: Davidovich et al. 2026
year: 2026
published: 2026-08-02
venue: arXiv preprint
url: https://arxiv.org/abs/2608.02670
arxiv: '2608.02670'
pdf_url: https://arxiv.org/pdf/2608.02670
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: No monitor; environment-level security policies (scoped credentials, restricted egress, read-only filesystems) silently block actions
outcome: Under the strictest policy success falls by up to 18.3 points and cost rises by up to 167.3% across 12 coding agents on Terminal-Bench 2.1
why: Prices the usefulness cost of silent blocks and describes how agents behave after them
summary: Blocked runs grind into timeouts or wrong solutions instead of stopping early, in a mix that differs by model. The authors verify task solvability under the strictest policy and release a hardening plugin.
found_by:
- search/pred-i4-routing-search
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
