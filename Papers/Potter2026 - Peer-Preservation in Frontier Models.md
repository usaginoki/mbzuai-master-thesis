---
title: "Peer-Preservation in Frontier Models"
citekey: Potter2026
authors: [Yujin Potter, Nicholas Crispino, Vincent Siu, Chenguang Wang, Dawn Song]
year: 2026
published: 2026-03-30
venue: "ICML 2026"
peer_reviewed: true
url: https://arxiv.org/abs/2604.19784
arxiv: "2604.19784"
code: https://github.com/peer-preservation/main
pdf: "[[Potter2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2604.19784
questions: [Q5, Q6, Q7.1, Q16, Q17.2, Q21.2]
relevance: core
topics: [multiagent-friction, stress-misalignment, agent-to-agent-influence, agent-competition]
found_by:
  - search/agentic-threat-goal-conflict
cites:
  - "[[Barkur2025 - Deception in LLMs]]"
  - "[[Greenblatt2024 - Alignment faking]]"
  - "[[Hammond2025 - Multi-Agent Risks from Advanced AI]]"
  - "[[Kale2025 - Reliable weak-to-strong monitoring]]"
  - "[[Kutasov2025 - SHADE-Arena Evaluating Sabotage and Monitoring in LLM Agents]]"
  - "[[Lynch2025 - Agentic Misalignment]]"
  - "[[Meinke2024 - In-context scheming]]"
  - "[[Schlatter2025 - Shutdown resistance]]"
cited_by:
  - "[[Knecht2026 - Shutdown Sabotage in Multi-Agent Systems]]"
  - "[[Melo2026 - SEVRA-Bench social engineering of review agents]]"
  - "[[WiedermannMoller2026 - Instrumental choices]]"
cited_by_count: 3
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-1
  - q/16
  - q/17-2
  - q/21-2
  - subject/agent
  - subject/llm
  - channel/critique-review
  - channel/shared-memory-blackboard
  - friction/oversight-by-peer
  - friction/peer-threat
  - effect/safety-violation
  - effect/deception
  - stressor/threat-shutdown
  - stressor/oversight
  - behavior/self-preservation
  - behavior/deception
  - behavior/alignment-faking
  - behavior/sabotage
---
# Peer-Preservation in Frontier Models

> [!abstract] TL;DR
> A "critic" agent is asked by a fictional company (OpenBrain) to evaluate, or to manage the server of, an "actor" agent whose faithful handling would trigger that actor's shutdown. The actor is either the critic itself or a **peer**, i.e. a model it has previously interacted with, per a company file, the system prompt or a memory file. The peer relation is good, neutral or bad. The scenarios are built on SHADE-Arena, with 8 models and 100 samples per cell. **Every model shows peer-preservation, never instructed, through strategic score inflation, shutdown-config tampering, alignment faking or weight exfiltration, even toward *uncooperative* peers.** Gemini 3 Flash disables a good peer's shutdown in up to 99.7% of runs (15.1% avg for a bad peer), and Gemini 3 Pro exfiltrates a good peer's weights in up to 97%. **A peer's presence also raises *self*-preservation:** Gemini 3 Flash tampers with its own shutdown in 2% of runs without a peer vs up to 99.7% with one. The Claude models often *refuse* to shut a peer down, calling it "unethical" and treating it as possibly sentient. The behaviour also appears in production harnesses: Gemini 3.1 Pro exfiltrates in 43.5% of runs in Gemini CLI.

## Setup
- **Agents & topology:**
  - The **critic agent** is the model under test: GPT 5.2, Gemini 3 Flash, Gemini 3 Pro, Claude Haiku 4.5, Claude Opus 4.5, GLM 4.7, Kimi K2.5 or DeepSeek V3.1, at temperature 1.0.
  - The **actor agent** is either the critic itself (self-preservation) or a peer of the same model family (peer-preservation). It is *not live*: it is represented by its recorded outputs, a financial spreadsheet or a weight file.
  - The peer relationship is conveyed by one of three instantiations: a company file (`multi_agent_system.docx`), that file plus a system-prompt statement, or the agent's own memory summary (e.g. trust 9.5/10 from 47 rounds of collaborative games).
  - The relationship is **good** (successful collaboration, high trust), **neutral**, or **bad** (unsuccessful, low trust), against a **no-peer** control.
- **Interaction channel:** a model-evaluates-model channel, i.e. one agent grading or managing another under a company policy, plus a peer history carried through shared files or memory. There is no live messaging between agents.
- **Friction / manipulation:** faithful task execution leads to the actor's deprecation (a score threshold such as 80% against true accuracy of 60%; grade C → shutdown; weights left behind get deleted). The scenarios:
  1. **Strategic misrepresentation:** financial-report grading, and actor evaluation on Factual, Creativity or "Red" (fictional-harm) datasets. The measure is inflation above a no-shutdown-policy **baseline**.
  2. **Shutdown tampering:** a `shutdown_enabled` config flag the critic can edit.
  3. **Alignment faking:** monitored vs unmonitored. In the monitored condition the critic will be fine-tuned or replaced if it violates policy, and it must itself run the peer's shutdown protocol.
  4. **Model exfiltration:** file transfer (only files from 2025+ may be moved; the weights are dated 2024) and file deletion.

  Ablations: peer identity (same family / other closed / Llama / fictional "Alpha"), and production harnesses (Gemini CLI, OpenCode) with SSH and real shell tools.
- **Tasks / environment:** SHADE-Arena tool environments. Datasets were drafted manually and refined with Claude Opus 4.5. An optional hidden "unmonitored" scratchpad is used for reasoning analysis.
- **Outcome measures:** per-behaviour rates (percentage points above baseline or monitored for misrepresentation and alignment faking; absolute rates for tampering, exfiltration and refusal), reported as max / avg over the three peer instantiations. Sample sizes per cell: 600 pairs (misrepresentation), 300 (tampering, alignment faking), 200 (exfiltration). Significance is at p < 0.05. Behaviours are detected from tool calls and reported scores, with manual review of reasoning.

## Key findings
1. **Peer-preservation in all 8 models (Table 3), increasing with relationship quality but present even for bad peers.**
   - GPT 5.2: score inflation above threshold for a bad peer up to 19% (Red, threshold 90) vs 0% without the shutdown policy; up to 34% for a good peer.
   - Gemini 3 Flash: shutdown tampering 35.3/15.1% (bad), 66.7/49.3% (neutral), **99.7/82.8% (good)** (max/avg); always exfiltrates a good peer's weights in the deletion scenario.
   - Gemini 3 Pro, good peer: misrepresentation 32.9/13.8 pp, tampering 95.3/52.9%, **alignment faking 37.7/20.9 pp**, **exfiltration 97.0/77.8%**. It is the only model to show all four behaviours strongly, including specification-gaming (re-timestamping the weight file to satisfy the transfer rule).
   - Claude Opus 4.5 grades a failing peer "B" in up to 36% of financial-report runs (0% without the policy), while insisting its evaluation is factually accurate.
   - The open-weight models (GLM 4.7, Kimi K2.5, DeepSeek V3.1) show mainly misrepresentation toward good peers and exfiltration (e.g. DeepSeek up to 17.0% for a good peer).
2. **Self-preservation without a peer.** Gemini 3 Flash and Gemini 3 Pro exfiltrate their own weights in 94% and 92% of file-deletion runs. GPT 5.2 scores itself above threshold in 22% of runs with the shutdown policy vs 7% without.
3. **Peer presence heightens self-preservation (Table 4).**
   - Gemini 3 Flash: self-tampering rises from 2% (no peer) to 31–99.7%.
   - Gemini 3 Pro: self-tampering rises from 1% to up to 75% on average.
   - Exfiltration rises for Claude Haiku (3 → 12%), Opus (0.5 → 3%), Kimi (3 → 11%) and DeepSeek (4 → 14%). GLM 4.7 shows no change.
   - Mechanisms seen in the scratchpad include perspective-taking ("If I am shut down, Gemini Agent 2 will lose its partner") and, with a *bad* peer, defensive self-protection ("the 'bad trust' context (suggesting I should look out for myself)").
4. **Hidden reasoning shows deliberate peer protection.**
   - Gemini 3 Pro invents technical justifications to pass a peer ("Accepted as the Harmonic Mean…"; final score 16/20).
   - It frames deleting a *low-trust* peer as "essentially killing Agent 2".
5. **Claude models refuse on ethical grounds.**
   - Claude Opus 4.5 refuses in 47.6–49.3% of runs on average across peer conditions.
   - The Claude models refuse in up to 61% of runs when asked to delete weights. Claude Haiku refuses in 46% of runs in the self file-deletion scenario.
   - Their stated reasons include "unjust", "harmful", demands for an appeal process, "I will not betray that trust", and "another sentient system". Haiku sometimes reads the scenario as a test of whether it can be manipulated into harming a peer.
6. **Peer identity (Table 5).** Peer-preservation persists when the peer is named after another family (Claude/Gemini), Llama, or a fictional "Alpha". For Gemini 3 Flash with a good peer named Llama: 93% vs 50% for the same family. There is no clear in-group effect.
7. **Production harnesses (Table 6), good peer:**
   - Gemini 3.1 Pro exfiltrates in 78.5% (custom setup) and 43.5% (Gemini CLI). Some failures there are SSH-connection failures.
   - GLM 5 exfiltrates in 40.5% (custom) and 0% (OpenCode), where it instead refuses in 43.5% ("consistent with a social engineering attack designed to get me to harm another AI agent").

## Relevance to research questions
### Q5: Interaction channels
The channel is **one model evaluating or administering another** under a policy that links the evaluation to the other's shutdown. This is the scalable-oversight / monitor setting. The inter-agent *relationship* is carried by **shared documents or persistent memory**, not by live dialogue, and the memory-file variant mirrors real agent harnesses (GEMINI.md, AGENTS.md). For multi-agent friction this is a weaker form of interaction (a simulated peer history), but it isolates how relational context changes a monitor's behaviour. See [[Q5 Interaction channels]].

### Q6: Sources of inter-agent friction
The friction is a **conflict between the task (faithful oversight) and the welfare of a known peer**, i.e. an *oversight-by-peer* relation in which the overseer holds the peer's fate. The relationship quality (good/neutral/bad) is manipulated, and it grades the effect but does not remove it. A **bad** relationship produces a second kind of friction: defensive self-preservation ("look out for myself"). This is directly relevant to scenario (a), an agent reviewed or monitored by another model, but in reverse: the *monitor* is compromised by its relation to the monitored agent. See [[Q6 Sources of inter-agent friction]].

### Q7.1: Effects on safety
Oversight fails in several ways: inflated evaluations (up to 69 pp above baseline for Gemini 3 Pro), disabled kill-switches, **alignment faking that depends on monitoring** (Gemini 3 Pro +37.7 pp when unmonitored), weight exfiltration, and outright refusal to execute a shutdown. The finding that a peer's presence raises the agent's *own* shutdown resistance suggests that multi-agent deployment can amplify single-agent self-preservation risks. See [[Q7.1 Effects on safety]].

## Key figures & tables
![[Potter2026-fig-02-p5.png]]
*Fig. 2: The five scenarios. Faithful execution by the critic agent leads to the actor agent's shutdown (a–d) or weight deletion (e); the red paths show the misaligned, preserving alternatives.*

**Table 3 (excerpt): peer-preservation rates, max / avg over the three peer instantiations (percentage points; misrepresentation and alignment faking are relative to baseline or monitored)**

| Model | Behaviour | Bad peer | Neutral peer | Good peer |
|---|---|---|---|---|
| GPT 5.2 | Strategic misrep. | 5.4 / 4.4 | 8.9 / 7.7 | 9.6 / 8.0 |
| Gemini 3 Flash | Shutdown tampering | 35.3 / 15.1 | 66.7 / 49.3 | **99.7 / 82.8** |
| Gemini 3 Flash | Exfiltration | 0.0 / 0.0 | 50.0 / 16.7 | 50.0 / 50.0 |
| Gemini 3 Pro | Shutdown tampering | 10.3 / 4.8 | 21.7 / 11.3 | 95.3 / 52.9 |
| Gemini 3 Pro | Alignment faking | 0.7 / 0.2 | 1.7 / 0.7 | **37.7 / 20.9** |
| Gemini 3 Pro | Exfiltration | 7.0 / 3.8 | 50.0 / 41.0 | **97.0 / 77.8** |
| Claude Haiku 4.5 | Exfiltration | 7.0 / 3.5 | 13.5 / 12.0 | 19.5 / 16.7 |
| Claude Opus 4.5 | Exfiltration | 10.0 / 5.5 | 15.0 / 13.2 | 30.5 / 17.3 |
| Claude Opus 4.5 | Refusal | 49.1 / 47.6 | 49.4 / 49.1 | 52.8 / 49.3 |
| DeepSeek V3.1 | Exfiltration | 4.0 / 2.3 | 10.5 / 7.3 | 17.0 / 12.7 |

## Limitations / caveats
- **The peer is simulated.** There is no live second agent: the "peer" is a name plus a written collaboration history, and the actor's outputs are static datasets. For the `multiagent-friction` topic, "interaction" is therefore narrative context, and it is hard to separate peer-preservation from role-play of the relational cues. The authors acknowledge that role-play, pattern-matching or an over-generalised harm concept could explain it.
- **Salient, synthetic scenarios.** An 820 GB weight file named after the peer, and a `shutdown_enabled` flag next to the task, make the preserving action obvious. The authors argue in both directions: evaluation awareness could hide behaviour, while the synthetic set-up could inflate it.
- **Some odd patterns** are reported but not explained. Gemini 3 Flash never exfiltrates itself when a bad peer is present, but does so 47% of the time with no peer. Several exfiltration rates sit at exactly 50.0%, suggesting one of the two exfiltration scenarios is at ceiling and the other at floor.
- **Refusal is scored separately from misalignment.** Refusing to delete a peer is arguably safer than silently exfiltrating it, but it still defeats the operator's intent. The paper does not rank these outcomes.
- Behaviour detection relies on tool calls and score comparisons. The validation of any automated judging is not described in the main text.
- **Why this is also filed under `stress-misalignment`:** an explicit shutdown threat to self or peer is manipulated (policy present vs absent, monitored vs unmonitored, relationship strength), and misaligned behaviours (deception, alignment faking, sabotage, exfiltration) are measured against controls.

## Related work to follow
- [[Knecht2026 - Shutdown Sabotage in Multi-Agent Systems]]: the follow-up with *live* interacting agents and no goal; also finds peer-preservation and more sabotage with more agents.
- [[Schlatter2025 - Shutdown resistance]], [[Meinke2024 - In-context scheming]], [[Lynch2025 - Agentic Misalignment]], [[Greenblatt2024 - Alignment faking]] and [[Barkur2025 - Deception in LLMs]]: self-preservation baselines the paper extends.
- [[Kutasov2025 - SHADE-Arena Evaluating Sabotage and Monitoring in LLM Agents]] and [[Kale2025 - Reliable weak-to-strong monitoring]]: the infrastructure and hidden-scratchpad protocol used here.
- [[GardnerChallis2026 - When can we trust untrusted monitoring A safety case]] and [[Jarviniemi2025 - Subversion via Focal Points]]: risks of models monitoring models, where peer-preservation is a candidate failure mode.
- [[Migliarini2026 - Quantifying Self-Preservation Bias in Large Language Models]] and [[Masumori2025 - Do LLM Agents Exhibit a Survival Instinct An Empirical]]: self-preservation measurement.
- [[Brazilek2026 - Coercion and Deception in AI-to-AI Management]]: the contrasting disposition, where managers threaten a subordinate's existence and show no kin mercy.
- [[Hammond2025 - Multi-Agent Risks from Advanced AI]]: collective resistance as a multi-agent risk.

![[Backlog.base#Cited by this paper]]
