"""
Enhanced presentation generator for MedSkill_AI_Final_Presentation.pptx
Includes:
- Slide on Chatbot vs. Dedicated Viva Trainer (MedSkill AI)
- Complete visual comparison table
- The 25 clinical problems and 8 student stakeholders
- All new features (30-second examiner pressure timer, 1-click pocket cram sheet generator, 1-click retry quiz)
- 16:9 widescreen format
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Theme colors
    c_navy = RGBColor(15, 23, 42)      # #0F172A
    c_teal = RGBColor(13, 148, 136)    # #0D9488
    c_blue = RGBColor(2, 132, 199)     # #0284C7
    c_light = RGBColor(248, 250, 252)  # #F8FAFC
    c_white = RGBColor(255, 255, 255)
    c_slate = RGBColor(100, 116, 139)  # #64748B
    c_border = RGBColor(226, 232, 240)
    c_amber = RGBColor(180, 83, 9)     # #B45309
    c_red = RGBColor(220, 38, 38)      # #DC2626
    c_green = RGBColor(22, 163, 74)    # #16A34A

    def add_header(slide, title_text, category_text="CA2 - ACTIVITY 13: DESIGN FOR THE UNSEEN"):
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.1))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p_cat = tf.paragraphs[0]
        r_cat = p_cat.add_run()
        r_cat.text = category_text.upper()
        r_cat.font.size = Pt(10)
        r_cat.font.bold = True
        r_cat.font.color.rgb = c_teal

        p_title = tf.add_paragraph()
        r_title = p_title.add_run()
        r_title.text = title_text
        r_title.font.size = Pt(24)
        r_title.font.bold = True
        r_title.font.color.rgb = c_navy

    # -------------------------------------------------------------
    # SLIDE 1: Title Slide
    # -------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = c_navy
    bg1.line.color.rgb = c_navy

    tb = s1.shapes.add_textbox(Inches(1.2), Inches(1.3), Inches(10.9), Inches(4.8))
    tf = tb.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "DEPARTMENT OF ROBOTICS & AUTOMATION | BATCH 2024-28 (SEM V) | CA2 ACTIVITY 13"
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = c_teal

    p1 = tf.add_paragraph()
    p1.text = "MedSkill AI: Practical Viva Trainer"
    p1.font.size = Pt(38)
    p1.font.bold = True
    p1.font.color.rgb = c_white
    p1.space_before = Pt(12)

    p2 = tf.add_paragraph()
    p2.text = "A Human-Centered Digital Simulator for Healthcare Technology Students"
    p2.font.size = Pt(18)
    p2.font.color.rgb = RGBColor(186, 230, 253)
    p2.space_before = Pt(6)

    p3 = tf.add_paragraph()
    p3.text = "Specialties: Respiratory Therapy | Anaesthesia Technology | Dialysis Technology\nLive Platform: https://medskill-ai.streamlit.app/ | Stanford d.school Design Thinking Framework"
    p3.font.size = Pt(13)
    p3.font.color.rgb = RGBColor(148, 163, 184)
    p3.space_before = Pt(16)

    # -------------------------------------------------------------
    # SLIDE 2: We Thought... (Assumptions & Unseen Stakeholder)
    # -------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "1. We Thought... Challenging Our Initial Assumptions")

    card1 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    card1.fill.solid()
    card1.fill.fore_color.rgb = c_white
    card1.line.color.rgb = c_border
    tf1 = card1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_right = tf1.margin_top = Inches(0.4)

    p = tf1.paragraphs[0]
    p.text = "WHAT WE INITIALLY THOUGHT"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = c_slate

    points1 = [
        "Initial Assumption: Healthcare technology students fail practical vivas because they lack lecture notes, PPTs, or reference question banks.",
        "Proposed Obvious Fix: Give students more PDF question banks or build a 3D VR ICU room to turn machine knobs.",
        "The Design Thinking Test: In Activity 13 ('Design for the Unseen'), we suspended assumptions and immersed ourselves in the hospital floor."
    ]
    for pt in points1:
        p = tf1.add_paragraph()
        p.text = f"• {pt}"
        p.font.size = Pt(11.5)
        p.font.color.rgb = c_navy
        p.space_before = Pt(10)

    card2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    card2.fill.solid()
    card2.fill.fore_color.rgb = c_white
    card2.line.color.rgb = c_border
    tf2 = card2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_right = tf2.margin_top = Inches(0.4)

    p = tf2.paragraphs[0]
    p.text = "THE UNSEEN STAKEHOLDERS (8 STUDENTS)"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = c_teal

    points2 = [
        "The Cohort: Allied health technologists operating mechanical ventilators, anaesthesia workstations, and dialyzers.",
        "Why Unseen: Instructors see them attaching circuits and assume mastery. But oral vivas by external examiners cause deep panic.",
        "Direct Research Participants: Riddhi, Siddhi, Naziya, Preethi, Bhargav, Naveen, Tharun, and Atharv.",
        "Observation Grounding: Shadowed 6 clinical shifts across adult ICUs, emergency OTs, and hemodialysis suites."
    ]
    for pt in points2:
        p = tf2.add_paragraph()
        p.text = f"• {pt}"
        p.font.size = Pt(11.5)
        p.font.color.rgb = c_navy
        p.space_before = Pt(8)

    # -------------------------------------------------------------
    # SLIDE 3: We Observed & Discovered (The 25 Clinical Problems)
    # -------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "2. We Observed & Discovered... (25 Real Clinical Problems)")

    cats = [
        ("A. Airway & Circuit Hazards", [
            "Low water levels in oxygen humidifier bottles (inspissated secretions)",
            "Accidental patient self-extubation during nurse turns",
            "Ventilator circuit disconnection during repositioning",
            "Undetected NIV mask leaks compromising ventilation",
            "Endotracheal tube (ETT) depth migration past incisors",
            "Delayed suctioning causing secretion plugging"
        ]),
        ("B. Alarms & Critical Events", [
            "Delayed response to high-priority ventilator alarms",
            "Severe ICU Alarm Fatigue (reflexive muting)",
            "Unidentified patient-ventilator asynchrony (double triggering)",
            "Dialyzer TMP spikes & fiber membrane clotting",
            "Delayed recognition of patient respiratory deterioration",
            "Repeated unmonitored desaturation episodes"
        ]),
        ("C. Ward Workflow & Transport", [
            "Incomplete respiratory therapist shift handovers",
            "Time-consuming manual paper flowsheet charting",
            "Transport oxygen cylinder pressure depletion",
            "Equipment unavailability during emergency code calls",
            "Missing/lost chest X-ray jackets during morning rounds",
            "Expired equipment maintenance & sensor calibrations"
        ]),
        ("D. Data Overload & Reasoning", [
            "Difficulty correlating real-time ABG reports with vent changes",
            "Missed spontaneous breathing trials (SBT) for weaning",
            "Inadequate monitoring of delivered FiO2 & flow rates",
            "Managing pending RT orders across 15-20 beds",
            "Lack of a centralized respiratory monitoring dashboard"
        ])
    ]

    col_w = Inches(2.75)
    gap = Inches(0.2)
    left_start = Inches(0.8)
    for c_i, (c_title, c_probs) in enumerate(cats):
        c_left = left_start + c_i * (col_w + gap)
        box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c_left, Inches(1.8), col_w, Inches(5.0))
        box.fill.solid()
        box.fill.fore_color.rgb = c_white
        box.line.color.rgb = c_border
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.25)
        
        p = tf.paragraphs[0]
        p.text = c_title
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = c_blue

        for prob in c_probs:
            p = tf.add_paragraph()
            p.text = f"• {prob}"
            p.font.size = Pt(9)
            p.font.color.rgb = c_navy
            p.space_before = Pt(4)

    # -------------------------------------------------------------
    # SLIDE 4: We Realised the Real Problem Was... (Root Cause)
    # -------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "3. We Realised the Real Problem Was: Passive Revision Syndrome")

    rc_box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(11.733), Inches(5.0))
    rc_box.fill.solid()
    rc_box.fill.fore_color.rgb = c_white
    rc_box.line.color.rgb = c_border
    tf_rc = rc_box.text_frame
    tf_rc.word_wrap = True
    tf_rc.margin_left = tf_rc.margin_right = tf_rc.margin_top = Inches(0.5)

    p = tf_rc.paragraphs[0]
    p.text = "THE ROOT CAUSE DISCOVERED BEHIND ALL 25 PROBLEMS:"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = c_teal

    p_quote = tf_rc.add_paragraph()
    p_quote.text = "\"Students know what button to press, but freeze completely when external examiners ask WHY a ventilator pressure spiked or HOW an APL valve functions.\""
    p_quote.font.size = Pt(16)
    p_quote.font.bold = True
    p_quote.font.color.rgb = c_navy
    p_quote.space_before = Pt(10)

    rc_points = [
        "Passive Revision Syndrome: Reading PDFs, notes, and manuals creates an illusion of competence. Passive reading does not activate active recall circuits.",
        "Oral Viva Reality: Examiners do not give 4 multiple-choice options; they ask rapid oral questions under severe time pressure.",
        "Fear of Judgment: Mock vivas with seniors or professors induce fear. Students need a safe, zero-judgment digital sandbox.",
        "The Missing Bridge: No educational tool existed that bridged routine hospital procedures with verbal physiological reasoning.",
        "Reframed Problem Statement: How might we provide healthcare technology students with an accessible, interactive digital viva simulator that pinpoints conceptual misconceptions and provides verified textbook explanations without requiring complex infrastructure?"
    ]
    for pt in rc_points:
        p = tf_rc.add_paragraph()
        p.text = f"• {pt}"
        p.font.size = Pt(11)
        p.font.color.rgb = c_navy
        p.space_before = Pt(6)

    # -------------------------------------------------------------
    # SLIDE 5: CHATBOT VS. DEDICATED VIVA TRAINER (KEY DIFFERENTIATOR)
    # -------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "4. What Makes MedSkill AI Different From a Generic AI Chatbot?")

    # Comparison Table
    t_shape = s5.shapes.add_table(rows=7, cols=3, left=Inches(0.8), top=Inches(1.8), width=Inches(11.733), height=Inches(5.0))
    table = t_shape.table
    table.columns[0].width = Inches(2.5)
    table.columns[1].width = Inches(4.5)
    table.columns[2].width = Inches(4.733)

    t_headers = ["Evaluation Dimension", "Generic AI Chatbot (ChatGPT / Claude / Copilot)", "MedSkill AI (Dedicated Viva Simulator)"]
    for j, h in enumerate(t_headers):
        cell = table.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = c_navy
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = c_white

    comp_data = [
        ("Curriculum Grounding", "Generic, unpredictable generation; prone to clinical hallucinations & unverified values.", "144 verified curriculum questions anchored in Egan, Miller, and Daugirdas textbooks."),
        ("Psychological Viva Urgency", "No time pressure. Chatbots sit passively waiting for user text with zero stress stimulus.", "30-Second Examiner Pressure Mode: Active countdown timer replicating oral viva anxiety."),
        ("Offline Reliability", "Requires 100% active cloud connection; completely fails in shielded hospital basements & labs.", "100% Offline-First Architecture: Local keyword retrieval engine runs with zero API keys or network."),
        ("Structured Practice Flow", "Open-ended chat log with no concept of passing, failing, difficulty tiers, or topics.", "Dual Mode (Objective MCQ + Quick Viva comparison against model instructor answers)."),
        ("Remediation & Takeaways", "No structured gap analysis. Student must prompt 'quiz me on what I got wrong'.", "1-Click Retry Quiz targeting missed items + 1-Click Pocket Viva Cram Sheet (.docx generator)."),
        ("Clinical Safety Boundaries", "Unbounded generative text; may hallucinate dangerous prescribing recommendations.", "Strict educational scope; explicit clinical disclaimer; no diagnostic or clinical liability.")
    ]
    for r_idx, (d0, d1, d2) in enumerate(comp_data, start=1):
        for c_idx, val in enumerate([d0, d1, d2]):
            cell = table.cell(r_idx, c_idx)
            cell.fill.solid()
            if c_idx == 2:
                cell.fill.fore_color.rgb = RGBColor(240, 253, 244) if r_idx % 2 == 1 else RGBColor(240, 253, 250)
            else:
                cell.fill.fore_color.rgb = c_light if r_idx % 2 == 1 else c_white
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(9.5)
            p.font.color.rgb = c_navy

    # -------------------------------------------------------------
    # SLIDE 6: We Generated & Killed Our First Idea (Ideation)
    # -------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "5. We Generated & Killed Our First Idea (Concept Selection)")

    k_box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    k_box.fill.solid()
    k_box.fill.fore_color.rgb = c_white
    k_box.line.color.rgb = c_border
    tf_k = k_box.text_frame
    tf_k.word_wrap = True
    tf_k.margin_left = tf_k.margin_right = tf_k.margin_top = Inches(0.4)

    p = tf_k.paragraphs[0]
    p.text = "KILL YOUR FIRST IDEA: 3D VR KNOB SIMULATOR"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = c_red

    k_points = [
        "First Obvious Idea: Build a 3D Virtual Reality simulator where students walk through an ICU and turn virtual ventilator knobs.",
        "Why We Killed It (Evidence-Based):",
        "1. Wrong Problem: Students already touch real ventilators every shift. Their deficit is verbal conceptual reasoning, not motor skills.",
        "2. Cost Barrier: VR headsets and gaming graphics cards are unaffordable for typical government college students.",
        "3. High Friction: Large file downloads and setup time prevent quick 5-minute study sessions during hospital tea breaks."
    ]
    for pt in k_points:
        p = tf_k.add_paragraph()
        p.text = f"• {pt}"
        p.font.size = Pt(11)
        p.font.color.rgb = c_navy
        p.space_before = Pt(8)

    id_box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    id_box.fill.solid()
    id_box.fill.fore_color.rgb = c_white
    id_box.line.color.rgb = c_border
    tf_id = id_box.text_frame
    tf_id.word_wrap = True
    tf_id.margin_left = tf_id.margin_right = tf_id.margin_top = Inches(0.4)

    p = tf_id.paragraphs[0]
    p.text = "10 IDEAS GENERATED -> SELECTED STRATEGY"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = c_teal

    sel_points = [
        "1. Paper flashcards (Discarded: static, no feedback)",
        "2. Heavy Android/iOS app (Discarded: app store barriers)",
        "3. Voice-only AI chatbot (Discarded: high latency, poor speech recognition on medical terms in noisy labs)",
        "4. Web-based practical viva simulator (SELECTED)",
        "5. 3D VR knob simulator (KILLED: wrong problem)",
        "6. Peer-to-peer audio calls (Discarded: scheduling conflicts)",
        "7. Rule-based targeted gap recommendations (SELECTED)",
        "8. Curated 144-question curriculum bank (SELECTED)",
        "9. Offline-first intelligence with optional AI (SELECTED)",
        "10. Gamified points leaderboard (Deprioritized: distraction)"
    ]
    for pt in sel_points:
        p = tf_id.add_paragraph()
        p.text = f"• {pt}"
        p.font.size = Pt(9.5)
        p.font.color.rgb = c_navy
        p.space_before = Pt(4)

    # -------------------------------------------------------------
    # SLIDE 7: Users Told Us... So We Changed (Evidence of Iteration)
    # -------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "6. Users Told Us... So We Changed (Evidence of Iteration)")

    t7_shape = s7.shapes.add_table(rows=8, cols=3, left=Inches(0.8), top=Inches(1.8), width=Inches(11.733), height=Inches(5.0))
    t7 = t7_shape.table
    t7.columns[0].width = Inches(2.2)
    t7.columns[1].width = Inches(4.5)
    t7.columns[2].width = Inches(5.033)

    t7_headers = ["Stakeholder", "Observed Friction in Prototype 1", "Engineering Iteration in Prototype 2"]
    for j, h in enumerate(t7_headers):
        cell = t7.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = c_navy
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = c_white

    iter_data = [
        ("Riddhi (Resp. Tech)", "Dark-mode mobile phones rendered white font on white cards (invisible text).", "Locked .streamlit/config.toml to light base + enforced dark navy !important CSS typography."),
        ("Siddhi (Resp. Tech)", "Initial bank had only 2 questions per topic; insufficient for full 2-hour viva revision.", "Expanded question bank to 144 verified questions (exactly 12 in every topic across 12 topics)."),
        ("Naziya (Allied Health)", "Vivas are verbal! Students freeze when asked to formulate an oral answer aloud.", "Engineered Quick Viva Mode: students type/draft answers and compare against reference model answers."),
        ("Bhargav (Anaesthesia)", "Students had to restart the entire 20-question quiz just to review 2 missed mistakes.", "Engineered 1-Click Quick Retry Quiz isolating only incorrect questions for immediate retest."),
        ("Naveen (ICU Posting)", "Hospital basements have zero mobile reception; app crashed if API key missing.", "Built Offline-First Knowledge Engine searching local verified records with zero crash risk."),
        ("Preethi (Resp. Care)", "Students panic because external examiners rush them; untimed quizzes don't prepare for viva.", "Engineered 30-Second Examiner Pressure Mode: Rapid countdown timer with red urgency alerts."),
        ("Tharun (Resp. Care)", "Students cannot take laptops/phones into the viva examination waiting hall.", "Engineered 1-Click Pocket Viva Cram Sheet Generator creating printable 2-page .docx summaries.")
    ]
    for r_idx, (stk, fric, iter_desc) in enumerate(iter_data, start=1):
        for c_idx, val in enumerate([stk, fric, iter_desc]):
            cell = t7.cell(r_idx, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = c_light if r_idx % 2 == 1 else c_white
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(9.5)
            p.font.color.rgb = c_navy

    # -------------------------------------------------------------
    # SLIDE 8: Final Solution & Platform Architecture
    # -------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "7. Our Final Solution: MedSkill AI (Live Deployed Platform)")

    f_box = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(11.733), Inches(5.0))
    f_box.fill.solid()
    f_box.fill.fore_color.rgb = c_white
    f_box.line.color.rgb = c_border
    tf_f = f_box.text_frame
    tf_f.word_wrap = True
    tf_f.margin_left = tf_f.margin_right = tf_f.margin_top = Inches(0.4)

    p = tf_f.paragraphs[0]
    p.text = "MEDSKILL AI — PRODUCTION PLATFORM & NEW FEATURE SUITE"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = c_teal

    final_bullets = [
        "Live Deployment: Hosted live on Streamlit Community Cloud at https://medskill-ai.streamlit.app/",
        "144 Verified Curriculum Questions: Exactly 12 questions in each of the 12 core topics across Respiratory Therapy, Anaesthesia, and Dialysis technology.",
        "Dual-Mode Simulation: Seamlessly switch between Objective MCQ practice and Spoken Quick Viva self-evaluation against reference instructor models.",
        "NEW: 30-Second Examiner Pressure Mode: Rapid countdown timer injecting realistic exam-hall urgency with visual color changes.",
        "NEW: 1-Click Pocket Viva Cram Sheet Generator: Produces compact, printable .docx cheat-sheets summarizing high-yield clinical rules & missed questions.",
        "NEW: 1-Click Quick Retry Quiz: Automatically isolates failed items so students can immediately achieve 100% mastery.",
        "100% Offline-First Architecture: Tier 1 local knowledge engine runs without internet or API keys; Tier 2 provides optional Gemini integration.",
        "Verified Impact: Tested with 8 core student stakeholders (Riddhi, Siddhi, Naziya, Preethi, Bhargav, Naveen, Tharun, Atharv) + 6 peer technologists."
    ]
    for fb in final_bullets:
        p = tf_f.add_paragraph()
        p.text = f"• {fb}"
        p.font.size = Pt(11)
        p.font.color.rgb = c_navy
        p.space_before = Pt(6)

    prs.save("MedSkill_AI_Final_Presentation.pptx")
    print("Saved updated MedSkill_AI_Final_Presentation.pptx successfully!")

if __name__ == "__main__":
    create_deck()
