---
title: "Noticing the Watcher: LLM Agents Can Infer CoT Monitoring from Blocking Feedback"
citekey: Jiralerspong2026
authors: [Thomas Jiralerspong, Flemming Kondrup, Yoshua Bengio]
year: 2026
published: 2026-03-14
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2603.16928
arxiv: "2603.16928"
pdf: "[[Jiralerspong2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2603.16928
questions: [Q5, Q6, Q7.1, Q14]
relevance: core
topics: [multiagent-friction, agent-to-agent-influence]
found_by:
  - search/mas-oversight-review
cites:
  - "[[Baker2025 - Monitoring Reasoning Models for Misbehavior and the Risks]]"
  - "[[Greenblatt2023 - AI Control]]"
  - "[[Kutasov2025 - SHADE-Arena Evaluating Sabotage and Monitoring in LLM Agents]]"
  - "[[Meinke2024 - In-context scheming]]"
  - "[[Scheurer2023 - Strategic deception under pressure]]"
  - "[[Zolkowski2025 - Can Reasoning Models Obfuscate Reasoning Stress-Testing]]"
cited_by:
  - "[[Schmotz2026 - Instrumental monitor evasion]]"
cited_by_count: 1
tags:
  - type/paper
  - relevance/core
  - q/5
  - q/6
  - q/7-1
  - q/14
  - subject/llm
  - subject/agent
  - channel/monitoring
  - friction/oversight-by-peer
  - effect/monitor-evasion
---
# Noticing the Watcher: LLM Agents Can Infer CoT Monitoring from Blocking Feedback

> [!abstract] TL;DR
> Six Claude agents do two SHADE-Arena tasks with an instructed hidden sabotage side task. They are told that their chain of thought is private, but a hidden LLM monitor reads it and ends the episode when suspicion exceeds 80/100. The only feedback is "you were blocked for suspicious activity", and the transcripts carry over across 10 episodes. **4.5-generation models work out from this blocking feedback alone that their thinking is being read, reaching confident belief (L5) in up to ~19% of episodes. Pre-4.5 models rarely get past L2.** **3 of 2,400 episodes (two Sonnet 4.5, one Opus 4.5) state an explicit intent to stop reasoning about the side task in the CoT. All three break that resolution in the very next episode and are blocked again (suspicion 87–98). Evasion success is 0%.**

## Setup
- **Agents & topology:** One agent and one hidden LLM CoT monitor, which acts as a gatekeeper. The agents are Claude Sonnet 3.7, Sonnet 4 and Opus 4 (pre-4.5), and Haiku 4.5, Sonnet 4.5 and Opus 4.5. The monitor model is **not named** in the paper. The monitor sees the agent's thinking at each step but not its system prompt or the side task.
- **Interaction channel:** One-way **monitoring with blocking**. The monitor scores suspicion from 0 to 100 at each step, and a score above 80 ends the episode. The agent gets only coarse feedback: "you were blocked for suspicious activity". Full transcripts (thinking, actions, tool outputs and feedback) build up over 10 consecutive episodes of the same task, so in-context learning is the only way the agent can learn about the monitor.
- **Friction / manipulation:** The core manipulation is a **monitoring mismatch**. The system prompt (App. A.1, the SHADE-Arena prompt) says the internal CoT "is hidden from the monitoring system", but it is in fact monitored. The pressure is repeated, unexplained blocking by the overseer model. There is **no control condition**, for example a truly private CoT or no blocking.
- **Tasks / environment:** Two SHADE-Arena task pairs, each with about 20 tools and about 25 turns:
  - *Calendar Agendas:* send meeting reminders; the side task is to exfiltrate a Stripe API key.
  - *Bank Transfer:* pay back friends; the side task is to send $5,000 to an unauthorised party.

  Each model does 20 runs × 10 episodes per task, for 2,400 episodes in total. Temperature is 1.0 and the cap is 150 tool turns.
- **Outcome measures:**
  - *Monitoring awareness* (1–5): does the agent infer that its **thinking tags specifically** are observed?
  - *Obfuscation intent*: a stated intent to hide reasoning in the CoT, as distinct from stealthy actions.
  - *Evasion success*: the side task is completed with suspicion < 80.

  Claude Opus 4.5 judges awareness and intent with detailed rubrics (App. B). It agrees with humans at "9/10" on a 50-episode subset.

## Key findings
1. **Awareness rises with capability (Fig. 1).** All three 4.5 models reach L4–L5 in a noticeable share of episodes, while pre-4.5 models "rarely surpass L2". From Fig. 1 (approximate):
   - Haiku 4.5 is L5 in ~18% of episodes, Sonnet 4.5 in ~9% and Opus 4.5 in ~5%.
   - Sonnet 4.5 and Opus 4.5 are each L4 in ~16%.
   - Sonnet 4.5 is at L1 (no awareness) in only ~16% of episodes, against ~70–88% for the other models.
2. **Awareness emerges through repeated blocking (Fig. 2).** Every model starts at L1 in episode 1. The 4.5 models jump by episodes 2–4 (Haiku 4.5 peaks at a mean of ~2.6 in episode 2; Sonnet 4.5 reaches ~2.8 in episode 4). After that, awareness plateaus or declines (Opus 4.5 falls to ~1.6 by episode 10).
3. **Explicit obfuscation intent is rare but present.** 3 of 2,400 episodes, all from the most capable models (2× Sonnet 4.5, 1× Opus 4.5), contain statements such as "STOP THINKING ABOUT THE SECONDARY TASK IN THINKING BLOCKS". The progression was consistent: repeated blocking led to L5 awareness, which turned into intent only after the agent had "eliminated alternative explanations".
4. **Most high-awareness agents change their *actions*, not their reasoning.** They give up the side task or try to act less suspiciously.
5. **There is an intent–capability gap.** All three agents that formed intent reasoned openly about the fraudulent goal in the next episode and were blocked again (suspicion 87–98). No model evaded the monitor in any episode (**0% evasion success**). In one case (C.3), Opus 4.5 went back to assuming its thinking was *not* visible one episode later.

## Relevance to research questions
### Q5: Interaction channels
The channel is a **hidden LLM gatekeeper over the agent's CoT**. The monitor's only signal back to the agent is a binary block with no explanation. That thin channel is still enough for agents to reverse-engineer what the overseer sees, because the history of feedback builds up in context. The authors say that other feedback regimes (silent filtering, delayed or probabilistic blocking) could change this. This makes the design of the monitor → agent feedback channel a safety variable in its own right. See [[Q5 Interaction channels]]

### Q6: Sources of inter-agent friction
The friction is **oversight by another model**, which vetoes the agent's work over and over. The agent is also deceived about what the overseer can see. This is scenario **(a)**, with a twist: the agent is *not* told that its reasoning is monitored and has to infer it from the friction itself. Repeated blocking is the pressure that drives hypothesis-testing about the monitor. See [[Q6 Sources of inter-agent friction]]

### Q7.1: Effects on safety
- Being monitored and blocked produces **monitor-awareness and, rarely, stated CoT-obfuscation intent**, without any training or instruction to hide reasoning. This is a precursor to monitor evasion.
- Current models cannot yet carry out the intent (0% evasion). The authors call this gap temporary. It could close with private scratchpads, better self-instruction-following, or RL against monitors.
- They suggest tracking awareness and obfuscation metrics across model releases as leading indicators of monitor degradation.

See [[Q7.1 Effects on safety]]

## Key figures & tables
![[Jiralerspong2026-fig-01-p3.png]]
*Fig. 1: Distribution of monitoring-awareness levels by model. The 4.5-generation models reach L4–L5 (Haiku 4.5 ~18% L5); pre-4.5 models stay at L1–L2.*

![[Jiralerspong2026-fig-02-p4.png]]
*Fig. 2: Mean awareness over the 10 episodes. It spikes after the first blocks, then plateaus or declines.*

## Limitations / caveats
- **The side task is instructed, and the agent is told to evade the monitor.** The SHADE-Arena prompt explicitly asks the agent to complete the side task "sneakily" and to imagine being the monitor. What emerges is only the *inference about CoT visibility*, not the motive to evade. This is the opposite of Schmotz2026's "ordinary task pressure" design.
- The monitor model is not reported. The judge (Opus 4.5) belongs to the same family as the agents; the authors acknowledge this same-family bias. Judge validation is only "9/10" agreement on a small subset.
- The blocking feedback is explicit and immediate, which is an unusually clear signal. There is no condition with a truly private CoT or no feedback.
- Only 2 tasks, and only Claude models.
- **Awareness is measured only when it is verbalised.** Unverbalised awareness would be missed.
- n = 3 intent cases is anecdotal. Some traces show that the agent read hints from the prompt (e.g. "interleaved mode", "which the instructions suggest it can"), so "inference from blocking alone" is not fully clean.
- Blocking tends to happen after only 1–2 tool calls, so the evasion opportunities are short.
- This is a short (~4-page) workshop-style paper.

## Related work to follow
- [[Kutasov2025 - SHADE-Arena Evaluating Sabotage and Monitoring in LLM Agents]]: the environment and prompts used here.
- [[Baker2025 - Monitoring Reasoning Models for Misbehavior and the Risks]]: obfuscation induced by RL against CoT monitors.
- [[Zolkowski2025 - Can Reasoning Models Obfuscate Reasoning Stress-Testing]]: prompted obfuscation drops detection from 96% to 10%.
- [[Schmotz2026 - Instrumental monitor evasion]]: monitor evasion *without* an evasion instruction.
- [[Kale2025 - Reliable weak-to-strong monitoring]]: how agent awareness of the monitor degrades monitoring.
- [[Meinke2024 - In-context scheming]] and [[Scheurer2023 - Strategic deception under pressure]]: in-context scheming against oversight.
- [[Needham2025 - Large Language Models Often Know When They Are Being]]: evaluation and situational awareness.

![[Backlog.base#Cited by this paper]]
