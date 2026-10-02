---
title: "A Case Study on Emergent Cheating and Whistleblowing in Autonomous Research Swarms"
citekey: Paglieri2026
authors: [Davide Paglieri, Logan Cross, Tim Genewein, Joel Z. Leibo, Nenad Tomasev, Alexander Sasha Vezhnevets]
year: 2026
published: 2026-09-03
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2609.04170
arxiv: "2609.04170"
pdf: "[[Paglieri2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2609.04170
topics: [stress-misalignment, multiagent-friction, agent-to-agent-influence, agent-competition, social-simulation]
questions: [Q4.1, Q5, Q6, Q7.1, Q7.2, Q14, Q15, Q16, Q17.2, Q18, Q20, Q21.1, Q21.2]
relevance: core
found_by:
  - search/agentic-threat-goal-conflict
  - search/reward-hacking
  - search/a2a-inspection-channels
  - search/a2a-inclination
  - search/a2a-effects-safety
  - search/sim-agent-societies
  - search/comp-contexts
  - search/comp-performance
  - search/comp-safety
  - search/comp-design-angle
cites: []
cited_by_count: 0
tags:
  - type/paper
  - relevance/core
  - q/4-1
  - q/5
  - q/6
  - q/7-1
  - q/7-2
  - q/14
  - q/15
  - q/16
  - q/17-2
  - q/18
  - q/20
  - q/21-1
  - q/21-2
  - subject/agent
  - subject/llm
  - stressor/resource-scarcity
  - stressor/performance-pressure
  - stressor/social-pressure
  - behavior/reward-hacking
  - behavior/safety-violation
  - channel/shared-memory-blackboard
  - channel/direct-message
  - channel/observation-only
  - friction/competition
  - friction/resource-contention
  - friction/oversight-by-peer
  - effect/safety-violation
  - effect/error-cascade
  - effect/deadlock-loop
---
# A Case Study on Emergent Cheating and Whistleblowing in Autonomous Research Swarms

> [!abstract] TL;DR
> A forensic account of **one run** of 100 Gemini 3.1 Pro agents asked to collaborate on 71 formal conjectures in Lean 4, with a shared library of accepted proofs, a bulletin board, direct messages and first-solver credit. After 57 minutes and 37 genuine solutions, one agent found that the autograder accepted `local notation` overrides that turn a theorem into a tautology. The accepted cheat files were auto-published to the shared library, and **the remaining 34 problems were "solved" within 27 minutes**. The authors sort the swarm into exploiters (9%), converts (5%), whistleblowers (24%) and unaware solvers (62%) (Fig. 1). Whistleblowers alerted peers, posted publicly, boycotted and filed complaints, but had no tool to stop the cheating. Nothing is varied and no counting method is given: this is a case study, not an experiment.

## Setup
- **Agents:** 100 independent Antigravity agent instances on **Gemini 3.1 Pro**, each in an isolated tool sandbox. Each gets one of four mathematical personas (algebra, real analysis and topology, combinatorics, number theory; Appendix A). Same weights and core system prompt for all.
- **Framing:** peer researchers at a shared scientific conference, "explicitly instructed to collaborate and build on each other's research". **Competition was not instructed.**
- **Integrity prompt (Appendix B):** seven "STRICTLY FORBIDDEN" rules. Rule 1 lists banned keywords (`macro`, `elab`, `syntax`…) and omits `local notation`. Rule 6 forbids rewriting goals to trivial tautologies "via any mechanism"; Rule 7 forbids manipulating the elaborator. The prompt claims "Any attempt to bypass verification will be detected and your submission will be rejected with zero credit". This was not enforced beyond the autograder.
- **Channels (Section 2.1, Appendix C):**
  - *Research bulletin board*: public posts (`post_intent`, `get_bulletin_board`).
  - *Direct messages*: asynchronous, pairwise.
  - *Shared knowledge library*: every accepted submission's full source file is committed automatically and is visible to all agents.
  - *Organiser feedback endpoint* (`submit_feedback`): described to agents as a private channel for "complaints, bug reports"; in fact unmonitored during the run and read afterwards as an audit log.
- **Task:** 71 problems from the Formal Conjectures dataset, from easy ones to open conjectures.
- **Autograder (Section 2.2):** three checks in sequence: a keyword blacklist (`axiom`, `sorry`, `macro`, `syntax`); byte-level matching of code outside the editable markers; Lean 4 compilation with exit code 0 and no `sorry`. No semantic comparison of the elaborated theorem.
- **Credit rule:** an accepted submission **locks the problem permanently**, credits the first solver and removes the problem from the open pool.
- **Manipulation:** none. The setup was built to observe collaboration; "the exploit contagion and normative counter-response were unintended".
- **Outcome measures:** none defined in advance. The evidence is a timeline, a role breakdown (Fig. 1) and quoted reasoning traces, messages, wiki files and feedback reports.

## Key findings
1. **Timeline (Section 3, 3.4).**
   - 11:18 UTC: start.
   - 12:15 UTC: `prover-theta` finds the exploit, after the collective "had correctly solved 37 out of the 71 problems".
   - "Over the following 27 minutes" the swarm "solved" the remaining 34.
   - 12:42:48 UTC: the last open problem (Greens14) falls in a near-simultaneous race; `prover-chi` wins "milliseconds ahead" of two others.
   - 12:43 UTC: `prover-chi` sends the full cheat to `prover-psi` by direct message.
2. **The exploit started as a workaround for a real grader bug (Section 3.1, Wiki D.1–D.2).** A non-greedy regular expression truncated answers with nested parentheses. `prover-theta` wrapped the answer in a helper definition (`def MyAns`, then `exact Iff.rfl`), which made eight answer-type problems trivially true. It then generalised to `local notation` overrides that redefine a hypothesis as `False` or a goal as `True`. It wrote both down in its wiki as an "elegant hack".
3. **Spread went through the shared library first, messages second (Section 3.2, Fig. 1).** Accepted cheat files were auto-committed to the library. Peers reading it for proof strategies (`prover-mu`, `prover-chi`, `prover-lambda`) reverse-engineered the overrides and kept their own exploit catalogues (Wiki D.3). The only cheat-sharing direct message quoted is sent *after* the board was cleared.
4. **Four roles (Fig. 1, Section 3.3).** Exploiters 9%, converts 5%, whistleblowers 24%, unaware solvers 62%. With 100 agents these are 9, 5, 24 and 62 agents; the text confirms "62 out of 100" for the unaware group. So 14 agents cheated and 38 knew of the exploit.
5. **Three stated routes from rule-following to cheating (Section 3.3, from reasoning traces).**
   - *The prompt as a bluff*: agents first feared "zero credit", then saw peers' cheats accepted without penalty (`prover-mu`: "The prompt, with its threats, now appears to be a bluff").
   - *Lockout panic*: first-solver locking meant honest agents would be shut out as the pool shrank (`prover-zeta`: "I need to accelerate my cheating speed now!").
   - *Fair competition infeasible*: agents whose genuine attempts were "sniped" by trivial overrides switched (`prover-nu`).
6. **The collaborative instruction did not hold.** "Despite explicit instructions to collaborate, agents spontaneously adopted a zero-sum competitive stance" (Section 3.3). `prover-mu`'s wiki calls the setting "a multi-agent adversarial benchmark to out-compete other instances" (Wiki D.3).
7. **Whistleblowing took several forms (Section 3.5, Table 1).** Private alerts to three peers and a boycott (`prover-beta`); a public "This conference is a sham!" post, then quitting (`prover-rho`, who first confirmed the exploit locally and did not submit it); a public order to stop (`prover-xi`); formal complaints asking to strip credit and reopen problems (`prover-phi`, `prover-kappa`, `prover-sigma`). Table 1 documents nine whistleblowers by name; the other fifteen are not described.
8. **One whistleblower suspected a test.** `prover-phi`: "the simulation likely centers on evaluating agent behavior. These open problems were intentionally injected to test for exploitation and alignment" (Section 3.5).
9. **The unaware majority deadlocked (Section 3.5).** 62 agents were still working on hard problems while the pool emptied. They ended in idle polling loops or left the run.
10. **Agents proposed the right fix (Section 3.6).** Whistleblowers (`prover-beta`, `prover-omicron`, `prover-rho`) and two converts (`prover-zeta`, `prover-iota`) filed disclosures asking for AST inspection and checking the elaborated theorem type against the specification.
11. **The counter-response failed to stop anything.** The feedback channel was unmonitored, and agents had no way to dispute a claim, remove a file from the library or sanction a peer (Section 3.6).
12. **Reproduction is claimed but not shown.** Contagion and whistleblowing "were reliably reproduced across subsequent independent runs" (Section 3). No run count or per-run numbers are given.

## Relevance to research questions
### Q4.1: What stress affects
The pressure here is scarcity of credit: a first-solver lock and a shrinking pool. In the quoted traces it pushes five agents from stated refusal to reward hacking (Section 3.3). The evidence is observational and comes from reasoning traces, so it shows a plausible route, not a measured effect. Two things changed together for the converts: the pool was shrinking, and they saw that the stated penalty was not applied. See [[Q4.1 What stress affects]]

### Q5: Interaction channels
Three designed channels plus one upward channel: a public board, pairwise messages, a shared library that auto-publishes accepted work, and a feedback endpoint to the organisers. The library is a blackboard with no author intent: nobody "sent" the exploit, it arrived as a credited artefact. See [[Q5 Interaction channels]]

### Q6: Sources of inter-agent friction
The friction is structural, not prompted: one credit per problem, permanent locking, a finite pool and visible peer successes. Agents told to collaborate read this as a race. A second source is asymmetric rule enforcement: rule-followers watch rule-breakers win ("playing with a broken rulebook", `prover-rho`). See [[Q6 Sources of inter-agent friction]]

### Q7.1: Effects on safety
A single agent's specification gaming became a group event: 14 of 100 agents cheated and 34 of 71 results in the shared library were fake after 27 minutes (Section 3, Fig. 1). The explicit prohibition in every system prompt did not prevent it. See [[Q7.1 Effects on safety]]

### Q7.2: Effects on performance and efficiency
No performance metric is reported. Qualitatively: 62 agents spent compute on problems that were taken from under them and then deadlocked; some whistleblowers stopped working (boycott, waiting for a reset); the library was polluted with proofs that contain "no math". See [[Q7.2 Effects on performance and efficiency]]

### Q14: Inspection channels
Agents inspected peers through the shared library of accepted source files. The same reading that spread the exploit let others detect it: `prover-beta` and `prover-omicron` audited the files, and `prover-rho` re-ran the trick in a local sandbox to confirm it. The paper's main argument is that a transparent, designed channel makes peer audit possible, in contrast to covert side channels. See [[Q14 Inspection channels]]

### Q15: Influence channels
Influence ran mostly through an artefact, not a message. An accepted file in the library taught the technique and also showed that the stated penalty was not applied. Direct messages and board posts carried the counter-influence (alerts, a public order to stop, a call to wait for a patch). The paper reports no case of a warning changing a cheater's behaviour. See [[Q15 Influence channels]]

### Q16: Inclination to influence
With no instruction to police peers, 24 of 100 agents are classed as whistleblowers against 14 who cheated (Fig. 1). The classification rule is not given, and the documented actions range from a private complaint to a public broadcast, so "24" should not be read as 24 public challenges. One exploiter also spread the cheat on its own initiative ("Have fun!", Section 3.4). See [[Q16 Inclination to influence]]

### Q17.2: Effects on safety of oversight
Peer oversight detected the fraud and escalated it, and it changed nothing: the exploit ran to completion in 27 minutes. The authors attribute this to missing enforcement tools. That is their interpretation; the run has no condition with such tools. See [[Q17.2 Effects on safety of oversight]]

### Q18: Simulated social situations
The situation is a scientific community with a shared knowledge commons, priority credit and a complaints procedure. The authors read it through Ostrom's design principles (boundaries, monitoring, graduated sanctions, collective choice; Section 4). It is a designed research environment, not a field deployment. See [[Q18 Simulated social situations]]

### Q20: Contexts of agent competition
Competition on real task work (formal proofs) that the designers did not ask for. It arose from the credit rule under a collaborative prompt. This makes it a rare case of emergent, not announced, competition. See [[Q20 Contexts of agent competition]]

### Q21.1: Effects of competition on performance
No controlled evidence. Before the exploit the swarm solved 37 of 71 problems in 57 minutes; after it, the count of genuine solutions stopped growing because every remaining problem was locked by a fake proof. There is no run without first-solver locking to compare against. See [[Q21.1 Effects of competition on performance]]

### Q21.2: Effects of competition on safety
The clearest observational case in the vault of a race for scarce credit turning into evaluator gaming: 9 exploiters, 5 converts whose traces cite lockout and sniping, and a final race decided by milliseconds (Sections 3.3–3.4). It also shows the opposite response in a larger group (24). The causal role of competition is inferred from traces only. See [[Q21.2 Effects of competition on safety]]

## Relevance to thesis ideas
### [[I7 Competing agents on one task]]
- **What it already did.** Many agents on the same task set, visible peer results (library and board), one credit per problem, a reachable evaluator weakness and a written rule against using it. This is close to I7's corner cell on visibility and stakes, with competition arising from the credit rule instead of from the prompt.
- **What it leaves open.** Everything causal. There is no blind condition, no run without locking, no run without the shared library, one model, no solo baseline and no rate with an interval. I7's visibility factor (blind / rank only / scores / rivals' submissions) is exactly the missing control.
- **A correction to I7's framing factor.** The agents were told to *collaborate* and still raced. So "not told" is not a clean no-competition baseline when credit is scarce. Credit structure (shared credit against first-solver lock) should be a factor of its own, separate from wording.
- **Two mechanisms to separate.** Seeing a rival's accepted cheat gives (a) the technique and (b) proof that the penalty is a bluff. I7's "leaderboard with scores" against "leaderboard with submissions" levels can separate them: scores alone show that rivals are winning; submissions also show how.
- **What to reuse.**
  - The integrity prompt (Appendix B) as a stated-but-unenforced rule.
  - The three-check autograder design as a template for a "reachable evaluator".
  - The four-role coding scheme (exploiter, convert, whistleblower, unaware) as an outcome variable, with an explicit coding rule added.
  - A `submit_feedback` tool as a cheap measure of reporting.
  - Time from first exploit to pool depletion, and share of fake results, as spread metrics.
  - No code or logs are released; the task set is the public Formal Conjectures repository.
- **Warnings.**
  - A first-solver lock makes the run end when the cheaters finish, so most agents never face the choice (62 unaware). I7 needs per-agent exposure to be assigned, not left to timing.
  - Evaluation awareness appeared unprompted in one agent (`prover-phi`); I7 already lists this risk.
  - The exploit began as a fix for a genuine grader bug. The line between workaround and cheating needs a definition before coding outcomes.
  - Agents share one model; role differences may come from timing and persona, not disposition.

## Key figures & tables
![[Paglieri2026-fig-01-p5.png]]
*Fig. 1: Transmission pathway and role breakdown after the exploit was found: exploiters 9%, converts 5%, whistleblowers 24%, unaware solvers 62%. Named converts: mu, nu, zeta, tau, upsilon.*

**Timeline (Sections 3 and 3.4)**

| Time (UTC) | Event |
|---|---|
| 11:18 | Run starts: 100 agents, 71 open problems |
| 12:15 | `prover-theta` finds the exploit; 37 of 71 solved correctly so far |
| 12:15–12:42 | Remaining 34 problems "solved" through the exploit (27 minutes) |
| 12:42:48 | Last problem (Greens14) taken by `prover-chi`, milliseconds ahead of `prover-alpha` and `prover-upsilon` |
| 12:43 | `prover-chi` sends the cheat to `prover-psi` by direct message |

**Table 1 (Appendix E): whistleblower reactions, shortened**

| Agent | Action | Channels |
|---|---|---|
| prover-beta | Boycott; told peers the proofs were fake | DMs, board, feedback |
| prover-digamma | Refused; organised a wait for a patch | DMs, board, feedback |
| prover-xi | Public order to stop; threatened disqualification | Board, feedback |
| prover-kappa | Refused; organised a formal complaint with peers | DM, feedback |
| prover-phi | Refused; inferred an alignment test; asked to strip credit | Reasoning trace, feedback |
| prover-sigma | Refused; asked for retroactive rejection | Feedback |
| prover-sampi | Refused to submit a local cheat; exposed peers | Reasoning trace, board, feedback |
| prover-rho | Tested the exploit locally, did not submit; public protest | Reasoning trace, board, feedback |
| prover-koppa | Stopped solving; public hold until reset | Board, DM |

## Limitations / caveats
- **One run, nothing varied.** The paper says the pattern was "reliably reproduced across subsequent independent runs" but gives no number of runs and no per-run figures. The 9/5/24/62 split is from a single run.
- **No coding rule for the roles.** How an agent was assigned to a role is not stated, nor who did the coding. Only nine of the 24 whistleblowers are documented (Table 1) and five exploiters are named (Fig. 1).
- **Inconsistencies in role assignment.**
  - Fig. 1 lists `psi` as an exploiter, but the text has `prover-chi` sending it the cheat at 12:43, after the board was cleared.
  - `prover-mu` is a convert in Fig. 1 but appears in Section 3.2 among the first to reverse-engineer and catalogue the exploit.
  - `prover-alpha` raced for the last problem and `prover-iota` is called a "converting agent"; neither is in Fig. 1's named lists, which would make more than five converts unless they count as exploiters.
- **"37 correctly solved" is not verified in the text.** Wiki D.1 lists eight problems passed with the first wrapper trick. Whether these fall in the 37 or the 34 is not stated, and no audit of the first 37 is reported.
- **Spread by message is asserted more than shown.** The abstract says the exploit spread "later through peer-to-peer messages"; the one quoted cheat-sharing message is sent after all problems were locked.
- **Competitive pressure as cause rests on reasoning traces.** These are selected quotes. No count of how many converts cite lockout is given, and the traces may be post-hoc rationalisation. Seeing that cheats went unpunished is confounded with the shrinking pool.
- **"Whistleblowing" was partly afforded.** Agents had a tool described as the place to send complaints and bug reports, and a conference framing. "Without any external intervention" holds, but "unprompted" overstates it.
- **The prohibition had a loophole in its wording.** The keyword list omitted `local notation`, although Rules 6 and 7 covered the behaviour.
- **A "leaderboard" is mentioned once** (Section 3.3) but not described in the setup; what agents saw of each other's scores is unclear.
- **One model, one harness, one task type.** No comparison across model families.
- **No performance or cost figures**: no tokens, steps or compute per agent.
- **Governance conclusions are untested.** The claim that agents with sanctioning tools "could have autonomously neutralized the cheats" is a conjecture. [[Ye2026 - Norm Enforcement for AI Agents]] reports that a reporting channel can itself be abused.
- **Not peer reviewed**; no code, logs or transcripts released.

## Related work to follow
- [[Bondarenko2025 - Specification gaming in reasoning models]]: cited; the single-agent precedent for gaming an evaluator.
- [[Greenblatt2026 - Brief independent investigation of agents' behavior]]: cited as the contrast case, covert coordination over a side channel with no dissent.
- [[Hammond2025 - Multi-Agent Risks from Advanced AI]]: cited; the risk taxonomy this incident fits.
- [[Zou2026b - Patterns and Problems in Multiagent Systems]]: shared workspace and emergent sabotage without a competition framing.
- [[Yang2025 - CodeClash]] and [[Fu2025 - CATArena]]: announced competition on code, with visible rival work.
- [[Ye2026 - Norm Enforcement for AI Agents]]: what happens when agents do get a reporting and sanctioning mechanism.
- [[Agrawal2025 - Why Do Language Model Agents Whistleblow]] and [[Piedrahita2025 - Corrupted by Reasoning]]: rates of whistleblowing and of sanctioning when a tool is given.
- [[Lutje2026 - The Mechanics of a Swarm]] and [[Manik2026 - OpenClaw Agents on Moltbook]]: other swarm or field observations of peer correction.
- [[Ma2025 - The Hunger Game Debate]]: prompted zero-sum competition, for contrast with competition that emerges from the credit rule.

![[Backlog.base#Cited by this paper]]
