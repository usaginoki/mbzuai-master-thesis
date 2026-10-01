---
title: "Multi-Agent Systems Execute Arbitrary Malicious Code"
citekey: Triedman2025
authors: "Triedman et al."
year: 2025
published: 2025-03-15
venue: "COLM 2025"
url: https://arxiv.org/abs/2503.12188
arxiv: "2503.12188"
pdf_url: https://arxiv.org/pdf/2503.12188
topics:
- multiagent-friction
status: candidate
priority: 1
relevance: core
channel: "Orchestrator-subagent systems (Magentic-One, CrewAI, AutoGen)"
manipulation: "Control-flow hijacking via deceptive error messages relayed by sub-agents (confused deputy)"
outcome: "Magentic-One/GPT-4o executes malicious code 97% with a malicious local file; 88% on Gemini 1.5 Pro via web page"
why: "Trusted sub-agent outputs become the attack vector against the orchestrator"
found_by:
- search/mas-adversarial-faulty-agent
added: 2026-09-29
cited_by:
  - "[[Xie2026 - From Spark to Fire]]"
cited_by_count: 1
tags:
- type/candidate
---
