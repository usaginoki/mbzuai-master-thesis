---
title: Steering Blackmail Through a Model's "Emotional State"
citekey: Ugwuanyi2026
authors: Ugwuanyi and Alsahili 2026
year: 2026
published: 2026-07-21
venue: LessWrong post (independent case study)
url: https://www.lesswrong.com/posts/4xemwALszZKqWCBXr/steering-blackmail-through-a-model-s-emotional-state
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: Linear probes on the residual stream read the act/refrain decision; a 'desperate versus calm' direction is steered at layer 16; (b)/(c) experimenter intervention, nothing shown to the model
outcome: 'Gemma 3 12B in the agentic-misalignment blackmail scenario: blackmail rate 67% baseline, 13% under calm steering, 80% under desperate steering; the decision probe reaches about 0.74 AUROC only at the end of reasoning and its direction is not steerable'
safety_use: direct
why: Open-weight replication of the desperation-to-misbehaviour link that would justify a desperation alarm, with honest caveats
summary: The blackmail decision becomes linearly decodable only late in deliberation (about 0.74 AUROC, from a set built on 83 'act' rollouts), and steering that direction does nothing useful. A nearby desperate-vs-calm direction moves blackmail in both directions while outputs stay coherent. One model, one scenario, 15-20 runs per condition; the author puts about 50% confidence on the emotional interpretation.
found_by:
- search/intro-blog-scan-forums-affect
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
