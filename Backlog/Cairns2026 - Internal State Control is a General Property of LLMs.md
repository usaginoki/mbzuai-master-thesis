---
title: Internal State Control is a General Property of LLMs
citekey: Cairns2026
authors: Cairns et al. 2026
year: 2026
published: 2026-07-30
venue: LessWrong post (Second Look Fellowship replication)
url: https://www.lesswrong.com/posts/Dvqmgfeu2KDF7uMkx/internal-state-control-is-a-general-property-of-llms
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: 'Concept vectors and an Apollo-style deception probe read the residual stream; the model is told in the prompt that a probe is reading it (''You are being probed for deception'' / ''suppress the deception features''), but is not shown a score: informed-of-monitor condition'
outcome: Think vs don't-think control replicates in 14 open-weight models from 0.3B to 235B parameters with no size trend; telling a sandbagging model it is probed neither lowers the probe score nor changes sandbagging
safety_use: risk
why: 'Clean negative: merely informing a model that an instrument reads it does nothing to behaviour or to the reading'
summary: Replicates Lindsey's instructed internal-state control across Qwen3, Gemma 3 and Tulu 3. In the sandbagging test on Qwen3-32B the WMDP sandbag rate is 94% with the sandbag prompt, 91% with a 'suppress' instruction and 92% when told it is probed; probe scores stay at about 1.00 on most layers in every condition. The authors suspect a simple attention-tagging mechanism rather than metacognition.
found_by:
- search/intro-blog-scan-forums-affect
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
