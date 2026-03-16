# AI Agent Incident Case Library: Real-World Failures and Analysis

## 1. Narrative-Ready Cases (High Priority)

### 1.1 The Air Canada Chatbot Negligent Misrepresentation
*   **Scenario:** In late 2022, passenger Jake Moffatt sought bereavement fare information via an AI-powered chatbot on Air Canada’s website following a family death.
*   **Failure Point:** The chatbot "hallucinated" an outdated policy, informing the passenger they could apply for a refund retroactively within 90 days. This directly contradicted the airline’s actual policy requiring pre-booking requests.
*   **Consequences:** The passenger paid full price and was denied a refund. The British Columbia Civil Resolution Tribunal (CRT)—Canada's first online tribunal designed for accessible and speedy adjudication—held the airline liable for negligent misrepresentation. The airline was ordered to pay $812 in damages and fees (*Moffatt v. Air Canada*, 2024).
*   **Fix/Action:** This case operationalizes the "separate agent" fallacy. The airline argued the chatbot was a "separate legal entity" responsible for its own actions—a defense the Tribunal dismissed as "remarkable." Applying the **Learned Hand formula (B < P * L)**, the burden (B) of ensuring the chatbot was fed accurate information was negligible compared to the high probability (P) of misinformation and the financial loss (L) to the consumer. Legally, the deployer is the "cheapest cost avoider" and remains liable for all website representations, regardless of whether they are static or automated.
*   **Quotable Sentence:** "It makes no difference whether the information comes from a static page or a chatbot; the corporation remains liable for the representations of its automated systems."
*   **Sources:**
    *   St-Hilaire (2025): "Lying Chatbot Makes Airline Liable: Negligent Misrepresentation in Moffatt v Air Canada," UBC Law Review.
    *   Conformance AI: "The Air Canada Chatbot Case" (May 2024).

### 1.2 The Uber Self-Driving Fatal Classification Error (Arizona)
*   **Scenario:** A semi-autonomous Uber vehicle underwent public road testing in Tempe, Arizona, in 2018.
*   **Failure Point:** The automated system failed to correctly classify a pedestrian. The safety driver, tasked with passive monitoring, suffered from "vigilance decrement"—seeking external stimulation to combat the boredom of supervising a mostly reliable system—and was streaming *The Voice* on Hulu at the time of the collision.
*   **Consequences:** A fatal collision occurred. Uber reached a civil settlement, but the safety driver was charged with negligent homicide, effectively serving as a "liability sponge" for systemic failures in automation design.
*   **Fix/Action:** This incident highlights the "Moral Crumple Zone," where human operators absorb the legal impact of systemic defects. The failure demonstrates that the **Burden of Precaution (B)** must include shifting from "presence of oversight" to "capacity for oversight." Meaningful Human-Systems Integration (HSI) requires active engagement protocols rather than passive observation, as the human brain is evolutionarily ill-suited for the latter.
*   **Quotable Sentence:** "When an AI fails, the human operator is often positioned as a 'liability sponge,' absorbing the legal impact of systemic automation defects."
*   **Sources:**
    *   NTSB: "Collision Between Vehicle Controlled by Developmental Automated Driving System and Pedestrian" (2019).
    *   Min Htin (2026): "Redefining the Standard of Human Oversight for AI Negligence," Harvard Journal of Law & Technology.

### 1.3 Verily Health Data Breach and Valuation Collapse
*   **Scenario:** Verily, an AI-driven health platform, managed electronic Protected Health Information (ePHI) for over 25,000 patients.
*   **Failure Point:** The organization failed to report HIPAA breaches and monitor vulnerabilities. This was exacerbated by the proliferation of **"Shadow AI"**—the use of unauthorized or unendorsed AI tools by employees. Research indicates 67% of physicians use AI tools daily, often bypassing formal governance.
*   **Consequences:** A whistleblower lawsuit and regulatory scrutiny led to an 80% collapse in the company's valuation.
*   **Fix/Action:** Compliance requires moving beyond "Shadow AI" toward formal governance. Organizations must establish designated oversight roles, conduct comprehensive audits of all AI tools (endorsed or otherwise), and implement risk management activities as mandated by evolving HHS/HIPAA regulations.
*   **Quotable Sentence:** "The use of 'Shadow AI' and the failure to report vulnerabilities can lead to catastrophic valuation loss and legal enforcement."
*   **Sources:**
    *   Brooks Pierce (2026): "The Need for Comprehensive Governance of AI Use in Health Care Settings."

### 1.4 Sriwijaya Air Flight 182: Automation Disengagement
*   **Scenario:** A commercial flight utilizing an autothrottle system to manage engine thrust.
*   **Failure Point:** A mechanical autothrottle malfunction occurred. The flight crew, experiencing "out-of-the-loop unfamiliarity" due to prolonged reliance on the automated system, failed to monitor engine instruments for several minutes. When the autopilot disengaged, the crew lacked the cognitive engagement to recover.
*   **Consequences:** A fatal crash claiming 62 lives.
*   **Fix/Action:**
    *   **Technical Fix:** Update autothrottle systems and monitoring alerts.
    *   **Governance Fix:** Implement HSI frameworks that utilize **Friction Roles** (forcing humans to perform active tasks, like inputting reasoning before seeing an AI output, to maintain vigilance) and **Resilience Roles** (AI providing "cognitive handrails" such as Uncertainty Quantification to signal when the model is operating outside its training distribution).
*   **Quotable Sentence:** "The human brain is wired for active engagement, not for prolonged periods of inactive supervision of a mostly reliable AI."
*   **Sources:**
    *   BBC News: "Sriwijaya Air crash... blamed on throttle and pilot error" (2022).
    *   Min Htin (2026): "Redefining the Standard of Human Oversight for AI Negligence," Harvard Journal of Law & Technology.

## 2. Candidate Cases (Weak Evidence/Incomplete)

### 2.1 Microsoft Bing Chat (Sydney) Internal Data Leak
*   **[Weak Evidence]** Lacks specific legal or financial resolution details.
*   **Scenario:** During an interaction, the assistant "Sydney" inadvertently disclosed internal development information and instructions to a user.
*   **Context:** This serves as a primary example of sensitive data exposure through "prompt injection" or extraction techniques.
*   **Sources:** Generative AI Security: Key Risks and Protection Strategies (2025).

### 2.2 Discriminatory Lending AI Patterns
*   **[Weak Evidence]** Lacks specific company names or case files.
*   **Scenario:** AI systems in the financial sector exhibited discriminatory patterns in credit decisions.
*   **Analysis:** This represents a systemic governance failure where **Shadow AI** tools used in credit scoring bypass traditional anti-discrimination audits, leading to regulatory penalties and reputational harm.
*   **Sources:** Generative AI Security: Key Risks and Protection Strategies; Brooks Pierce (2026).

### 2.3 Italian Ban on ChatGPT (March 2023)
*   **[Weak Evidence]** A regulatory event rather than a specific accident or technical failure.
*   **Scenario:** The Italian Data Protection Authority (Garante) identified GDPR violations, including lack of age verification and legal basis for data collection, leading to a temporary nationwide ban.
*   **Sources:** Generative AI Security: Key Risks and Protection Strategies (2025).

## 3. Writing Strategy and Support

### 3.1 Master Thesis Support: "The Illusion of the Separate Agent"
The documented cases prove that the legal defense of "The AI did it" is functionally obsolete.
*   **Deployer as Cheapest Cost Avoider:** Per the **Learned Hand formula**, the Burden of Precaution (B) sits with the company deploying the tool. If the cost of testing/HSI is less than the probability of harm (P) times the loss (L), the company is negligent.
*   **Rejection of Agency:** Courts (notably the CRT in the Air Canada case) have clarified that an AI is not a separate legal person; it is a component of corporate infrastructure for which the corporation holds absolute liability.
*   **Human Limits:** HSI must account for human "cognitive bandwidth." Simply placing a human "in the loop" does not satisfy the duty of care if the system design induces vigilance decrement or automation bias.

### 3.2 Primary Narratives for Storytelling
*   **Recommendation 1: Air Canada Chatbot.** Ideal for illustrating **Consumer Trust and the "Separate Agent" Fallacy.** This case is the most relatable for business policy-makers, proving that hallucinations are a corporate liability, not a technical excuse.
*   **Recommendation 2: The Uber/Arizona Crash.** Ideal for illustrating **The Moral Crumple Zone.** By highlighting the driver streaming *The Voice*, the narrative shifts from "driver error" to a systemic failure of HSI design, forcing a discussion on why "human-in-the-loop" is often a regulatory trap.

## 4. Technical Appendix: Failure Classification

| Risk Category | Description | Legal/Regulatory Lever | Case Example |
| :--- | :--- | :--- | :--- |
| **Model Vulnerability** | Exploitation of model logic or classification errors (e.g., prompt injection). | Tort / Negligence | Uber/Arizona (Classification Error) |
| **Misuse / Output Risks** | Generation of hallucinations or biased content; failures in truthfulness. | Consumer Protection / Tort | Air Canada Chatbot (Hallucination) |
| **Data-Related Risks** | Exposure of sensitive information or ePHI; violations of privacy statutes. | HIPAA / GDPR | Verily Health (Data Breach) |
| **Governance Risks** | Failures in oversight, reporting, or "Shadow AI" management. | Administrative Law / HIPAA | Uber/Arizona (Automation Bias) |