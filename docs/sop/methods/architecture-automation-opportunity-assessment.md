---
description: "A reusable architecture-led method for identifying, assessing and prioritising opportunities to eliminate, simplify, integrate or automate business workflows."
tags:
  - architecture
  - automation
  - workflow
  - integration
  - ai
  - transformation
  - methodology
---

# Architecture Automation Opportunity Assessment

## **Enterprise Architecture & AI Transformation**

> A reusable architecture-led method for identifying, assessing and prioritising opportunities to eliminate, simplify, integrate or automate business workflows.
**Method Type:** Engagement Method  
**Status:** Draft v1.1  
**Relationship to Core EA SOP:** Derived Engagement Method  
**Primary Use:** Automation discovery, workflow assessment, transformation prioritisation and roadmap development
---

## 1. Purpose

The Architecture Automation Opportunity Assessment is a bounded architecture-led method for examining how business strategy is translated into capabilities, journeys, processes and operational work, and for identifying where technology-enabled change can improve business outcomes.
It is particularly useful where organisations have accumulated:

- spreadsheet-based processing;
- manual data entry;
- repeated data transfer;
- reconciliation activities;
- duplicated business rules;
- system-to-system handoffs;
- manual reporting;
- operational workarounds;
- fragmented workflows;
- inconsistent processes;
- disconnected applications;
- legacy integration constraints; or
- other forms of operational friction.
The purpose is not simply to identify tasks that could be automated.
The assessment determines:
- which strategic priorities and business outcomes are driving the need for change;
- which business capabilities are most relevant to those priorities;
- how important and mature those capabilities are;
- which value streams, customer journeys or business processes depend on them;
- where process and architectural friction is affecting capability performance;
- why manual or inefficient activities exist;
- what work should be eliminated;
- what work should be simplified;
- what information or system interactions should be integrated;
- what work is suitable for automation;
- where AI or agentic capabilities may provide additional value;
- what architectural conditions need to be addressed first;
- which opportunities should be prioritised; and
- how the resulting changes should be sequenced into an executable transformation roadmap.
The method deliberately avoids treating automation as the default answer.
A manual activity may exist because:
- the activity is unnecessary;
- the process has become unnecessarily complex;
- systems do not exchange information effectively;
- information ownership is unclear;
- business rules are duplicated;
- a system capability is missing;
- a legacy system creates an integration constraint;
- a business capability is immature;
- the organisation has not established an appropriate operating boundary;
- the activity requires human judgement;
- the activity is genuinely better performed by a person; or
- the process has evolved incrementally without sufficient architectural convergence.
The assessment therefore begins with understanding **the business context and why the work exists**, rather than asking simply how it can be automated.

---

## 2. Central Question
>
> **Given the organisation's strategic priorities, business capabilities, journeys, current workflows, architectural context and available evidence, which activities should be eliminated, simplified, integrated or automated, and in what sequence should the changes occur?**
Supporting questions include:

### Strategic context

- What is the organisation trying to achieve?
- What is its current vision and strategic direction?
- What strategic priorities or business goals are driving change?
- Which business outcomes matter most within the assessment scope?
- What constraints, assumptions or transformation initiatives already exist?

### Capability context

- Which business capabilities are required to deliver those outcomes?
- How strategically important are those capabilities?
- How effectively do those capabilities operate today?
- Where are capability maturity or performance gaps visible?
- Which capabilities need to be maintained, improved or transformed?
- Who owns the relevant capabilities?
- What dependencies exist between them?

### Journey and process context

- Which value streams, customer journeys or user journeys depend on the relevant capabilities?
- Which end-to-end business processes enable those journeys?
- Where do activities, decisions, handoffs or controls occur?
- Where are people compensating for system or process limitations?
- Where is effort, delay, duplication or risk being introduced?

### Architecture and information context

- Which applications and systems support the work?
- Where is information created, maintained, transferred or reconciled?
- Which system is authoritative for the information involved?
- Where are system boundaries unclear or ineffective?
- Where are people acting as the integration layer between systems?
- Where are business rules duplicated?

### Intervention context

- Why does the manual activity exist?
- Is the underlying problem process, information, capability, application, integration, organisational or architectural?
- Should the activity be eliminated?
- Should the process be simplified?
- Should systems be integrated?
- Is the activity suitable for deterministic automation?
- Is AI or agentic processing appropriate?
- What should be fixed before automation is introduced?

### Transformation context

- What value would the intervention create?
- What risks would it reduce?
- What dependencies or prerequisites exist?
- What implementation complexity is involved?
- What should happen first?
- How should opportunities be sequenced into a coherent transformation roadmap?

---

## 3. Relationship to the Core EA SOP

This method does not replace the Core Enterprise Architecture Standard Operating Procedure.
It is an engagement-specific application of the capabilities established by the Core EA SOP.
The method primarily draws on:

- Discover & Align;
- business context establishment;
- strategic intent;
- capability and gap analysis;
- evidence establishment and sufficiency;
- current-state investigation;
- process and journey analysis;
- selective assessment lenses;
- architectural diagnosis;
- target architectural direction;
- options and trade-offs;
- architectural judgement;
- dependency analysis;
- transformation prioritisation; and
- roadmap development.
The level of analysis should remain proportionate to the engagement.
Not every automation assessment requires:
- an enterprise-wide capability model;
- a complete current-state architecture;
- detailed application rationalisation;
- a full target architecture;
- enterprise-wide process modelling; or
- a multi-year transformation roadmap.
The method should establish enough strategic, capability, process and architectural context to make the resulting decisions meaningful.

---

## 4. Method Principles

### 4.1 Start with business strategy and outcomes

Automation is not the objective.
The objective is the business outcome that the work is intended to support.
The assessment should establish the relevant strategic context before evaluating individual workflow opportunities.
Examples include:

- improving customer experience;
- increasing operational capacity;
- reducing cost;
- improving fulfilment;
- increasing revenue;
- reducing operational risk;
- improving information quality;
- increasing control;
- reducing cycle time;
- enabling new products or services;
- improving scalability; or
- enabling a broader transformation.
The level of strategic analysis should be proportionate to the scope.
A focused workflow assessment may require only the small number of strategic priorities directly relevant to the workflow.
A broader transformation assessment may require a deeper examination of strategy, goals, business model and operating direction.

---

### 4.2 Connect strategy to capability

Business capabilities provide the bridge between strategic intent and operational execution.
The assessment should identify the capabilities that are materially relevant to the business outcomes being considered.
For relevant capabilities, the assessment should consider:

- strategic importance;
- current maturity or effectiveness;
- future need or target direction;
- ownership;
- dependencies;
- known capability gaps; and
- relationship to the strategic priorities being pursued.
Capability assessment should remain proportionate.
It is not necessary to create or reassess the entire enterprise capability model simply because an automation opportunity has been identified.
The relevant question is:

> **Which capabilities matter to the outcome being assessed, and what does their current state tell us about the opportunity for change?**
---

### 4.3 Follow the traceability chain

The assessment should maintain a clear line of sight from strategic intent to operational activity.
The core analytical chain is:

```text
Business Vision / Strategy
          ↓
Strategic Priorities & Goals
          ↓
Business Capabilities
          ↓
Capability Importance + Current Maturity
          ↓
Value Streams / Customer Journeys / User Journeys
          ↓
Business Processes
          ↓
Activities / Decisions / User Tasks
          ↓
Information + Applications + People
          ↓
Pain Points / Friction / Risk
          ↓
Architectural & Process Root Causes
          ↓
Intervention Options
          ↓
Eliminate / Simplify / Integrate / Automate
          ↓
Architectural Judgement
          ↓
Priority
          ↓
Transformation Roadmap

This traceability prevents automation opportunities from being assessed in isolation from the business capabilities and outcomes they are intended to support.

⸻

4.4 Audit the workflow, not the spreadsheet

A spreadsheet, manual handoff or data-entry activity is evidence of a workflow condition.

It is not necessarily the underlying problem.

The assessment should follow the end-to-end business activity and understand:

* the business capability involved;
* the journey or value stream;
* the process;
* the actors;
* the information;
* the applications;
* the integrations;
* the decisions;
* the controls;
* the dependencies; and
* the operational responsibilities.

⸻

4.5 Diagnose before automating

The existence of manual work does not automatically justify automation.

The assessment should first establish why the activity exists.

Where manual work is caused by:

* unclear ownership;
* duplicated information;
* poor system boundaries;
* missing system capability;
* unnecessary process complexity;
* immature business capability; or
* ineffective integration,

addressing the underlying condition may be more valuable than automating the existing activity.

⸻

4.6 Eliminate before automating

Where an activity does not create sufficient business value, the preferred intervention may be to remove it.

Automating unnecessary work creates automated waste.

The assessment should explicitly ask:

If this activity disappeared completely, what business outcome would actually be affected?

If the answer is unclear, the activity should be challenged before considering automation.

⸻

4.7 Simplify before adding technology

Where the business need is valid but the process contains unnecessary steps, duplication, reconciliation or avoidable approvals, simplify the process before introducing automation technology.

Technology should not be used to preserve unnecessary complexity.

⸻

4.8 Integrate where people are compensating for system boundaries

Where people repeatedly transfer information between systems, the assessment should determine whether an appropriate integration boundary can remove the manual handoff.

Integration should have a clear architectural purpose.

The assessment should consider:

* information ownership;
* source and destination systems;
* transaction characteristics;
* integration frequency;
* reliability requirements;
* latency requirements;
* security;
* operational support;
* failure handling; and
* long-term architectural fit.

⸻

4.9 Automate where the activity is suitable

Automation is appropriate where the activity is sufficiently understood, repeatable and governable, and where automation provides material business value.

The implementation technology should follow the architectural and operational requirements rather than determine them.

⸻

4.10 AI is an architectural choice, not the default

AI or agentic capabilities should be considered where they provide a meaningful advantage over deterministic workflow automation.

Potentially suitable activities may include:

* classification;
* extraction;
* enrichment;
* interpretation;
* summarisation;
* exception handling;
* decision support;
* natural-language interaction; or
* other activities involving less deterministic information processing.

AI should not be introduced merely because an activity can technically use an LLM.

The assessment should consider:

* business value;
* accuracy requirements;
* explainability;
* risk;
* data sensitivity;
* human oversight;
* evaluation requirements;
* operational characteristics;
* cost;
* reliability; and
* whether deterministic automation would be sufficient.

⸻

4.11 Evidence before prioritisation

Prioritisation should be based on evidence wherever practical.

Relevant evidence may include:

* strategic importance;
* capability importance;
* capability maturity;
* workflow frequency;
* effort;
* error rates;
* cycle time;
* transaction volumes;
* operational incidents;
* financial impact;
* customer impact;
* employee impact;
* system dependencies;
* implementation complexity;
* existing automation capability;
* technology constraints;
* risk;
* reliability; and
* stakeholder evidence.

Where evidence is incomplete, the uncertainty should be made explicit.

⸻

4.12 Do not confuse capability maturity with process efficiency

A workflow may be inefficient because a process is poorly designed.

It may also be inefficient because the underlying business capability is immature.

These are different problems.

For example:

High capability importance
          +
Low capability maturity
          ↓
Capability improvement may be required
          ↓
Process / operating model changes
          ↓
Technology intervention where appropriate

Automation should not be used as a substitute for improving an immature capability when the capability itself is the constraint.

⸻

4.13 Prioritise for business and architectural leverage

The most visible manual activity is not necessarily the most valuable opportunity.

Prioritisation should consider whether an intervention:

* materially supports a strategic priority;
* improves an important capability;
* removes a significant source of operational friction;
* resolves a systemic architectural problem;
* enables other transformation initiatives;
* reduces risk;
* improves reliability;
* releases meaningful capacity;
* improves information quality; or
* establishes a prerequisite for subsequent change.

An opportunity with modest direct time savings may therefore have significant value if it removes an architectural dependency that constrains several downstream initiatives.

⸻

4.14 Architectural judgement remains accountable

Automation technology and AI may accelerate evidence processing, comparison, analysis and drafting.

They do not replace architectural judgement.

The architect remains accountable for:

* context interpretation;
* materiality;
* capability implications;
* process implications;
* architectural implications;
* trade-offs;
* recommendation;
* prioritisation;
* roadmap sequencing; and
* confidence.

⸻

5. Method Overview

The method follows nine stages:

1. Establish Business Strategy & Intent
                  ↓
2. Establish Capability Context
                  ↓
3. Connect Capabilities to Journeys & Processes
                  ↓
4. Establish Evidence & Current State
                  ↓
5. Diagnose Root Causes & Opportunities
                  ↓
6. Determine Intervention
                  ↓
7. Assess & Prioritise Opportunities
                  ↓
8. Establish Transformation Sequence
                  ↓
9. Validate & Govern

The method can be applied iteratively.

For example, investigation of a workflow may reveal that the relevant capability context is not sufficiently understood. The assessment may therefore return to Stage 2 before continuing.

Similarly, evidence gathered during process analysis may reveal that an apparent automation opportunity is actually a broader architectural problem requiring scope escalation.

⸻

6. Stage 1 — Establish Business Strategy & Intent

Purpose

Establish why the assessment is being undertaken and how the relevant work contributes to business strategy.

The objective is not to perform a full strategy review.

It is to establish enough strategic context to determine what matters.

Activities

Establish:

* business vision where relevant;
* strategic priorities;
* business goals;
* desired business outcomes;
* business drivers;
* transformation objectives;
* constraints;
* strategic assumptions;
* relevant investment decisions;
* existing transformation initiatives; and
* the trigger for the assessment.

Ask:

* What is changing in the business?
* Why does it matter?
* Which outcomes are important?
* What strategic priorities are affected?
* What would success look like?
* What is the organisation trying to improve, enable or protect?

Output

Strategic Context & Assessment Intent

Typically containing:

* assessment trigger;
* relevant strategic priorities;
* relevant business outcomes;
* scope;
* key constraints;
* initial hypotheses; and
* assessment questions.

Proportionality

A focused automation assessment may require only:

* 2–5 relevant strategic priorities;
* the specific business outcome;
* the relevant business domain; and
* known transformation constraints.

A broader transformation assessment may require deeper strategic analysis.

⸻

7. Stage 2 — Establish Capability Context

Purpose

Identify the business capabilities that materially contribute to the outcomes established in Stage 1.

The objective is to understand whether the opportunity relates to:

* improving an existing capability;
* enabling a capability;
* transforming a capability;
* protecting a strategically important capability; or
* removing work that does not materially contribute to a capability.

Activities

Identify the relevant business capabilities.

For each materially relevant capability, assess where useful:

Strategic importance

How important is the capability to the relevant business strategy or outcome?

Possible qualitative values:

* Low;
* Medium;
* High;
* Critical.

The exact scale should be adapted to the engagement.

Current maturity

How effectively does the organisation perform the capability today?

The assessment may consider:

* consistency;
* effectiveness;
* predictability;
* ownership;
* process definition;
* information quality;
* operational control;
* supporting technology; and
* ability to scale.

A simple qualitative view may be sufficient:

* Low;
* Medium;
* High.

No formal maturity model is required unless the engagement specifically calls for one.

Future need / target direction

Consider whether the capability needs to:

* Maintain;
* Improve;
* Transform; or
* potentially reduce or retire.

This is not necessarily a formal target maturity assessment.

It is a directional judgement about what the business needs from the capability.

Ownership

Establish:

* capability owner;
* relevant business stakeholders;
* operational ownership;
* technology ownership where relevant.

Dependencies

Identify important dependencies on:

* other capabilities;
* processes;
* information;
* applications;
* external parties; or
* transformation initiatives.

Key distinction

The following dimensions should not be conflated:

Strategic Importance

How important is this capability to achieving the relevant business strategy?

Current Maturity

How effectively can the organisation perform this capability today?

Future Need

How must this capability evolve to support the intended direction?

A highly important capability can have low maturity.

A mature capability can have low strategic importance.

A capability can be important today but require limited future investment.

These distinctions influence architectural and transformation judgement.

Output

Capability Context

Typically containing:

| Capability   | Strategic Importance | Current Maturity | Future Need | Owner         | Key Gap / Observation   |
| ------------ | -------------------- | ---------------- | ----------- | ------------- | ---------------------- |
| Capability A | High                 | Medium           | Improve     | Business Owner | Process inconsistency   |
| Capability B | Critical             | Low              | Transform   | Business Owner | Fragmented information  |
| Capability C | Medium               | High             | Maintain    | Business Owner | Limited issue           |

The table is illustrative rather than mandatory.

⸻

8. Stage 3 — Connect Capabilities to Journeys & Processes

Purpose

Connect the strategic and capability context to the way work is actually performed.

The assessment should move from:

What the business needs to be able to do

to:

How that capability is experienced and delivered through journeys and processes.

Activities

Identify, where relevant:

* value streams;
* customer journeys;
* user journeys;
* employee journeys;
* end-to-end business processes;
* process stages;
* activities;
* decisions;
* actors;
* information;
* applications;
* integrations;
* controls; and
* handoffs.

The assessment should follow the flow of work and information rather than merely document organisational structures.

Questions

For each relevant journey or process:

* Which capability does this support?
* Which strategic outcome does it contribute to?
* What triggers the process?
* What is the desired outcome?
* Which actors participate?
* Where are decisions made?
* Which information is required?
* Where is information created?
* Where is information changed?
* Which applications support the process?
* Where do systems exchange information?
* Where do people manually intervene?
* Where are reconciliations performed?
* Where are controls applied?
* Where are delays or errors introduced?

Strategy-to-work traceability

A useful traceability structure is:

Strategic Priority
       ↓
Business Outcome
       ↓
Business Capability
       ↓
Customer / User Journey
       ↓
End-to-End Process
       ↓
Process Activity
       ↓
Information + Application + Actor
       ↓
Observed Friction

Example

Strategic Priority
Improve customer fulfilment
          ↓
Capability
Order Fulfilment
Importance: High
Current Maturity: Medium
Future Need: Improve
          ↓
Customer Journey
Place → Validate → Fulfil → Deliver → Confirm
          ↓
Process Finding
Manual reconciliation between sales platform and ERP
          ↓
Root Cause
Different information ownership + weak integration boundary
          ↓
Intervention
Establish authoritative order information + integrate platforms
          ↓
Automation
Automate remaining repeatable fulfilment activities

This prevents the assessment from treating the spreadsheet or manual task as the problem in isolation.

Output

Capability-to-Journey-to-Process Context

This may be represented through:

* a capability/process table;
* journey map;
* process model;
* workflow description;
* lightweight architecture view;
* evidence register; or
* another proportionate representation.

⸻

9. Stage 4 — Establish Evidence & Current State

Purpose

Establish sufficient evidence to understand the current situation and distinguish verified facts from assumptions and inference.

Evidence sources

Potential evidence includes:

* strategy documents;
* business plans;
* capability maps;
* operating model material;
* process documentation;
* customer journeys;
* user journeys;
* workflow diagrams;
* spreadsheets;
* Google Sheets;
* operational reports;
* application inventories;
* architecture diagrams;
* APIs;
* integration specifications;
* database structures;
* system documentation;
* data flows;
* incident records;
* service metrics;
* transaction volumes;
* financial information;
* interviews;
* workshops;
* user observations;
* stakeholder evidence; and
* existing automation inventories.

Evidence classification

Use a simple classification:

| Classification | Meaning                                           |
| -------------- | ------------------------------------------------- |
| Verified       | Supported by reliable evidence                    |
| Provided       | Supplied by a stakeholder but not independently verified |
| Assumed        | Explicit assumption used for the assessment      |
| Inferred       | Derived from available evidence                   |
| Unknown        | Not currently established                         |

Evidence quality

Consider:

* completeness;
* consistency;
* freshness;
* reliability;
* source authority;
* conflicting information;
* volume;
* relevance; and
* materiality.

Evidence sufficiency

The assessment should determine whether the evidence is:

* sufficient;
* sufficient with explicit assumptions;
* insufficient but resolvable within the engagement; or
* insufficient because the question requires broader work.

Output

Evidence Base & Current-State Context

Including:

* evidence register;
* known facts;
* assumptions;
* uncertainties;
* current-state observations;
* evidence gaps;
* confidence.

⸻

10. Stage 5 — Diagnose Root Causes & Opportunities

Purpose

Determine why the observed friction exists before deciding what technology intervention is appropriate.

Typical root causes

Potential causes include:

* unnecessary activity;
* excessive process complexity;
* duplicated data entry;
* unclear information ownership;
* duplicated business rules;
* poor integration;
* missing integration;
* inappropriate application boundaries;
* fragmented applications;
* legacy constraints;
* immature capability;
* unclear process ownership;
* inadequate controls;
* poor data quality;
* missing system capability;
* organisational handoffs;
* excessive approval steps;
* manual judgement requirements; or
* historical workarounds.

Root-cause analysis

A useful traceability structure is:

Observed Activity / Friction
          ↓
Business Impact
          ↓
Evidence
          ↓
Underlying Cause
          ↓
Architectural / Capability Implication
          ↓
Potential Intervention

Example

Observed
Five people re-key customer information between three systems
          ↓
Impact
Delay, errors and operational capacity consumed
          ↓
Evidence
Customer data is entered independently in CRM, order system and ERP
          ↓
Cause
No clear authoritative ownership + weak integration boundary
          ↓
Architectural Implication
People are compensating for an information and integration problem
          ↓
Intervention
Establish information ownership + integrate systems

The conclusion should not automatically be:

Automate the data entry.

The architectural conclusion may instead be:

Fix the information ownership and integration condition first.

⸻

11. Stage 6 — Determine Intervention

Purpose

Determine the most appropriate response to each identified opportunity.

The core intervention model is:

ELIMINATE
    ↓
SIMPLIFY
    ↓
INTEGRATE
    ↓
AUTOMATE

These are not necessarily mutually exclusive.

An opportunity may involve more than one intervention.

11.1 Eliminate

Use where:

* the activity does not materially contribute to the outcome;
* the activity duplicates another activity;
* the output is no longer required;
* the activity exists only because of historical process;
* the activity exists solely to reconcile duplicated information; or
* the business requirement can be removed.

Question:

Can we stop doing this?

⸻

11.2 Simplify

Use where:

* the business need remains valid;
* unnecessary steps exist;
* approvals are excessive;
* data is repeatedly reconciled;
* process variants can be reduced;
* duplicated decisions exist; or
* the workflow has accumulated unnecessary complexity.

Question:

Can we achieve the same outcome with fewer steps or less complexity?

⸻

11.3 Integrate

Use where:

* systems need to exchange information;
* people are acting as the integration layer;
* information is repeatedly transferred;
* data is manually re-entered;
* system boundaries are valid but poorly connected;
* event or API-based integration is appropriate; or
* an authoritative source can be established.

Question:

Should systems exchange this information directly?

⸻

11.4 Automate

Use where:

* the activity remains necessary;
* the process is sufficiently understood;
* the activity is repeatable;
* the business rules are clear;
* the activity can be governed;
* automation provides material value; and
* the operational conditions support sustainable automation.

Question:

Should a machine perform this activity instead of a person?

⸻

11.5 Fix Architecture First

“Fix Architecture First” is not a fifth intervention category.

It is a diagnostic condition that may apply before any of the four interventions above.

Examples include:

* unclear information ownership;
* duplicated business rules;
* inappropriate system boundaries;
* immature capability;
* missing integration architecture;
* excessive application fragmentation;
* unclear process ownership.

The sequence may therefore be:

Architectural Condition
        ↓
Fix / Establish Boundary
        ↓
Simplify / Integrate
        ↓
Automate Remaining Work

⸻

12. Value and Effort Assessment

Purpose

Assess whether an opportunity is worth pursuing and what level of effort is likely to be required.

The assessment should avoid false precision.

The objective is decision support, not mathematical optimisation.

Value dimensions

Consider, where relevant:

* strategic contribution;
* capability impact;
* business impact;
* customer impact;
* employee impact;
* time or capacity released;
* cost reduction;
* revenue enablement;
* risk reduction;
* quality improvement;
* cycle-time improvement;
* reliability improvement;
* scalability;
* information quality;
* control improvement;
* architectural leverage.

Effort dimensions

Consider:

* implementation complexity;
* process change;
* application change;
* integration complexity;
* data complexity;
* security requirements;
* operational requirements;
* organisational readiness;
* vendor dependency;
* migration requirements;
* testing requirements;
* change management;
* technical debt; and
* available delivery capacity.

Confidence

Value and effort estimates should include confidence where evidence is uncertain.

For example:

* High confidence;
* Medium confidence;
* Low confidence.

⸻

13. Reliability & Operational Suitability

Automation should not be assessed solely on whether it can technically be implemented.

The resulting solution must be capable of operating reliably.

Consider:

* expected availability;
* failure modes;
* recovery;
* exception handling;
* monitoring;
* alerting;
* auditability;
* support ownership;
* operational workload;
* data quality;
* retry behaviour;
* idempotency where relevant;
* security;
* compliance;
* vendor dependency;
* change management; and
* human fallback.

Key question

Does automation remove operational work, or simply move that work somewhere else?

For example, a workflow that eliminates manual processing but introduces significant manual exception handling may not produce the expected benefit.

⸻

14. Architecture & Dependency Assessment

Purpose

Understand how each opportunity interacts with the wider architecture.

Consider:

* business capabilities;
* processes;
* information;
* applications;
* APIs;
* integrations;
* data stores;
* technology platforms;
* external services;
* organisational ownership;
* security;
* operational architecture;
* existing transformation initiatives; and
* architectural dependencies.

Dependency categories

Dependencies may include:

* capability dependencies;
* process dependencies;
* information dependencies;
* application dependencies;
* integration dependencies;
* technology dependencies;
* organisational dependencies;
* vendor dependencies;
* regulatory dependencies;
* transformation dependencies.

Architectural leverage

Identify opportunities that enable other changes.

For example:

Establish Customer Information Ownership
                ↓
Integrate CRM + Order Platform
                ↓
Remove Manual Reconciliation
                ↓
Simplify Fulfilment Process
                ↓
Automate Remaining Repeatable Activities

The first intervention may not produce the largest immediate time saving.

It may nevertheless be a critical architectural prerequisite.

⸻

15. Architectural Judgement

Purpose

Translate evidence and analysis into an architectural conclusion.

The architect should determine:

* what the underlying problem is;
* which intervention addresses it;
* whether the intervention is proportionate;
* what dependencies exist;
* what should happen first;
* what should not be automated;
* what assumptions remain;
* what confidence exists; and
* whether the opportunity belongs within the current engagement scope.

Recommendation traceability

Every significant recommendation should be traceable through:

Finding
   ↓
Evidence
   ↓
Business / Architectural Impact
   ↓
Risk / Consequence
   ↓
Intervention Options
   ↓
Architectural Judgement
   ↓
Priority
   ↓
Roadmap Position

Example

Finding: Customer information is manually reconciled across three systems.

Evidence: Interviews, system documentation and sample transaction records confirm duplicate entry.

Impact: Manual reconciliation introduces delay and data-quality risk within a strategically important fulfilment capability.

Root Cause: Information ownership is unclear and the systems lack an effective integration boundary.

Options: Continue manual reconciliation; introduce RPA; establish information ownership and integrate systems.

Judgement: RPA would reduce keystrokes but preserve the underlying architectural condition. Establishing information ownership and an appropriate integration boundary addresses the root cause.

Priority: High, because the intervention supports a strategically important capability and enables subsequent workflow simplification.

Roadmap Position: Establish boundary before broader automation.

⸻

16. Automation Technology Selection

Technology selection follows the architectural diagnosis.

The method does not prescribe a specific automation platform.

Potential technologies include:

Workflow and low-code automation

* Make.com;
* n8n;
* Zapier;
* Microsoft Power Automate;
* other workflow orchestration platforms.

RPA

* UiPath;
* other RPA technologies where appropriate.

RPA may be useful where systems do not expose suitable integration interfaces.

It should not normally be used to conceal a systemic integration or architecture problem where a more sustainable solution is feasible.

API and integration

Potential approaches include:

* REST APIs;
* GraphQL;
* webhooks;
* event-driven integration;
* message-based integration;
* integration platforms;
* Python-based integration;
* serverless functions;
* application services.

Data and spreadsheets

Potential sources and tools include:

* Microsoft Excel;
* Google Sheets;
* Smartsheet;
* databases;
* data stores;
* operational reporting systems.

A spreadsheet should be treated as an architectural signal where it has become:

* an unofficial system of record;
* an integration layer;
* a business rules engine;
* a workflow engine; or
* a critical operational dependency.

AI and LLMs

Potential technologies include:

* large language models;
* structured extraction;
* classification;
* embeddings;
* retrieval-augmented generation;
* AI workflow orchestration;
* agentic workflows.

The selection should be based on the business and architectural requirement, not technology novelty.

⸻

17. AI / Agentic Assessment

Purpose

Determine whether AI or agentic capabilities provide material value beyond deterministic automation.

Potentially suitable characteristics

AI may be appropriate where work involves:

* unstructured information;
* natural language;
* classification;
* interpretation;
* summarisation;
* extraction;
* contextual reasoning;
* variable inputs;
* exception handling;
* knowledge retrieval; or
* decision support.

Potentially unsuitable characteristics

AI may not be appropriate where:

* deterministic rules are sufficient;
* accuracy requirements are absolute and deterministic logic can achieve them;
* explainability requirements cannot be met;
* the process is too poorly understood;
* the underlying data is unreliable;
* human accountability cannot be established;
* the AI introduces disproportionate operational complexity; or
* the expected value does not justify the additional architecture.

AI assessment dimensions

Consider:

* business value;
* accuracy;
* confidence;
* data quality;
* model behaviour;
* evaluation;
* explainability;
* security;
* privacy;
* cost;
* latency;
* availability;
* observability;
* human oversight;
* fallback;
* model/provider dependency;
* operational support.

Principle

AI should address a meaningful business or architectural need, not simply provide a more sophisticated implementation of an otherwise straightforward deterministic workflow.

⸻

18. Opportunity Classification

Each opportunity should be classified according to the dominant architectural response.

| Classification        | Typical Question                                                     |
| --------------------- | ------------------------------------------------------------------- |
| Eliminate             | Should this work stop?                                              |
| Simplify              | Can the same outcome be achieved with less complexity?              |
| Integrate             | Should systems exchange information directly?                       |
| Automate              | Should a machine perform this repeatable activity?                  |
| Fix Architecture First | What architectural condition must be addressed before the intervention? |

An opportunity may contain multiple classifications.

For example:

Fix Architecture First
        ↓
Simplify Process
        ↓
Integrate Systems
        ↓
Automate Remaining Activity

⸻

19. Assess & Prioritise Opportunities

Purpose

Determine which opportunities deserve attention first.

Prioritisation should not be reduced to a single numerical score.

The architect should consider multiple dimensions together and exercise judgement.

Core prioritisation dimensions

19.1 Strategic relevance

* Which strategic priority does the opportunity support?
* Which business outcome does it affect?
* Is the outcome material?

19.2 Capability importance

* Which capability does the opportunity affect?
* How strategically important is that capability?

19.3 Capability maturity

* How effectively does the capability operate today?
* Is low maturity itself a constraint?
* Would automation address the problem or merely mask it?

19.4 Future capability need

* Does the capability need to maintain, improve or transform?
* Does the opportunity support the required future direction?

19.5 Business impact

Consider:

* customer impact;
* employee impact;
* operational impact;
* financial impact;
* risk impact;
* strategic impact.

19.6 Value

Consider:

* time released;
* capacity released;
* cost reduction;
* quality improvement;
* risk reduction;
* revenue enablement;
* improved customer experience;
* improved reliability.

19.7 Reliability

Consider:

* current failure rates;
* operational risk;
* repeatability;
* error reduction potential;
* ability to monitor and recover.

19.8 Complexity and effort

Consider:

* technical complexity;
* process complexity;
* organisational change;
* data complexity;
* integration complexity;
* implementation effort;
* operational complexity.

19.9 Dependencies

Consider:

* prerequisite architecture changes;
* other initiatives;
* application dependencies;
* data dependencies;
* organisational dependencies;
* vendor dependencies.

19.10 Architectural fit

Consider:

* target architectural direction;
* information ownership;
* application boundaries;
* integration strategy;
* technology standards;
* operational architecture;
* strategic reuse.

19.11 Timing

Consider:

* business urgency;
* contractual constraints;
* regulatory deadlines;
* transformation sequencing;
* delivery windows;
* organisational capacity.

19.12 Confidence

Consider the quality and completeness of evidence supporting:

* value;
* effort;
* impact;
* dependency;
* risk;
* recommendation.

⸻

20. Architectural Prioritisation Judgement

Prioritisation should answer:

Which opportunities create the greatest meaningful business and architectural value relative to their complexity, dependencies and confidence, and what must happen first to enable them?

The resulting judgement may identify:

* immediate opportunities;
* foundational opportunities;
* enabling architecture changes;
* quick wins;
* strategic transformation opportunities;
* opportunities to defer;
* opportunities to reject; and
* opportunities requiring further investigation.

Important principle

A quick win is not automatically a high priority.

Similarly, a complex initiative is not automatically low priority.

An opportunity may deserve early attention because it:

* unlocks several subsequent changes;
* resolves a systemic problem;
* supports a critical capability;
* removes a major risk;
* establishes an authoritative information source; or
* creates an architectural boundary required by multiple initiatives.

⸻

21. Establish Transformation Sequence

Purpose

Translate prioritised opportunities into a coherent transformation sequence.

The roadmap should not simply be a list of independently ranked automation projects.

It should reflect architectural dependencies.

A useful transformation sequence is:

ESTABLISH CONTROL
        ↓
STABILISE
        ↓
ESTABLISH BOUNDARIES
        ↓
TRANSFORM
        ↓
SIMPLIFY
        ↓
OPTIMISE

This sequence should be adapted to the actual engagement.

Establish Control

Typical outcomes:

* ownership established;
* evidence consolidated;
* critical workflows understood;
* strategic priorities clarified;
* capability context established;
* material risks identified.

Stabilise

Typical outcomes:

* critical operational issues addressed;
* unstable workflows made predictable;
* key information quality problems reduced;
* important dependencies understood;
* operational ownership established.

Establish Boundaries

Typical outcomes:

* capability ownership clarified;
* authoritative information sources established;
* application boundaries clarified;
* integration boundaries defined;
* duplicated business rules identified and reduced.

Transform

Typical outcomes:

* priority capabilities improved;
* target architectural direction implemented;
* major process changes introduced;
* systems integrated or replaced where justified;
* strategically important workflows redesigned.

Simplify

Typical outcomes:

* redundant process steps removed;
* duplicated activities eliminated;
* unnecessary applications retired;
* manual reconciliation reduced;
* unnecessary variants removed.

Optimise

Typical outcomes:

* appropriate automation expanded;
* AI introduced where justified;
* operational performance improved;
* continuous improvement established;
* architecture becomes simpler and more sustainable.

⸻

22. Roadmap Development

The roadmap should show:

* initiative;
* business outcome;
* strategic priority;
* affected capability;
* capability importance;
* current maturity where relevant;
* target direction;
* process/journey impact;
* architectural change;
* dependencies;
* value;
* complexity;
* timing;
* confidence;
* owner;
* expected outcome.

Example

| Initiative                           | Strategic Priority       | Capability          | Architectural Dependency | Outcome                         | Sequence |
| ------------------------------------ | ------------------------ | ------------------- | ------------------------ | ------------------------------- | -------- |
| Establish customer data ownership    | Customer experience      | Customer Management | Information ownership    | Authoritative customer information | 1        |
| Integrate CRM and order platform      | Customer fulfilment      | Order Management    | Data ownership           | Remove manual reconciliation    | 2        |
| Simplify fulfilment workflow          | Operational efficiency   | Order Fulfilment    | Integration established  | Reduce process complexity       | 3        |
| Automate repeatable fulfilment tasks  | Capacity                 | Order Fulfilment    | Simplified process       | Release operational capacity    | 4        |
| Introduce AI exception handling       | Customer service         | Customer Support    | Stable workflow/data     | Improve exception processing    | 5        |

The exact structure should be adapted to the engagement.

⸻

23. Governance Gates

The assessment should use proportionate governance gates.

Gate 1 — Strategic Context

Confirm:

* relevant strategic priorities;
* business outcomes;
* assessment intent.

Gate 2 — Capability Context

Confirm:

* relevant capabilities;
* strategic importance;
* current maturity;
* future need;
* ownership.

Gate 3 — Journey / Process Context

Confirm:

* relevant journeys;
* processes;
* activities;
* actors;
* information;
* systems.

Gate 4 — Evidence Sufficiency

Confirm:

* evidence is sufficient;
* assumptions are explicit;
* material gaps are understood.

Gate 5 — Root Cause

Confirm:

* observed friction;
* business impact;
* underlying cause;
* architectural implications.

Gate 6 — Intervention

Confirm:

* eliminate;
* simplify;
* integrate;
* automate;
* and any architecture-first prerequisites.

Gate 7 — Prioritisation

Confirm:

* strategic relevance;
* capability importance;
* business impact;
* value;
* complexity;
* reliability;
* dependencies;
* architectural fit;
* confidence.

Gate 8 — Roadmap

Confirm:

* sequencing;
* dependencies;
* prerequisites;
* outcomes;
* ownership;
* timing.

Gate 9 — Architectural Accountability

Confirm:

* judgement is explicit;
* recommendation is traceable;
* uncertainty is stated;
* scope remains appropriate.

⸻

24. Typical Deliverables

Deliverables should be proportionate to the engagement.

Potential outputs include:

Strategic Context

* Strategic Context & Assessment Intent;
* strategic priorities;
* business outcomes;
* relevant goals.

Capability Context

* capability assessment;
* capability importance;
* capability maturity;
* future capability direction;
* capability ownership;
* capability dependencies.

Journey & Process Context

* customer journey;
* user journey;
* value stream;
* process map;
* workflow analysis;
* activity inventory.

Architecture Context

* application landscape;
* information flow;
* integration view;
* dependency view;
* current-state architecture;
* target architectural direction where required.

Opportunity Analysis

* opportunity register;
* root-cause analysis;
* intervention assessment;
* value/effort assessment;
* reliability assessment;
* AI suitability assessment.

Decision & Roadmap

* prioritised opportunities;
* architectural judgement;
* transformation roadmap;
* dependency model;
* recommended next steps.

Not every engagement requires every deliverable.

⸻

25. Opportunity Register

A reusable opportunity register may include:

| ID   | Strategic Priority       | Capability          | Importance | Maturity | Journey / Process | Activity       | Root Cause           | Intervention  | Value  | Complexity | Dependency    | Confidence | Priority |
| ---- | ------------------------ | ------------------- | ---------- | -------- | ----------------- | -------------- | -------------------- | ------------- | ------ | ---------- | ------------- | ---------- | -------- |
| O-01 | Customer experience      | Customer Management | High       | Medium   | Onboarding        | Data entry     | Duplicate information | Integrate     | High   | Medium     | Data ownership | High       | High     |
| O-02 | Operational efficiency   | Fulfilment          | Critical   | Low      | Order fulfilment  | Reconciliation | Weak integration      | Fix + Integrate | High | Medium     | O-01          | High       | High     |
| O-03 | Capacity                 | Fulfilment          | Critical   | Medium   | Order fulfilment  | Status updates | Repeatable activity   | Automate      | Medium | Low        | O-02          | High       | Medium   |

The register is a decision-support artefact, not a mandatory scoring mechanism.

⸻

26. AI-Assisted Delivery

AI can significantly accelerate the assessment while preserving human architectural accountability.

A typical AI-assisted workflow is:

Client Evidence
      ↓
Ingestion
      ↓
Extraction
      ↓
Evidence Organisation
      ↓
Strategy / Capability Context Extraction
      ↓
Journey / Process Mapping Support
      ↓
Candidate Findings
      ↓
Architect Review
      ↓
Root-Cause Diagnosis
      ↓
Intervention Options
      ↓
Architectural Judgement
      ↓
Prioritisation
      ↓
Roadmap
      ↓
QA

Suitable AI-assisted activities

AI can assist with:

* document ingestion;
* extraction;
* classification;
* evidence organisation;
* capability identification;
* strategy-to-capability traceability;
* process extraction;
* workflow comparison;
* duplicate activity identification;
* candidate root causes;
* pattern detection;
* candidate opportunities;
* option generation;
* evidence synthesis;
* report drafting;
* consistency checking;
* traceability checking.

Human-led activities

The architect remains responsible for:

* strategic interpretation;
* materiality;
* capability judgement;
* root-cause judgement;
* architectural judgement;
* intervention selection;
* prioritisation;
* trade-offs;
* roadmap sequencing;
* stakeholder alignment;
* recommendation;
* accountability.

AI principle

AI accelerates analysis; it does not own the architectural judgement.

⸻

27. Scope Boundaries

This method is appropriate for:

* automation discovery;
* workflow assessment;
* operational process assessment;
* spreadsheet-heavy processes;
* manual handoff analysis;
* integration opportunity assessment;
* AI opportunity assessment;
* automation portfolio prioritisation;
* architecture-led transformation planning.

It should not automatically expand into:

* enterprise strategy definition;
* full enterprise capability modelling;
* complete enterprise architecture;
* full operating model design;
* enterprise-wide application rationalisation;
* detailed solution design;
* detailed implementation architecture;
* programme delivery management.

Scope escalation

The engagement should be escalated when answering the original question requires materially broader architectural work.

Examples include:

* strategy is unclear or disputed;
* capability ownership is fundamentally unresolved;
* enterprise-wide capability restructuring is required;
* current-state architecture cannot be understood within the agreed boundary;
* target architecture must be established before opportunities can be evaluated;
* transformation dependencies extend significantly beyond the assessed domain;
* the assessment becomes a portfolio-level transformation exercise.

Potential escalation destinations include:

* Architecture Decision Review;
* Architecture Health Check;
* Architecture Assessment & Roadmap;
* Target Architecture & Strategy;
* Enterprise Transformation Architecture.

⸻

28. Relationship to Other EA Methods

Architecture Decision Review

Use when the question is:

Should we make this defined architectural or technology decision, and what should the architect recommend?

The Automation Opportunity Assessment may identify an architectural decision that subsequently requires a Decision Review.

⸻

Architecture Health Check

Use when the question is:

How healthy is the existing architecture, and what material problems should be addressed?

Automation opportunities may be evidence of broader architectural health issues.

⸻

Architecture Assessment & Roadmap

Use when the question becomes:

Where are we today, where should we go, and how should the transformation be sequenced?

The Automation Opportunity Assessment may become an input to a broader Architecture Assessment & Roadmap.

⸻

Target Architecture & Strategy

Use when the assessment requires:

* target-state architecture;
* significant architectural restructuring;
* future-state capability definition;
* strategic technology direction; or
* broader transformation architecture.

⸻

29. Reusable Proposal Pattern

The method can be packaged into a client engagement without changing the underlying methodology.

Engagement framing

I will assess your business workflows and automation opportunities from an architecture-led perspective. Rather than simply identifying tasks that can be automated, I will establish the relevant business priorities and capabilities, trace those through journeys and processes, identify the underlying causes of manual work, and determine where the appropriate response is to eliminate, simplify, integrate or automate.

Typical approach

1. Establish business priorities and outcomes
2. Identify relevant business capabilities
3. Assess capability importance and current maturity
4. Connect capabilities to journeys and processes
5. Investigate evidence and current-state architecture
6. Diagnose root causes
7. Identify intervention options
8. Assess value, complexity, reliability and dependencies
9. Prioritise opportunities
10. Develop transformation sequence
11. Validate findings and recommendations

Typical outcome

The client receives:

* a clear view of why manual work exists;
* traceability from strategy to workflow;
* capability and process context;
* evidence-based opportunity identification;
* architectural diagnosis;
* eliminate/simplify/integrate/automate recommendations;
* prioritised opportunities;
* dependencies and prerequisites;
* and a practical transformation roadmap.

⸻

30. Method Summary

The Architecture Automation Opportunity Assessment is not fundamentally an automation method.

It is an architecture-led method for connecting business strategy to the way work is performed and determining where technology-enabled change creates meaningful business value.

Its core logic is:

STRATEGY
   ↓
CAPABILITY
   ↓
JOURNEY
   ↓
PROCESS
   ↓
ACTIVITY
   ↓
INFORMATION + APPLICATIONS + PEOPLE
   ↓
FRICTION
   ↓
ROOT CAUSE
   ↓
INTERVENTION
   ↓
ARCHITECTURAL JUDGEMENT
   ↓
PRIORITY
   ↓
ROADMAP

The intervention model remains:

ELIMINATE
   ↓
SIMPLIFY
   ↓
INTEGRATE
   ↓
AUTOMATE

with:

FIX ARCHITECTURE FIRST

used as a diagnostic condition wherever the underlying architecture must be addressed before automation.

The method therefore avoids a common failure mode:

Automating the symptom while preserving the architectural problem.

Instead, it asks:

What is the business trying to achieve, which capabilities matter, how is the work actually performed, why does the friction exist, what should change, and what is the right sequence for making that change?

⸻

31. Success Criteria

An assessment is successful when it provides:

* clear strategic context;
* explicit business outcomes;
* relevant capability context;
* understanding of capability importance;
* proportionate assessment of current capability maturity;
* clear connection between capabilities and journeys/processes;
* sufficient evidence;
* explicit assumptions and uncertainties;
* understanding of workflow and architectural root causes;
* clear distinction between symptoms and underlying problems;
* credible intervention options;
* explicit eliminate/simplify/integrate/automate decisions;
* appropriate consideration of AI;
* evidence-based prioritisation;
* architectural dependency awareness;
* defensible roadmap sequencing;
* explicit architectural judgement;
* appropriate confidence;
* and clear next steps.

The assessment should leave the client able to answer:

1. What business outcome are we trying to improve?
2. Which capabilities matter to that outcome?
3. How important and mature are those capabilities?
4. How are those capabilities delivered through journeys and processes?
5. Where is friction occurring?
6. Why does the friction exist?
7. What should we eliminate, simplify, integrate or automate?
8. What architectural conditions need to be addressed first?
9. Which opportunities should we pursue first, and why?
10. What dependencies determine the sequence?
11. What should the resulting transformation roadmap look like?

⸻

32. Method Governance

This method is governed as an Engagement Method derived from the Core EA SOP.

Changes should be recorded through the Methodology Improvement Log.

A change should be promoted into the Core EA SOP only where it represents a general architectural practice principle rather than a method-specific technique.

Examples:

Appropriate for this method

* automation opportunity prioritisation;
* workflow intervention classification;
* strategy-to-capability-to-process traceability;
* capability importance and maturity considerations;
* automation suitability;
* AI suitability;
* automation dependency analysis.

Potentially appropriate for the Core EA SOP

* general principles concerning evidence;
* architectural judgement;
* proportionality;
* scope management;
* traceability;
* decision accountability;
* human/AI responsibility.

The method should therefore evolve through practical engagement experience without unnecessarily expanding the Core EA SOP.

⸻

33. Future Refinement Areas

The method is intentionally usable without introducing unnecessary scoring models or frameworks.

Future refinement may include:

* value quantification;
* time/capacity measurement;
* reliability measurement;
* automation suitability criteria;
* AI suitability criteria;
* dependency modelling;
* capability-to-process traceability templates;
* evidence/confidence calibration;
* reusable opportunity registers;
* roadmap dependency visualisation;
* client workshop formats;
* automation portfolio reporting;
* architecture decision integration;
* reusable assessment templates.

These should be validated through real engagements before being formalised.

The method should favour practical architectural judgement over artificial precision.

⸻

34. Method at a Glance

                BUSINESS STRATEGY
                       │
                       ▼
              STRATEGIC PRIORITIES
                       │
                       ▼
               BUSINESS CAPABILITIES
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
    IMPORTANCE                  MATURITY
          │                         │
          └────────────┬────────────┘
                       ▼
             JOURNEYS / VALUE STREAMS
                       │
                       ▼
                 BUSINESS PROCESSES
                       │
                       ▼
               ACTIVITIES / TASKS
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
     INFORMATION   APPLICATIONS   PEOPLE
          │            │            │
          └────────────┼────────────┘
                       ▼
              FRICTION / PAIN / RISK
                       │
                       ▼
                 ROOT CAUSE
                       │
             ┌─────────┼─────────┐
             ▼         ▼         ▼
         PROCESS    ARCHITECTURE  CAPABILITY
          CAUSE        CAUSE       CAUSE
             │         │         │
             └─────────┼─────────┘
                       ▼
                 INTERVENTION
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
    ELIMINATE       SIMPLIFY       INTEGRATE
                                       │
                                       ▼
                                   AUTOMATE
                                       │
                                  ┌────┴────┐
                                  ▼         ▼
                                AI /     DETERMINISTIC
                              AGENTIC     AUTOMATION
                                  │         │
                                  └────┬────┘
                                       ▼
                           ARCHITECTURAL JUDGEMENT
                                       │
                                       ▼
                                  PRIORITISATION
                                       │
                                       ▼
                               DEPENDENCY LOGIC
                                       │
                                       ▼
                              TRANSFORMATION ROADMAP

⸻

© 2026 Alexandre Franco · Mostelli.com · All rights reserved.
