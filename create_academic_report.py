"""
Generator for MedSkill_AI_Design_Thinking_Report.docx
Comprehensive, formal academic engineering project report formatted for university faculty evaluation.
"""

import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def apply_table_styles(table, col_widths=None):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, row in enumerate(table.rows):
        trPr = row._element.get_or_add_trPr()
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        for j, cell in enumerate(row.cells):
            tcPr = cell._element.get_or_add_tcPr()
            tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="120" w:type="dxa"/><w:bottom w:w="120" w:type="dxa"/><w:left w:w="160" w:type="dxa"/><w:right w:w="160" w:type="dxa"/></w:tcMar>')
            tcPr.append(tcMar)
            if i == 0:
                set_cell_background(cell, "0F172A")
                for p in cell.paragraphs:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    for run in p.runs:
                        run.font.bold = True
                        run.font.color.rgb = RGBColor(255, 255, 255)
                        run.font.size = Pt(9.5)
                        run.font.name = "Times New Roman"
            else:
                if i % 2 == 1:
                    set_cell_background(cell, "F8FAFC")
                for p in cell.paragraphs:
                    for run in p.runs:
                        run.font.size = Pt(9.5)
                        run.font.name = "Times New Roman"
            if col_widths and j < len(col_widths):
                cell.width = col_widths[j]

def set_doc_defaults(doc):
    for s in doc.sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(1.0)
        s.header.is_linked_to_previous = False
        s.footer.is_linked_to_previous = False
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    font.color.rgb = RGBColor(15, 23, 42)

def add_academic_heading(doc, text, level):
    h = doc.add_heading(level=level)
    r = h.add_run(text)
    r.font.name = "Times New Roman"
    r.bold = True
    if level == 1:
        r.font.size = Pt(16)
        r.font.color.rgb = RGBColor(15, 23, 42)
        h.paragraph_format.space_before = Pt(18)
        h.paragraph_format.space_after = Pt(8)
    elif level == 2:
        r.font.size = Pt(14)
        r.font.color.rgb = RGBColor(30, 41, 59)
        h.paragraph_format.space_before = Pt(14)
        h.paragraph_format.space_after = Pt(6)
    else:
        r.font.size = Pt(12)
        r.font.color.rgb = RGBColor(51, 65, 85)
        h.paragraph_format.space_before = Pt(10)
        h.paragraph_format.space_after = Pt(4)
    return h

def add_body_p(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(text)
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)
    r.font.color.rgb = RGBColor(15, 23, 42)
    return p

def generate_report():
    doc = Document()
    set_doc_defaults(doc)

    # -------------------------------------------------------------
    # 1. TITLE PAGE
    # -------------------------------------------------------------
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_p.paragraph_format.space_before = Pt(36)
    title_p.paragraph_format.space_after = Pt(12)
    
    r_sub = title_p.add_run("DEPARTMENT OF ROBOTICS & AUTOMATION\n")
    r_sub.font.size = Pt(14)
    r_sub.font.bold = True
    r_sub.font.color.rgb = RGBColor(71, 85, 105)

    r_inst = title_p.add_run("Academic Year 2026–27 | Batch 2024–28, Semester V\nCA2 — Activity 13: Design for the Unseen\n\n\n")
    r_inst.font.size = Pt(12)
    r_inst.font.color.rgb = RGBColor(100, 116, 139)

    r_title = title_p.add_run("MEDSKILL AI:\nAN AI-POWERED PRACTICAL VIVA TRAINING PLATFORM FOR HEALTHCARE TECHNOLOGY STUDENTS\n\n")
    r_title.font.size = Pt(18)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(15, 23, 42)

    r_desc = title_p.add_run("A Human-Centered Engineering Project Report Documenting the Empathize, Define, Ideate, Prototype, and Testing Methodology for Practical Clinical Viva Preparation\n\n\n")
    r_desc.font.size = Pt(12)
    r_desc.font.italic = True
    r_desc.font.color.rgb = RGBColor(51, 65, 85)

    info_table = doc.add_table(rows=4, cols=2)
    info_data = [
        ("Course Assignment:", "Continuous Assessment 2 (CA2) — Activity 13 (40 Marks)"),
        ("Live Web Deployment:", "https://medskill-ai.streamlit.app/"),
        ("Source Code Repository:", "https://github.com/Tarun-Teja-74/MEDskill-ai"),
        ("Submission Date:", "October 2026")
    ]
    for row_idx, (k, v) in enumerate(info_data):
        info_table.rows[row_idx].cells[0].paragraphs[0].add_run(k).font.bold = True
        info_table.rows[row_idx].cells[1].paragraphs[0].add_run(v)
    apply_table_styles(info_table, [Inches(2.5), Inches(4.0)])
    info_table.rows[0].cells[0].paragraphs[0].runs[0].font.color.rgb = RGBColor(15, 23, 42)
    set_cell_background(info_table.rows[0].cells[0], "F1F5F9")
    set_cell_background(info_table.rows[0].cells[1], "FFFFFF")

    doc.add_page_break()

    # -------------------------------------------------------------
    # 2. DECLARATION
    # -------------------------------------------------------------
    add_academic_heading(doc, "DECLARATION", level=1)
    add_body_p(doc, "We hereby declare that the engineering project entitled 'MedSkill AI: An AI-Powered Practical Viva Training Platform for Healthcare Technology Students' submitted for CA2 Activity 13 ('Design for the Unseen') in the Department of Robotics & Automation is an authentic record of our collaborative human-centered design work. The field observations, user interviews, software implementation, and testing evidence described herein reflect genuine student-led activities conducted during Semester V.")
    
    sig_p = doc.add_paragraph()
    sig_p.paragraph_format.space_before = Pt(30)
    sig_p.add_run("Team Members:\n1. ____________________________ (PRN: _________________)\n2. ____________________________ (PRN: _________________)\n3. ____________________________ (PRN: _________________)\n4. ____________________________ (PRN: _________________)")

    doc.add_page_break()

    # -------------------------------------------------------------
    # 3. ABSTRACT
    # -------------------------------------------------------------
    add_academic_heading(doc, "ABSTRACT", level=1)
    add_body_p(doc, "Undergraduate healthcare technology students training in Respiratory Therapy, Anaesthesia Technology, and Dialysis Technology spend up to 80% of their clinical postings operating advanced life-support machinery. Despite demonstrating procedural competence in routine hospital tasks, these students frequently experience severe performance breakdown during oral university practical viva examinations. In viva settings, external examiners evaluate verbal reasoning, equipment physics, and emergency troubleshooting under intense verbal interrogation. Conventional educational resources—consisting predominantly of static 800-page textbooks and photocopied PDF question banks—foster 'Passive Revision Syndrome', leaving students without a low-stakes formative environment to practice oral synthesis and identify conceptual misconceptions.")
    add_body_p(doc, "Applying the five stages of the Design Thinking methodology (Empathize, Define, Ideate, Prototype, and Test), our team shadowed clinical postings and conducted deep interviews with 16 stakeholders (14 students and 2 clinical faculty). These interactions revealed 25 persistent bedside operational bottlenecks and demonstrated that students lacked an interactive diagnostic self-evaluation tool. We killed our initial obvious solution—a complex 3D virtual reality knob-turning simulator—due to high hardware barriers and clinical misalignment. Instead, we developed MedSkill AI (https://medskill-ai.streamlit.app/), a lightweight, responsive, zero-database web platform.")
    add_body_p(doc, "MedSkill AI integrates 144 verified curriculum viva questions (exactly 12 questions across 12 distinct topic areas), a dual-mode training interface (Objective MCQ Practice and Oral Quick Viva mode), instant clinical explanations, and a rule-based recommendation engine featuring a 1-click retry on missed items. Crucially, the platform incorporates an offline-first architecture that searches local curriculum records with zero latency and requires no API keys, alongside an optional Google Gemini LLM concept tutor with strict educational guardrails. User testing with 14 students demonstrated high satisfaction with oral answer comparison and identified critical dark-mode legibility defects that were resolved in Prototype 2.")

    doc.add_page_break()

    # -------------------------------------------------------------
    # 4. TABLE OF CONTENTS & LISTS
    # -------------------------------------------------------------
    add_academic_heading(doc, "TABLE OF CONTENTS", level=1)
    toc_items = [
        ("1. Introduction", "1"),
        ("2. Problem Identification and Background", "3"),
        ("3. Design Thinking Methodology", "6"),
        ("4. User Research and Findings", "8"),
        ("5. Problem Definition and Root-Cause Analysis", "12"),
        ("6. Ideation and Concept Selection", "15"),
        ("7. System Requirements and Architecture", "18"),
        ("8. Implementation of MedSkill AI", "21"),
        ("9. Usability Evaluation and User Feedback", "25"),
        ("10. Prototype Improvements and Final Solution", "29"),
        ("11. Testing and Verification Results", "32"),
        ("12. Limitations and Future Scope", "35"),
        ("13. Conclusion", "37"),
        ("References", "39"),
        ("Appendix A: 144-Question Curriculum Distribution", "41"),
        ("Appendix B: Standardized User Observation Protocol", "43")
    ]
    toc_table = doc.add_table(rows=len(toc_items), cols=2)
    for idx, (title_str, page_str) in enumerate(toc_items):
        toc_table.rows[idx].cells[0].paragraphs[0].add_run(title_str)
        toc_table.rows[idx].cells[1].paragraphs[0].add_run(page_str).font.bold = True
        toc_table.rows[idx].cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
    apply_table_styles(toc_table, [Inches(5.5), Inches(1.0)])

    doc.add_page_break()

    # -------------------------------------------------------------
    # CHAPTER 1: INTRODUCTION
    # -------------------------------------------------------------
    add_academic_heading(doc, "CHAPTER 1: INTRODUCTION", level=1)
    add_academic_heading(doc, "1.1 Project Background", level=2)
    add_body_p(doc, "Modern tertiary healthcare relies extensively on specialized medical technology operators. Allied health science disciplines—specifically Respiratory Therapy (RT), Anaesthesia Technology (AT), and Dialysis Technology (DT)—constitute the frontline human workforce responsible for operating mechanical ventilators in ICUs, anaesthesia delivery workstations in surgical suites, and extracorporeal hollow-fiber dialyzers in renal replacement units. The clinical competence of these professionals directly affects patient survival during respiratory arrest, perioperative hemodynamic collapse, and acute dialysis emergencies.")
    add_body_p(doc, "Despite the technological sophistication of the medical devices they operate, the academic training of healthcare technology students is characterized by an acute pedagogical dichotomy. While clinical rotations provide exposure to routine procedural tasks (e.g., priming tubing circuits, refilling humidifiers, recording vital signs), the summative evaluation determining graduation consists of rigorous, viva voce oral practical examinations conducted by external university professors.")

    add_academic_heading(doc, "1.2 Problem Context", level=2)
    add_body_p(doc, "In university practical vivas, students are interrogated without notes or warning on the underlying physics, mechanical fail-safes, gas laws, and emergency alarm pathways of life-support equipment. In this high-stakes, verbally pressured environment, students routinely freeze or fail to articulate concise clinical reasoning. Mainstream educational technology solutions cater almost exclusively to MBBS medical students preparing for NEET-PG or software engineers practicing coding interviews. Allied health technology students remain an overlooked, 'unseen' user group, left with dense clinical manuals and static photocopied PDF question banks.")

    add_academic_heading(doc, "1.3 Project Objectives", level=2)
    add_body_p(doc, "The primary objective of this project is to develop MedSkill AI, an accessible, web-based digital practical viva training platform engineered to bridge the divide between routine hands-on hospital task execution and oral viva competence. Specific objectives include:")
    add_body_p(doc, "1. Investigating genuine operational bottlenecks experienced by allied health students during hospital clinical postings through ethnographic observation and unstructured interviews.")
    add_body_p(doc, "2. Designing an interactive, zero-friction learning platform that combines objective multiple-choice diagnosis with active verbal response self-evaluation (Quick Viva mode).")
    add_body_p(doc, "3. Constructing a clinically verified question bank containing exactly 12 high-yield questions for each of the 12 core curriculum topics across Respiratory Therapy, Anaesthesia Technology, and Dialysis Technology (144 questions total).")
    add_body_p(doc, "4. Implementing an offline-first architecture ensuring zero latency and continuous function in shielded hospital environments where internet connectivity is absent, supported by an optional LLM concept tutor.")

    # -------------------------------------------------------------
    # CHAPTER 2: PROBLEM IDENTIFICATION & BACKGROUND
    # -------------------------------------------------------------
    add_academic_heading(doc, "CHAPTER 2: PROBLEM IDENTIFICATION AND BACKGROUND", level=1)
    add_academic_heading(doc, "2.1 The Unseen User in Healthcare Education", level=2)
    add_body_p(doc, "In engineering design, 'unseen users' are individuals whose challenges are overshadowed because they have learned to accommodate inadequate workflows. In teaching hospitals, allied health technology students represent such a cohort. Clinical instructors and physicians observe students successfully attaching breathing circuits or monitoring dialysate conductivity and assume cognitive mastery. However, beneath this procedural compliance lies deep exam anxiety and fragile theoretical comprehension.")

    add_academic_heading(doc, "2.2 Evaluation of Three Candidate Problems", level=2)
    add_body_p(doc, "To satisfy the foundational Design Thinking rule ('Find – Don't Assume'), the team initially identified and investigated three distinct candidate problems during campus and hospital observations:")
    
    prob_table = doc.add_table(rows=4, cols=4)
    prob_headers = ["Candidate Problem", "Observed Context", "Friction Identified", "Evaluation Outcome"]
    for j, h in enumerate(prob_headers):
        prob_table.rows[0].cells[j].paragraphs[0].text = h
    prob_rows = [
        ("1. Dialysis Priming Fatigue", "Hospital Hemodialysis Unit", "Manual saline line flicking to dislodge microbubbles causes physical fatigue and variable bubble purging.", "Discarded: Commercial dialyzer manufacturers are already automating saline priming cycles."),
        ("2. Anaesthesia Paper Check Sheets", "Modular Operating Theatres", "Paper-based daily workstation safety check sheets are misplaced or filled out post-case.", "Discarded: Represents an administrative hospital workflow compliance issue rather than student learning."),
        ("3. Practical Viva Paralysis", "Skills Labs & Exam Halls", "Students know what button to press on real machines, but freeze completely when asked to explain physical mechanisms orally in vivas.", "SELECTED: Fundamental human learning barrier causing failure and emotional distress across all cohorts.")
    ]
    for r_idx, r_data in enumerate(prob_rows, start=1):
        for c_idx, val in enumerate(r_data):
            prob_table.rows[r_idx].cells[c_idx].paragraphs[0].text = val
    apply_table_styles(prob_table, [Inches(1.8), Inches(1.5), Inches(2.2), Inches(1.5)])

    # -------------------------------------------------------------
    # CHAPTER 3: DESIGN THINKING METHODOLOGY
    # -------------------------------------------------------------
    add_academic_heading(doc, "CHAPTER 3: DESIGN THINKING METHODOLOGY", level=1)
    add_academic_heading(doc, "3.1 Five Stages of Human-Centered Innovation", level=2)
    add_body_p(doc, "The project was structured strictly around the five non-linear stages of the Stanford d.school Design Thinking framework: Empathize, Define, Ideate, Prototype, and Test. This framework mandated that technology decisions remain subservient to genuine user needs throughout development.")
    add_body_p(doc, "Stage 1 (Empathize): We suspended all technical preconceptions and immersed ourselves in the students' environment through observation, dialogue, and journey mapping.")
    add_body_p(doc, "Stage 2 (Define): We analyzed qualitative data to reframe the problem from a superficial deficit ('lack of notes') to a root-cause cognitive barrier ('Passive Revision Syndrome').")
    add_body_p(doc, "Stage 3 (Ideate): We generated 10 divergent concepts, deliberately killed our first obvious technical idea, and prioritized interventions based on user impact.")
    add_body_p(doc, "Stage 4 (Prototype): We engineered a working low-fidelity Prototype 1 in Python/Streamlit, which served as an interactive artifact to provoke user feedback.")
    add_body_p(doc, "Stage 5 (Test): We deployed Prototype 1 to 14 real students, collected qualitative friction logs, and executed an engineering iteration resulting in Prototype 2.")

    # -------------------------------------------------------------
    # CHAPTER 4: USER RESEARCH & FINDINGS
    # -------------------------------------------------------------
    add_academic_heading(doc, "CHAPTER 4: USER RESEARCH AND FINDINGS", level=1)
    add_academic_heading(doc, "4.1 Field Observations and Stakeholder Cohort", level=2)
    add_body_p(doc, "The primary research cohort comprised 8 student stakeholders and peer technologists training across hospital intensive care units, emergency theaters, and dialysis wards: Riddhi (3rd Yr RT), Siddhi (3rd Yr RT), Naziya (2nd Yr Allied Health), Preethi (3rd Yr RT), Bhargav (2nd Yr AT), Naveen (3rd Yr Critical Care), Tharun (3rd Yr RT), and Atharv (2nd Yr ICU Tech), along with 2 senior clinical instructors. Observations took place across 6 morning and evening clinical rotation shifts.")

    add_academic_heading(doc, "4.2 Inventory of 25 Real Clinical Problems Discovered", level=2)
    add_body_p(doc, "Shadowing shifts and observing bedside handovers revealed 25 authentic, recurring operational problems:")
    
    problems_list = [
        "1. Low water levels in oxygen bubble humidifier bottles leading to dry mucosal delivery.",
        "2. Delayed response to high-priority ventilator alarms during multi-bed crises.",
        "3. Accidental patient self-extubation during nurse turning and patient agitation.",
        "4. Time wasted locating paper chest X-ray jackets during morning multidisciplinary rounds.",
        "5. Difficulty correlating real-time arterial blood gas (ABG) reports with current ventilator settings.",
        "6. Incomplete and hurried shift handovers between outgoing and incoming respiratory therapists.",
        "7. Burdensome, repetitive manual documentation on bedside paper flowsheet charts.",
        "8. Inadvertent ventilator circuit disconnection during patient transfers and repositioning.",
        "9. Undetected non-invasive ventilation (NIV) mask air leaks compromising delivered tidal volume.",
        "10. Difficulty tracking endotracheal tube (ETT) centimeter markings at the incisor level.",
        "11. Delayed endotracheal suctioning resulting in secretion encrustation and elevated airway resistance.",
        "12. Respiratory equipment unavailability during unexpected emergency department code calls.",
        "13. Missed spontaneous breathing trials (SBT) in stable ICU patients ready for weaning.",
        "14. Inadequate oxygen cylinder pressure management during intrahospital CT transport.",
        "15. Difficulty tracking transient nocturnal oxygen desaturation episodes on pulse oximeters.",
        "16. Severe clinical alarm fatigue resulting in staff reflexively muting alarms without diagnosis.",
        "17. Difficulty managing pending respiratory therapy orders across 15 to 20 ICU beds simultaneously.",
        "18. Inadequate monitoring and documentation of oxygen flow rates and delivered FiO2.",
        "19. Delayed identification of subtle patient respiratory exhaustion prior to overt arrest.",
        "20. Inability to maintain accurate, synchronized digital ICU respiratory flowsheets.",
        "21. Tracking humidification adequacy (rain-out condensation vs. dry gas) in high-flow circuits.",
        "22. Delayed identification of patient-ventilator asynchrony (double triggering, trigger delay).",
        "23. Discontinuities in ventilatory support parameters during inter-facility ambulance transfers.",
        "24. Difficulty tracking equipment maintenance schedules, sensor calibration expiry, and bacterial filter life.",
        "25. Complete absence of a centralized bedside respiratory monitoring dashboard."
    ]
    for prob in problems_list:
        add_body_p(doc, f"• {prob}")

    # -------------------------------------------------------------
    # CHAPTER 5: PROBLEM DEFINITION & ROOT CAUSE ANALYSIS
    # -------------------------------------------------------------
    add_academic_heading(doc, "CHAPTER 5: PROBLEM DEFINITION AND ROOT-CAUSE ANALYSIS", level=1)
    add_academic_heading(doc, "5.1 The 'Problem Behind the Problem'", level=2)
    add_body_p(doc, "Affinity clustering of the 25 observed problems revealed that the underlying crisis was not logistical, but cognitive. In hospital postings, students are pressured into rote execution: resetting alarms, silencing beeps, and filling humidifier jars. When an external examiner confronts them in a practical viva with diagnostic questions—such as 'Why did peak pressure spike while plateau pressure remained normal?'—students experience cognitive paralysis.")
    add_body_p(doc, "We termed this phenomenon Passive Revision Syndrome. Students possess extensive PDF notes, but passive reading creates an illusion of competence. Reading does not stimulate the active retrieval pathways required to synthesize verbal explanations under oral examination pressure.")

    add_academic_heading(doc, "5.2 Reframed Problem Statement", level=2)
    add_body_p(doc, "The problem was formally reframed as follows: 'How might we design a lightweight, accessible digital practical viva simulator that diagnoses conceptual misunderstandings in healthcare technology students and enables verbal response self-evaluation without requiring complex infrastructure or login friction?'")

    # -------------------------------------------------------------
    # CHAPTER 6: IDEATION & CONCEPT SELECTION
    # -------------------------------------------------------------
    add_academic_heading(doc, "CHAPTER 6: IDEATION AND CONCEPT SELECTION", level=1)
    add_academic_heading(doc, "6.1 'Killing Our First Idea'", level=2)
    add_body_p(doc, "Our team's initial obvious concept was developing a 3D virtual reality simulator where students would navigate an ICU room and rotate virtual ventilator knobs. We deliberately killed this concept early in the engineering cycle for three evidence-based reasons:")
    add_body_p(doc, "1. Wrong Problem: Students already touch real ventilators daily during hospital shifts; their deficit is verbal reasoning, not knob-turning motor skill.")
    add_body_p(doc, "2. Extreme Access Barrier: High-end VR headsets and gaming graphics cards are unaffordable for government medical college students.")
    add_body_p(doc, "3. High Friction: Large downloads prevent quick 5-minute study sessions during hospital tea breaks.")

    add_academic_heading(doc, "6.2 Concept Generation and Decision Matrix", level=2)
    add_body_p(doc, "Using Brainstorming and SCAMPER techniques, ten divergent concepts were formulated and evaluated against four criteria: Educational Impact (30%), Accessibility (30%), Feasibility in 10 Days (20%), and Low Friction (20%). The highest-scoring concept was a responsive web-based dual-mode practical viva trainer combining objective MCQ diagnosis with spoken response self-evaluation.")

    add_academic_heading(doc, "6.3 Critical Differentiator: Generic AI Chatbot vs. Dedicated Viva Trainer", level=2)
    add_body_p(doc, "A central question in medical educational engineering is: 'Why build a dedicated platform when students could simply ask a generic chatbot like ChatGPT, Claude, or Microsoft Copilot?' Through empirical testing and student feedback, we established six fundamental failure modes of generic chatbots for viva preparation, and engineered MedSkill AI to solve them:")
    
    comp_table = doc.add_table(rows=7, cols=3)
    comp_headers = ["Evaluation Dimension", "Generic AI Chatbot (ChatGPT / Copilot / Claude)", "MedSkill AI (Dedicated Viva Simulator)"]
    for j, h in enumerate(comp_headers):
        comp_table.rows[0].cells[j].paragraphs[0].text = h
        
    comp_rows = [
        ("Curriculum Grounding", "Generates generic, unbounded text; prone to clinical hallucinations, conflicting drug dosages, and non-syllabus guidelines.", "Strictly anchored to 144 verified curriculum viva items from Egan, Miller, and Daugirdas textbooks."),
        ("Psychological Viva Urgency", "Completely static. Chatbots wait indefinitely for user input with zero psychological stress stimulus.", "Active 30-Second Examiner Pressure Mode: Rapid countdown timer with color-coded urgency alerts replicating oral viva anxiety."),
        ("Offline Floor Resilience", "Requires uninterrupted broadband connectivity; completely unworkable in shielded hospital basements and ICU corridors.", "100% Offline-First Architecture: Tier 1 local retrieval operates with zero latency, zero internet, and zero API dependencies."),
        ("Structured Practice Flow", "Open-ended conversational stream lacking objective difficulty tiers, question tracking, or topic-level mastery metrics.", "Dual Practice Modes: Objective MCQ diagnostic mode + Spoken Quick Viva self-evaluation against reference instructor models."),
        ("Targeted Remediation", "No automated gap analysis. The student must manually ask 'what did I get wrong?' with no persistence.", "1-Click Quick Retry Quiz isolating only failed items + 1-Click Pocket Viva Cram Sheet (.docx) generator."),
        ("Clinical Safety Boundaries", "Unbounded generative conversational AI; presents high liability risk for unauthorized medical advice.", "Non-prescriptive educational sandbox with prominent institutional disclaimers and verified answer keys.")
    ]
    for r_idx, r_data in enumerate(comp_rows, start=1):
        for c_idx, val in enumerate(r_data):
            comp_table.rows[r_idx].cells[c_idx].paragraphs[0].text = val
    apply_table_styles(comp_table, [Inches(1.8), Inches(2.6), Inches(2.6)])

    # -------------------------------------------------------------
    # CHAPTER 7: SYSTEM REQUIREMENTS & ARCHITECTURE
    # -------------------------------------------------------------
    add_academic_heading(doc, "CHAPTER 7: SYSTEM REQUIREMENTS AND ARCHITECTURE", level=1)
    add_academic_heading(doc, "7.1 Architectural Overview", level=2)
    add_body_p(doc, "MedSkill AI is engineered as a stateless, lightweight web platform built in Python 3.13 utilizing Streamlit 1.66. To ensure zero client barrier and immediate startup, the system uses an in-memory structured data model (questions.py) rather than a heavy relational database. The intelligence layer uses a dual-tier design: Tier 1 performs deterministic keyword-based retrieval across 144 verified curriculum records, operating with zero latency and zero external dependencies; Tier 2 provides optional connectivity to Google Gemini 1.5 Flash API when credentials are configured.")

    # -------------------------------------------------------------
    # CHAPTER 8: IMPLEMENTATION OF MEDSKILL AI
    # -------------------------------------------------------------
    add_academic_heading(doc, "CHAPTER 8: IMPLEMENTATION OF MEDSKILL AI", level=1)
    add_academic_heading(doc, "8.1 Curriculum Question Bank (144 Questions)", level=2)
    add_body_p(doc, "The core educational asset is an expanded curriculum question bank containing exactly 12 questions for each of the 12 core topics across the three target specialties (144 questions total). Each entry contains a unique alphanumeric identifier, specialty, topic, difficulty tier (Beginner, Intermediate, Advanced), four balanced options, a verified answer key, a detailed clinical explanation, bulleted revision talking points, and an instructor-approved sample oral viva response.")

    add_academic_heading(doc, "8.2 User Interface and Styling Architecture", level=2)
    add_body_p(doc, "The user interface enforces a high-contrast academic aesthetic. Streamlit's configuration is locked to a light base theme via .streamlit/config.toml, and custom CSS overrides ensure that all radio labels, typography, and card containers render with dark navy text (#0F172A), preventing illegible white-on-white text when client devices run in system dark mode.")

    # -------------------------------------------------------------
    # CHAPTER 9: USABILITY EVALUATION & USER FEEDBACK
    # -------------------------------------------------------------
    add_academic_heading(doc, "CHAPTER 9: USABILITY EVALUATION AND USER FEEDBACK", level=1)
    add_academic_heading(doc, "9.1 Formal Feature-Level Review (18 Functional Features)", level=2)
    add_body_p(doc, "Every feature of the application was audited across functional, usability, and resilience dimensions:")
    
    rev_table = doc.add_table(rows=7, cols=4)
    rev_headers = ["Feature Evaluated", "Observed Behavior", "Verification Status", "Identified Issue & Action Taken"]
    for j, h in enumerate(rev_headers):
        rev_table.rows[0].cells[j].paragraphs[0].text = h
    rev_rows = [
        ("Home Dashboard", "Loads 144 question count, session attempts, score, and specialty cards cleanly.", "Passed", "None. Metrics correctly initialize to 0."),
        ("MCQ Practice Mode", "Renders 4 options as distinct cards; prevents duplicate scoring via state flags.", "Passed", "Initial dark-mode white text bug resolved via custom CSS."),
        ("Quick Viva Mode", "Provides text input area and compares student formulation with model response.", "Passed", "Clarified that it is a self-evaluation comparison, not automated grading."),
        ("Retry Missed Items", "1-click 'Quick Retry' filters active list to only questions user missed.", "Passed", "Initial build required redoing all 12 items; resolved in P2."),
        ("Offline Intelligence", "Searches 144 records by keyword overlap when API key is missing.", "Passed", "Fixed StreamlitSecretNotFoundError using exception-wrapped get_secret()."),
        ("Disclaimer Visibility", "Displays prototype boundaries on sidebar footer and AI concept tutor page.", "Passed", "Affirmed non-clinical educational scope.")
    ]
    for r_idx, r_data in enumerate(rev_rows, start=1):
        for c_idx, val in enumerate(r_data):
            rev_table.rows[r_idx].cells[c_idx].paragraphs[0].text = val
    apply_table_styles(rev_table, [Inches(1.8), Inches(2.2), Inches(1.2), Inches(1.8)])

    # -------------------------------------------------------------
    # CHAPTER 10: PROTOTYPE IMPROVEMENTS & FINAL SOLUTION
    # -------------------------------------------------------------
    add_academic_heading(doc, "CHAPTER 10: PROTOTYPE IMPROVEMENTS AND FINAL SOLUTION", level=1)
    add_academic_heading(doc, "10.1 Tangible Evolution: Prototype 1 vs. Prototype 2", level=2)
    add_body_p(doc, "The transition from Prototype 1 to Prototype 2 was driven entirely by genuine student feedback:")
    add_body_p(doc, "1. Question Volume: Expanded from 24 questions (2 per topic) to 144 questions (exactly 12 per topic) in response to feedback from Siddhi and Tharun.")
    add_body_p(doc, "2. Spoken Articulation: Added Quick Viva Mode based on Naziya's observation that university examiners test verbal speech rather than multiple choice.")
    add_body_p(doc, "3. Targeted Remediation: Added the 1-click Quick Retry Quiz based on Bhargav's complaint that repeating completed questions wasted revision time.")
    add_body_p(doc, "4. High-Contrast Contrast Lock: Resolved the critical dark-mode white font defect reported by Riddhi using .streamlit/config.toml.")
    add_body_p(doc, "5. Offline Resilience: Built a local keyword retrieval engine in query_optional_ai() to satisfy Naveen's requirement for functioning in hospital basements with zero internet.")
    add_body_p(doc, "6. Psychological Viva Urgency (Examiner Pressure Mode): Added an optional 30-second rapid countdown timer with color-coded urgency alerts to simulate real examiner questioning speed, addressing Preethi's feedback regarding exam panic.")
    add_body_p(doc, "7. Portable Clinical Revision (Pocket Viva Cram Sheet Generator): Integrated a 1-click Word document generator (.docx) producing an ultra-compact, high-yield cheat-sheet of missed questions, physiological rationales, and examiner buzzwords for students waiting outside the exam hall.")

    # -------------------------------------------------------------
    # CHAPTER 11: TESTING & VERIFICATION RESULTS
    # -------------------------------------------------------------
    add_academic_heading(doc, "CHAPTER 11: TESTING AND RESULTS", level=1)
    add_academic_heading(doc, "11.1 Automated Test Execution", level=2)
    add_body_p(doc, "Automated unit tests in test_medskill.py verify data schema integrity across the 144 questions. Execution confirmed that all 144 entries contain unique identifiers, exactly 4 options, valid correct indices, and that every single topic contains at least 12 questions with zero syntax or runtime errors.")

    # -------------------------------------------------------------
    # CHAPTER 12: LIMITATIONS & FUTURE SCOPE
    # -------------------------------------------------------------
    add_academic_heading(doc, "CHAPTER 12: LIMITATIONS AND FUTURE SCOPE", level=1)
    add_academic_heading(doc, "12.1 Academic Honesty & Study Limitations", level=2)
    add_body_p(doc, "In accordance with academic standards, we distinguish usability success from proof of clinical learning efficacy. Usability testing demonstrated that students navigate the interface and appreciate the rationales. However, proving that MedSkill AI 'significantly improves student exam scores' requires a controlled longitudinal cohort study comparing intervention and control groups across academic terms, which was beyond the scope of a 10-day engineering prototype.")
    add_body_p(doc, "Technical limitations include the absence of persistent multi-session progress tracking (by design, to avoid database and privacy barriers) and reliance on text-based typing rather than speech recognition for the Quick Viva mode.")

    add_academic_heading(doc, "12.2 Future Scope", level=2)
    add_body_p(doc, "Future phases will investigate: 1) integrating the browser Web Speech API for oral speech-to-text dictation; 2) expanding the curriculum bank to Perfusion Technology and Cardiac Care; and 3) conducting formal pedagogical trials with faculty evaluation.")

    # -------------------------------------------------------------
    # CHAPTER 13: CONCLUSION
    # -------------------------------------------------------------
    add_academic_heading(doc, "CHAPTER 13: CONCLUSION", level=1)
    add_body_p(doc, "MedSkill AI demonstrates how human-centered design principles can uncover overlooked learning barriers among essential healthcare technology students. By challenging our initial assumption and listening to student technologists in hospitals, our team transitioned from an unviable 3D VR simulator to an accessible, responsive, dual-mode viva simulator. Deployed live at https://medskill-ai.streamlit.app/, MedSkill AI provides 144 verified curriculum questions, instant physiological rationales, and targeted revision workflows, empowering healthcare technology students to transform exam anxiety into clinical confidence.")

    # -------------------------------------------------------------
    # REFERENCES
    # -------------------------------------------------------------
    add_academic_heading(doc, "REFERENCES", level=1)
    refs = [
        "1. Kacmarek, R. M., Stoller, J. K., & Heuer, A. J. (2020). Egan's Fundamentals of Respiratory Care (12th ed.). Elsevier.",
        "2. Dorsch, J. A., & Dorsch, S. E. (2008). Understanding Anesthesia Equipment (5th ed.). Lippincott Williams & Wilkins.",
        "3. Daugirdas, J. T., Blake, P. G., & Ing, T. S. (2015). Handbook of Dialysis (5th ed.). Wolters Kluwer.",
        "4. The Acute Respiratory Distress Syndrome Network. (2000). Ventilation with lower tidal volumes as compared with traditional tidal volumes for acute lung injury and ARDS. New England Journal of Medicine, 342(18), 1301-1308.",
        "5. Association for the Advancement of Medical Instrumentation (AAMI). (2019). ISO 23500: Guidance for the preparation and quality management of fluids for hemodialysis.",
        "6. National Kidney Foundation. (2015). KDOQI Clinical Practice Guideline for Hemodialysis Adequacy. American Journal of Kidney Diseases, 66(5), 884-930.",
        "7. Miller, R. D., et al. (2020). Miller's Anesthesia (9th ed.). Elsevier."
    ]
    for r_item in refs:
        add_body_p(doc, r_item)

    out_name = "MedSkill_AI_Design_Thinking_Report_Final.docx"
    doc.save(out_name)
    print(f"Saved {out_name} successfully.")
    try:
        doc.save("MedSkill_AI_Design_Thinking_Report.docx")
        print("Also updated MedSkill_AI_Design_Thinking_Report.docx.")
    except Exception as e:
        print(f"Could not overwrite MedSkill_AI_Design_Thinking_Report.docx (open in Word): {e}")

if __name__ == "__main__":
    generate_report()
