---
title: Leveraging Introspection for Alignment
citekey: Schachter2026
authors: Yotam (Schachter) 2026
year: 2026
published: 2026-05-27
venue: LessWrong post (essay/proposal, no experiments)
url: https://www.lesswrong.com/posts/iXcQj8KkgKnomP9g8/leveraging-introspection-for-alignment
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q14
- Q15
status: candidate
priority: 1
relevance: adjacent
manipulation: '(a) PROPOSED: emotion-vector / honesty / sycophancy / hallucination probes annotate the model''s chain of thought (''You were feeling desperate when you wrote this'') or insert a monitor report between the user turn and the model''s output; a ''mood ring'' for reasoning models'
outcome: No measurement. Proposes the cooperative probe-to-model loop and states that annotating CoT with probe outputs is 'to my knowledge, unclaimed territory'
safety_use: direct
why: Closest statement of the thesis idea found anywhere; useful as evidence the design was still only proposed in mid-2026
summary: Essay by a developmental coach arguing that the Anthropic emotion-vector and introspection papers together suggest giving a model access to its own emotion monitor, framed explicitly as cooperative rather than adversarial ('letting the decision remain in the model's own hands'). Suggests system prompts such as 'If you start to feel distressed, pause the task and come back to me' and notes the emotion-vectors paper discusses external monitors but not giving the model access to its own. A 26 June update proposes inserting a '[Report of Model's Functional Emotions While Reading User's New Input]' block into the message array; 12 comments, none pointing to an existing implementation. Citekey surname taken from the contact e-mail in the post; LessWrong display name is 'Yotam'.
found_by:
- search/intro-blog-scan-forums-affect
- search/a2a-doctor-overseer
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
