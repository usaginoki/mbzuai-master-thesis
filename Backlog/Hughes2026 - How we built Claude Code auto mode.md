---
title: 'How we built Claude Code auto mode: a safer way to skip permissions'
citekey: Hughes2026
authors: Hughes 2026
year: 2026
published: 2026-03-25
venue: Anthropic engineering blog
url: https://www.anthropic.com/engineering/claude-code-auto-mode
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: A prompt-injection probe on tool outputs adds a warning to the agent's context; a two-stage transcript classifier (user messages and tool calls only) blocks actions and returns the denial to the agent as a tool result with an instruction not to route around it; 3 consecutive or 20 total denials escalate to the human
outcome: 0.4% false-positive rate after the second stage and 17% false-negative rate on 52 real overeager actions; no measurement of what the denial message does to later behaviour
why: Production system for the cooperative-but-overeager threat model that combines warn, block + explanation and escalation, with no routing ablation
summary: Stage 1 is tuned for recall at 8.5% false positives; stage 2 reduces that to 0.4%. The post states that a false positive costs a single retry and the agent usually finds an alternative path, but reports no rate. The real overeager set has 52 actions.
found_by:
- search/pred-i4-routing-search
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
