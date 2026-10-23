"""
Generator for MedSkill_AI_Final_Presentation.pptx
Professional 16:9 widescreen slide deck for 5-minute university panel evaluation.
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Colors
    c_navy = RGBColor(15, 23, 42)      # #0F172A
    c_teal = RGBColor(13, 148, 136)    # #0D9488
    c_blue = RGBColor(2, 132, 199)     # #0284C7
    c_light = RGBColor(248, 250, 252)  # #F8FAFC
    c_white = RGBColor(255, 255, 255)
    c_slate = RGBColor(100, 116, 139)  # #64748B
    c_card_bg = RGBColor(255, 255, 255)
    c_border = RGBColor(226, 232, 240)

    def add_header(slide, title_text, category_text="CA2 - ACTIVITY 13: DESIGN FOR THE UNSEEN"):
        # Header shape
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.733), Inches(1.2))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p_cat = tf.paragraphs[0]
        r_cat = p_cat.add_run()
        r_cat.text = category_text.upper()
        r_cat.font.size = Pt(11)
        r_cat.font.bold = True
        r_cat.font.color.rgb = c_teal

        p_title = tf.add_paragraph()
        r_title = p_title.add_run()
        r_title.text = title_text
        r_title.font.size = Pt(26)
        r_title.font.bold = True
        r_title.font.color.rgb = c_navy

    # -------------------------------------------------------------
    # SLIDE 1: Title Slide
    # -------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    # Background fill
    bg = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = c_navy
    bg.line.color.rgb = c_navy

    tb = s1.shapes.add_textbox(Inches(1.2), Inches(1.5), Inches(10.9), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "DEPARTMENT OF ROBOTICS & AUTOMATION | BATCH 2024-28 (SEM V)"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = c_teal

    p1 = tf.add_paragraph()
    p1.text = "MedSkill AI: Practical Viva Trainer"
    p1.font.size = Pt(40)
    p1.font.bold = True
    p1.font.color.rgb = c_white
    p1.space_before = Pt(14)

    p2 = tf.add_paragraph()
    p2.text = "A Human-Centered Digital Simulator for Healthcare Technology Students"
    p2.font.size = Pt(20)
    p2.font.color.rgb = RGBColor(148, 163, 184)
    p2.space_before = Pt(8)

    p3 = tf.add_paragraph()
    p3.text = "CA2 — Activity 13: Design for the Unseen | Live Web Platform: https://medskill-ai.streamlit.app/"
    p3.font.size = Pt(13)
    p3.font.color.rgb = c_teal
    p3.space_before = Pt(30)

    p4 = tf.add_paragraph()
    p4.text = "Target Disciplines: Respiratory Therapy | Anaesthesia Technology | Dialysis Technology"
    p4.font.size = Pt(12)
    p4.font.color.rgb = c_white
    p4.space_before = Pt(10)

    # -------------------------------------------------------------
    # SLIDE 2: We Thought... & Initial Assumptions
    # -------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "1. We Thought... Challenging Our First Understanding")

    # Card 1: What We Initially Thought
    c1 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8))
    c1.fill.solid()
    c1.fill.fore_color.rgb = c_light
    c1.line.color.rgb = c_border
    tf1 = c1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_right = tf1.margin_top = Inches(0.4)
    p = tf1.paragraphs[0]
    p.text = "WHAT WE INITIALLY THOUGHT"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = RGBColor(220, 38, 38)
    
    bullets1 = [
        "Students fail clinical vivas because they lack reference notes or textbook question banks.",
        "The obvious solution was compiling another massive PDF question bank or digital flashcard app.",
        "Students who operate equipment during 8-hour hospital postings naturally understand the underlying machine physics.",
        "Rote memorization of hospital SOPs is sufficient for university examinations."
    ]
    for b in bullets1:
        p = tf1.add_paragraph()
        p.text = f"• {b}"
        p.font.size = Pt(12)
        p.font.color.rgb = c_navy
        p.space_before = Pt(10)

    # Card 2: The Unseen Stakeholder
    c2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(2.0), Inches(5.7), Inches(4.8))
    c2.fill.solid()
    c2.fill.fore_color.rgb = c_light
    c2.line.color.rgb = c_border
    tf2 = c2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_right = tf2.margin_top = Inches(0.4)
    p = tf2.paragraphs[0]
    p.text = "THE UNSEEN STAKEHOLDER"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = c_blue

    bullets2 = [
        "Undergraduate technologists in Respiratory, Anaesthesia, and Dialysis technology.",
        "They operate complex life-support machines (ventilators, absorbers, hemodialyzers) during ICU rotations.",
        "Overlooked by mainstream EdTech (which caters only to doctors/MBBS or software coders).",
        "Experience extreme verbal paralysis when external university examiners ask them to explain physical laws aloud."
    ]
    for b in bullets2:
        p = tf2.add_paragraph()
        p.text = f"• {b}"
        p.font.size = Pt(12)
        p.font.color.rgb = c_navy
        p.space_before = Pt(10)

    # -------------------------------------------------------------
    # SLIDE 3: We Observed & Discovered... (25 Problems & 8 Students)
    # -------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "2. We Observed & Discovered... 25 Real Clinical Bottlenecks")

    # 4 domain cards
    domains = [
        ("A. Alarm Fatigue & Failures", "Problems: 2, 8, 16, 22\n• Delayed response to ventilator alarms\n• Disconnection during repositioning\n• Severe ICU alarm desensitization\n• Missed patient-ventilator asynchrony"),
        ("B. Airway & Patient Hazards", "Problems: 1, 3, 9, 10, 11, 21\n• Dry oxygen humidifier bottles\n• Accidental self-extubation risks\n• Unmonitored NIV mask air leaks\n• Endotracheal tube depth migration"),
        ("C. Equipment & Transport Risks", "Problems: 12, 14, 18, 24\n• Equipment missing during admissions\n• Cylinder depletion during transport\n• Uncalibrated sensors & expired seals\n• Inadequate monitoring of flowmeters"),
        ("D. Data Overload & Reasoning", "Problems: 4, 5, 6, 7, 13, 15, 17, 20\n• Disconnect between ABG and vent settings\n• Incomplete shift handovers\n• Missed spontaneous weaning trials\n• Hours lost on manual paperwork")
    ]
    for idx, (d_title, d_desc) in enumerate(domains):
        x = Inches(0.8 + (idx % 2) * 5.9)
        y = Inches(2.0 + (idx // 2) * 2.5)
        box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.6), Inches(2.3))
        box.fill.solid()
        box.fill.fore_color.rgb = c_light
        box.line.color.rgb = c_border
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = Inches(0.3)
        p = tf.paragraphs[0]
        p.text = d_title
        p.font.bold = True
        p.font.size = Pt(13)
        p.font.color.rgb = c_teal

        p2 = tf.add_paragraph()
        p2.text = d_desc
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = c_navy
        p2.space_before = Pt(4)

    # -------------------------------------------------------------
    # SLIDE 4: We Realised the Real Problem Was...
    # -------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "3. We Realised the Real Problem Was... Passive Revision Syndrome")

    main_card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(2.0), Inches(10.3), Inches(4.8))
    main_card.fill.solid()
    main_card.fill.fore_color.rgb = c_white
    main_card.line.color.rgb = c_border
    tf = main_card.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.6)

    p = tf.paragraphs[0]
    p.text = "THE ROOT CAUSE DISCOVERED BEHIND ALL 25 PROBLEMS:"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = c_blue

    points = [
        "Floor Reality vs Exam Reality: In hospital postings, students execute physical tasks mechanically under high pressure. They rarely verbalize *why* a parameter behaves a certain way.",
        "Passive Revision Syndrome: Students own 500+ pages of PDF notes. Reading creates an illusion of mastery, but fails completely when an external examiner demands immediate oral synthesis.",
        "Zero Low-Stakes Practice: There was no accessible digital simulator to test conceptual depth, expose misconceptions, and practice oral articulation before facing university examiners.",
        "Reframed Problem Statement (How Might We): 'How might we build an accessible, interactive digital viva simulator that diagnoses conceptual misunderstandings in healthcare technology students and enables verbal response self-evaluation without requiring complex infrastructure?'"
    ]
    for pt in points:
        p = tf.add_paragraph()
        p.text = f"• {pt}"
        p.font.size = Pt(13)
        p.font.color.rgb = c_navy
        p.space_before = Pt(12)

    # -------------------------------------------------------------
    # SLIDE 5: We Generated & Killed Our First Idea
    # -------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "4. We Generated 10 Ideas & Killed Our First Solution")

    # Killed idea card
    k_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8))
    k_box.fill.solid()
    k_box.fill.fore_color.rgb = RGBColor(254, 242, 242)
    k_box.line.color.rgb = RGBColor(254, 202, 202)
    tf_k = k_box.text_frame
    tf_k.word_wrap = True
    tf_k.margin_left = tf_k.margin_top = Inches(0.4)
    p = tf_k.paragraphs[0]
    p.text = "KILL YOUR FIRST IDEA: 3D VR KNOB SIMULATOR"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = RGBColor(185, 28, 28)

    k_points = [
        "First obvious thought: build a 3D virtual reality simulator where students turn ventilator knobs.",
        "Why It Failed / Discarded:",
        "1. Solves the WRONG problem: Students already touch real machines in hospital postings; their real bottleneck is verbal clinical reasoning.",
        "2. Cost & Access Barrier: VR headsets and high-end GPUs are completely inaccessible to government college students.",
        "3. High Friction: 2GB+ downloads prevent quick study during 10-minute clinical tea breaks."
    ]
    for kp in k_points:
        p = tf_k.add_paragraph()
        p.text = kp
        p.font.size = Pt(11.5)
        p.font.color.rgb = c_navy
        p.space_before = Pt(8)

    # Selected solutions card
    s_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(2.0), Inches(5.7), Inches(4.8))
    s_box.fill.solid()
    s_box.fill.fore_color.rgb = RGBColor(240, 253, 244)
    s_box.line.color.rgb = RGBColor(187, 247, 208)
    tf_s = s_box.text_frame
    tf_s.word_wrap = True
    tf_s.margin_left = tf_s.margin_top = Inches(0.4)
    p = tf_s.paragraphs[0]
    p.text = "10 IDEAS GENERATED -> SELECTED STRATEGY"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = RGBColor(21, 128, 61)

    s_points = [
        "Used Brainstorming & SCAMPER across 10 concepts (flashcards, voice bots, peer calling, knob games, mobile apps).",
        "Key Decisions Made:",
        "• Idea 4 (Selected): Web-based Dual-Mode Practical Viva Trainer (MCQ + Quick Viva Mode) with zero login friction.",
        "• Idea 7 (Selected): Targeted Rule-Based Study Recommendations isolating only missed questions.",
        "• Idea 8 (Selected): Curated 144-Question Verified Curriculum Bank (12 per topic).",
        "• Idea 9 (Selected): Offline-First Knowledge Engine with optional Gemini LLM fallback."
    ]
    for sp in s_points:
        p = tf_s.add_paragraph()
        p.text = sp
        p.font.size = Pt(11.5)
        p.font.color.rgb = c_navy
        p.space_before = Pt(8)

    # -------------------------------------------------------------
    # SLIDE 6: We Built Prototype 1
    # -------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "5. We Built Prototype 1: Initial Fast Interactive Build")

    p1_box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(2.0), Inches(10.3), Inches(4.8))
    p1_box.fill.solid()
    p1_box.fill.fore_color.rgb = c_light
    p1_box.line.color.rgb = c_border
    tf_p1 = p1_box.text_frame
    tf_p1.word_wrap = True
    tf_p1.margin_left = tf_p1.margin_right = tf_p1.margin_top = Inches(0.5)

    p = tf_p1.paragraphs[0]
    p.text = "PROTOTYPE 1 ARCHITECTURE & CAPABILITIES"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = c_blue

    p1_features = [
        "Rapid Python + Streamlit Web Implementation: Built as an interactive prototype to test formative practice.",
        "24 Curated Practical Questions: 8 questions per specialty across Respiratory, Anaesthesia, and Dialysis technology.",
        "Basic MCQ Mechanics: 4-option radio selection with synchronous Check Answer feedback.",
        "Basic Score Metrics: Tracking attempted questions, correct count, and live session accuracy.",
        "Initial Limitation Identified: Lacked oral self-testing; small question bank; broke if external API key was missing; had critical mobile dark-mode contrast defect."
    ]
    for feat in p1_features:
        p = tf_p1.add_paragraph()
        p.text = f"• {feat}"
        p.font.size = Pt(12.5)
        p.font.color.rgb = c_navy
        p.space_before = Pt(12)

    # -------------------------------------------------------------
    # SLIDE 7: Users Told Us... & Evidence of Iteration (Prototype 2)
    # -------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "6. Users Told Us... So We Changed (Evidence of Iteration)")

    # Iteration table card
    table_shape = s7.shapes.add_table(rows=6, cols=3, left=Inches(0.8), top=Inches(2.0), width=Inches(11.733), height=Inches(4.8))
    table = table_shape.table
    table.columns[0].width = Inches(2.5)
    table.columns[1].width = Inches(4.4)
    table.columns[2].width = Inches(4.8)

    th = ["Stakeholder Feedback", "Observed Friction in Prototype 1", "Engineering Iteration in Prototype 2"]
    for j, h in enumerate(th):
        cell = table.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = c_navy
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = c_white

    iter_rows = [
        ("Riddhi (Resp. Tech)", "Dark-mode mobile phones rendered white text on white cards (invisible text).", "Locked .streamlit/config.toml to light base and applied !important dark navy CSS overrides."),
        ("Siddhi (Resp. Tech)", "Initial bank had only 2 questions per topic; insufficient for full 2-hour viva.", "Expanded question bank to 144 verified questions (exactly 12 in every topic)."),
        ("Naziya (Allied Health)", "Vivas are verbal, not multiple choice! Students freeze when asked to explain aloud.", "Engineered Quick Viva Mode: students type/draft answers and compare against reference models."),
        ("Bhargav (Anaesthesia)", "Students had to restart entire 20-question quiz just to review 2 missed mistakes.", "Engineered 1-Click Quick Retry Quiz isolating only incorrect questions for immediate retest."),
        ("Naveen (ICU Posting)", "Hospital basements have zero mobile network; app crashed if API key missing.", "Built Offline-First Knowledge Engine searching local verified records with zero crash risk.")
    ]
    for r_idx, (col0, col1, col2) in enumerate(iter_rows, start=1):
        for c_idx, val in enumerate([col0, col1, col2]):
            cell = table.cell(r_idx, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = c_light if r_idx % 2 == 1 else c_white
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(10)
            p.font.color.rgb = c_navy

    # -------------------------------------------------------------
    # SLIDE 8: Our Final Solution & Impact
    # -------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "7. Our Final Solution: MedSkill AI (Live Deployed Platform)")

    f_box = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(2.0), Inches(11.3), Inches(4.8))
    f_box.fill.solid()
    f_box.fill.fore_color.rgb = c_white
    f_box.line.color.rgb = c_border
    tf_f = f_box.text_frame
    tf_f.word_wrap = True
    tf_f.margin_left = tf_f.margin_right = tf_f.margin_top = Inches(0.5)

    p = tf_f.paragraphs[0]
    p.text = "MEDSKILL AI — PRODUCTION PLATFORM SUMMARY"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = c_teal

    final_bullets = [
        "Live Deployment: Hosted live on Streamlit Community Cloud at https://medskill-ai.streamlit.app/",
        "144 Reviewed Viva Questions: Balanced across 12 topics in Respiratory, Anaesthesia, and Dialysis technology (12 per topic).",
        "Dual-Mode Training: Seamlessly switch between Objective MCQ practice and Spoken Quick Viva self-evaluation.",
        "Instant Diagnostic Feedback: Detailed clinical explanations + expandable 'Key Viva Revision Points' buzzword cards.",
        "Targeted Remediation: Rule-based study recommendations with 1-click retry on missed items.",
        "Ethical & Operational Safety: 100% offline-first resilience; zero clinical prescribing; no patient data collected.",
        "Impact: Transforms passive textbook memorization into active verbal confidence for university clinical examinations."
    ]
    for fb in final_bullets:
        p = tf_f.add_paragraph()
        p.text = f"• {fb}"
        p.font.size = Pt(12)
        p.font.color.rgb = c_navy
        p.space_before = Pt(8)

    prs.save("MedSkill_AI_Final_Presentation.pptx")
    print("Saved MedSkill_AI_Final_Presentation.pptx successfully.")

if __name__ == "__main__":
    create_deck()
