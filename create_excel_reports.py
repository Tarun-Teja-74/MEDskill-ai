"""
Generator for:
1. MedSkill_AI_App_Review.xlsx
2. MedSkill_AI_Improvement_Tracker.xlsx
"""

import xlsxwriter

def create_app_review_excel():
    wb = xlsxwriter.Workbook('MedSkill_AI_App_Review.xlsx')
    
    # Formats
    header_fmt = wb.add_format({
        'bold': True, 'bg_color': '#0F172A', 'font_color': '#FFFFFF',
        'border': 1, 'align': 'center', 'valign': 'vcenter', 'text_wrap': True
    })
    sub_header = wb.add_format({
        'bold': True, 'bg_color': '#E2E8F0', 'font_color': '#0F172A',
        'border': 1, 'align': 'left', 'valign': 'vcenter'
    })
    cell_fmt = wb.add_format({'border': 1, 'valign': 'top', 'text_wrap': True})
    pass_fmt = wb.add_format({'border': 1, 'bg_color': '#DCFCE7', 'font_color': '#166534', 'bold': True, 'align': 'center'})
    partial_fmt = wb.add_format({'border': 1, 'bg_color': '#FEF3C7', 'font_color': '#92400E', 'bold': True, 'align': 'center'})
    fail_fmt = wb.add_format({'border': 1, 'bg_color': '#FEE2E2', 'font_color': '#991B1B', 'bold': True, 'align': 'center'})

    # -------------------------------------------------------------
    # SHEET 1: Functional Review (18 Features)
    # -------------------------------------------------------------
    ws1 = wb.add_worksheet('Functional_Review')
    ws1.set_column('A:A', 8)
    ws1.set_column('B:B', 22)
    ws1.set_column('C:C', 32)
    ws1.set_column('D:D', 34)
    ws1.set_column('E:E', 20)
    ws1.set_column('F:F', 14)
    ws1.set_column('G:G', 28)
    ws1.set_column('H:H', 30)
    ws1.set_column('I:I', 18)

    headers1 = [
        "Feature ID", "Feature Name", "Expected Behaviour", "Actual Observed Behaviour",
        "Test Method", "Result", "Issue Identified", "Suggested Improvement", "Evidence Reference"
    ]
    for col_idx, h in enumerate(headers1):
        ws1.write(0, col_idx, h, header_fmt)

    functional_data = [
        ("FR-01", "Home Dashboard", "Display brand title, specialty cards, question counts, and session stats.", "Header, metrics, and 3 specialty cards render with live question counter (144 available).", "Manual inspection on Chrome/Edge", "Passed", "None. Session metrics correctly initialize at 0 attempts.", "Add last active date or quick-start guide for first-time visitors.", "UI Code app.py L350-540"),
        ("FR-02", "Specialty Selection", "Clicking a specialty updates available topics and loads specialty metadata.", "Respiratory, Anaesthesia, and Dialysis buttons update session state and redirect smoothly.", "Click testing & state tracking", "Passed", "None. Metadata color badges and topic lists update dynamically.", "Add brief 1-sentence career role summary on each card.", "app.py L550-600"),
        ("FR-03", "Topic Selection", "Dropdown filters question pool to selected topic and displays live available count.", "Selecting any of 4 topics per specialty updates count to exactly 12 questions.", "Dropdown selection & state check", "Passed", "None. Topic counts correctly reflect questions.py.", "Show difficulty breakdown per topic directly in the summary card.", "app.py L610-660"),
        ("FR-04", "Question Loading", "Selected question set loads into active session array without index out-of-range errors.", "Questions load cleanly into active_question_list; progress bar reflects 1 to 12.", "Iterative navigation testing", "Passed", "Initial build lacked reset on mid-session switch.", "Prevent switching specialty mid-quiz without explicit user confirmation modal.", "app.py L670-710"),
        ("FR-05", "MCQ Practice Mode", "Render 4 distinct radio options; radio labels must be high-contrast and fully legible.", "Options render as rounded cards with bold navy text; no white-on-white text.", "Cross-browser dark/light mode check", "Passed", "Initial P1 build had white font on white background in dark mode.", "Fixed in P2 via .streamlit/config.toml and !important CSS overrides.", "Screenshot media_18ae0c6b.png"),
        ("FR-06", "Quick Viva Mode", "Provide text area for typing spoken answer and comparing against instructor model.", "User types answer; clicking 'Compare' displays model answer and key points checklist.", "Interactive text entry & submit", "Passed", "Does not perform NLP semantic grading (rule-based self-evaluation).", "Add clear disclaimer stating it is a self-evaluation checklist, not automated AI grading.", "app.py L790-850"),
        ("FR-07", "Answer Validation", "Check answer against correct_index; display clear immediate visual feedback.", "Correct selections trigger green alert; incorrect selections trigger red alert with correct key.", "Checked on all 144 items via automated script", "Passed", "Previous build placed Next Question button awkwardly beside Check Answer.", "Repositioned Next Question button below feedback box in vibrant blue.", "app.py L740-770"),
        ("FR-08", "Explanations & Revision", "Display concise physiological/equipment explanation and key viva talking points.", "Clinical explanation renders with an expandable 'Key Viva Revision Points' checklist.", "Content verification against textbooks", "Passed", "None. Explanations cite clinical principles directly.", "Add textbook chapter citation or page reference for further reading.", "questions.py metadata"),
        ("FR-09", "Score Calculation", "Calculate correct, incorrect, and accuracy percentage without duplicate counting.", "Scoring accurately increments; repeated clicks on Check Answer do not inflate score.", "Rapid re-click stress test", "Passed", "Initial version allowed duplicate counting on fast double-clicks.", "Added current_submitted boolean guard in session state.", "calculate_session_stats()"),
        ("FR-10", "Difficulty Filters", "Allow filtering by Beginner, Intermediate, or Advanced tiers.", "Filters pool to matching difficulty; displays difficulty badge on question card.", "Filter combination testing", "Passed", "Filtering by narrow topic + advanced may yield 0 questions if too restrictive.", "Display warning message suggesting 'All Difficulties' when zero matches found.", "app.py L630-650"),
        ("FR-11", "Weak-Topic Identification", "Track topics where user made errors and display targeted breakdown in Results.", "Results page lists all attempted topics with total, correct, missed, and % accuracy.", "Completed 5 mock quizzes with errors", "Passed", "Only activates after completing scored MCQ questions.", "Add indicator on dashboard highlighting topics that need revision.", "app.py L870-940"),
        ("FR-12", "Retry Missed Questions", "Provide a 1-click retry quiz loading only questions the user answered incorrectly.", "'Quick Retry Missed Questions Only' button filters active pool and restarts quiz seamlessly.", "Error injection & retry test", "Passed", "Initial build forced users to restart the entire 12-question set.", "Solved in P2 with 1-click retry engine deleting prior incorrect keys.", "app.py L960-990"),
        ("FR-13", "AI Concept Tutor", "Allow users to ask viva questions and receive simplified educational explanations.", "Generates 150-250 word structured explanations with beginner-friendly definitions.", "Live prompt testing on ventilator & gas physics", "Partially working", "Online LLM requires external API key; defaults to local retrieval when offline.", "Add visual badge clarifying whether output is from live LLM or local knowledge base.", "query_optional_ai()"),
        ("FR-14", "Offline Fallback", "Function seamlessly without crashing when GEMINI_API_KEY / OPENAI_API_KEY is missing.", "Local knowledge engine searches 144 verified curriculum records and returns matching rationale.", "Simulated missing keys & offline run", "Passed", "Initial build threw StreamlitSecretNotFoundError when secrets.toml was missing.", "Added get_secret() safe exception-wrapped helper function.", "app.py L240-270"),
        ("FR-15", "Session Reset", "Provide 1-click reset clearing all session attempts and score variables.", "Sidebar 'Reset Current Session' clears session_answers, active_list, and resets to Home.", "Button trigger & state audit", "Passed", "None. Resets cleanly without requiring browser page reload.", "Add confirmation prompt to prevent accidental loss of active quiz progress.", "app.py L320-335"),
        ("FR-16", "Error Handling", "Handle empty inputs, invalid question IDs, and missing keys gracefully.", "Empty viva text inputs show warning; missing keys use local fallback; 0/0 accuracy handles cleanly.", "Edge-case boundary testing", "Passed", "Zero division risk in accuracy calculation.", "Protected with (correct + incorrect) > 0 conditional check.", "calculate_session_stats()"),
        ("FR-17", "Responsive Layout", "Render legibly across laptop, tablet, and smartphone screen viewports.", "Single-column stack on mobile; sidebar collapses into hamburger menu; readable typography.", "Tested on iPhone Safari & desktop Chrome", "Passed", "Table in Design Thinking tab requires horizontal scroll on narrow mobile screens.", "Convert multi-column comparison tables into stacked card layouts on mobile.", "Viewport audit at 375px"),
        ("FR-18", "Educational Disclaimer", "State clearly that application is an educational prototype and not clinical decision support.", "Prominent disclaimer present in sidebar footer, Ask MedSkill AI page, and README.", "Compliance audit against medical software norms", "Passed", "None. Strictly positioned as a student viva preparation prototype.", "Ensure disclaimer remains visible on print-outs or exported revision sheets.", "Footer & headers")
    ]

    for row_idx, row_data in enumerate(functional_data, start=1):
        for col_idx, val in enumerate(row_data):
            if col_idx == 5:
                fmt = pass_fmt if val == "Passed" else (partial_fmt if val == "Partially working" else fail_fmt)
                ws1.write(row_idx, col_idx, val, fmt)
            else:
                ws1.write(row_idx, col_idx, val, cell_fmt)

    # -------------------------------------------------------------
    # SHEET 2: Usability Review (13 Criteria)
    # -------------------------------------------------------------
    ws2 = wb.add_worksheet('Usability_Review')
    ws2.set_column('A:A', 8)
    ws2.set_column('B:B', 24)
    ws2.set_column('C:C', 35)
    ws2.set_column('D:D', 15)
    ws2.set_column('E:E', 35)
    ws2.set_column('F:F', 30)

    headers2 = ["ID", "Usability Question", "Evaluation Criteria", "Status", "Observed User Behavior", "Recommendation"]
    for col_idx, h in enumerate(headers2):
        ws2.write(0, col_idx, h, header_fmt)

    usability_data = [
        ("UR-01", "App Purpose Clarity", "Is the educational purpose immediately clear on landing?", "Passed", "Header banner 'Practice. Understand. Improve.' conveys function within 5 seconds.", "Maintain simple student-focused tagline without jargon."),
        ("UR-02", "Specialty Identification", "Can students find their healthcare discipline effortlessly?", "Passed", "Three large cards with color badges (Cyan, Blue, Green) make choice immediate.", "Add specialty icons to increase visual recognition."),
        ("UR-03", "Topic Hierarchy", "Are curriculum topics grouped logically?", "Passed", "Topics match recognized B.Sc. Allied Health university syllabus structure.", "Ensure topic names match exact semester paper nomenclature."),
        ("UR-04", "Mode Distinction", "Is difference between MCQ and Quick Viva obvious?", "Passed", "Help tooltip and radio labels clarify objective vs spoken comparison modes.", "Add a 10-second illustrated example GIF on the selection screen."),
        ("UR-05", "Legibility & Typography", "Are questions and options comfortable to read?", "Passed", "Font size 1.25rem for questions; options styled as distinct white cards with navy text.", "Resolved earlier contrast defect observed in dark-mode browser."),
        ("UR-06", "Feedback Timing", "Is feedback presented synchronously upon submission?", "Passed", "Feedback renders instantaneously upon Check Answer without page jump.", "Keep feedback anchored adjacent to the selected option."),
        ("UR-07", "Explanation Conciseness", "Are rationales concise (< 150 words) and high-yield?", "Passed", "Explanations explain physical laws (Bernoulli, Laplace, Fick) in 2-3 focused sentences.", "Key points expander separates quick buzzwords from full explanations."),
        ("UR-08", "Score vs Learning Progress", "Can students distinguish session score from understanding?", "Passed", "Distinguishes between MCQ score and un-scored Quick Viva self-evaluations.", "Add separate counter for 'Viva Cards Reviewed' alongside MCQ accuracy."),
        ("UR-09", "Weak Topic Discoverability", "Are weak areas prominent after practice?", "Passed", "Results page renders color-coded topic cards (Green >=70%, Amber 50-69%, Red <50%).", "Include direct link to open relevant revision notes from the card."),
        ("UR-10", "Error Message Clarity", "Are empty inputs and missing states communicated politely?", "Passed", "Empty text area in Quick Viva prompts: 'Please type a brief response before comparing.'", "Avoid generic system alert codes; keep messages supportive."),
        ("UR-11", "Small Screen Usability", "Does layout remain functional on mobile phones?", "Passed", "Vertical responsive flow; buttons stretch to container width for easy tapping.", "Ensure expander click targets are at least 48px high for thumb touch."),
        ("UR-12", "Zero-Key Accessibility", "Can students use core features with no API credentials?", "Passed", "100% of the 144-question bank, scoring, and local search works offline without keys.", "Prominently display 'Offline-First Verified Mode' badge."),
        ("UR-13", "Educational Limitations", "Is clinical prototype disclaimer noticeable?", "Passed", "Clear warning labels: 'Educational prototype - Not for clinical decision support.'", "Maintain visible boundary separating college revision from hospital diagnosis.")
    ]

    for row_idx, row_data in enumerate(usability_data, start=1):
        for col_idx, val in enumerate(row_data):
            if col_idx == 3:
                ws2.write(row_idx, col_idx, val, pass_fmt if val == "Passed" else partial_fmt)
            else:
                ws2.write(row_idx, col_idx, val, cell_fmt)

    # -------------------------------------------------------------
    # SHEET 3: Content Review (12 Topics / 144 Questions)
    # -------------------------------------------------------------
    ws3 = wb.add_worksheet('Content_Review')
    ws3.set_column('A:A', 6)
    ws3.set_column('B:B', 22)
    ws3.set_column('C:C', 32)
    ws3.set_column('D:D', 14)
    ws3.set_column('E:E', 18)
    ws3.set_column('F:F', 20)
    ws3.set_column('G:G', 35)

    headers3 = ["S.No", "Specialty", "Topic Name", "Total Questions", "Difficulty Spread", "Answer Key Status", "Curriculum Focus Areas"]
    for col_idx, h in enumerate(headers3):
        ws3.write(0, col_idx, h, header_fmt)

    content_data = [
        (1, "Respiratory Therapy", "Respiratory anatomy and physiology", 12, "3 Beg / 5 Int / 4 Adv", "100% Verified (0 errors)", "Vd/Vt, Oxy-Hb curve shifts, PAO2 alveolar equation, FRC, West Zones, HPV, CO2 transport, Fowler dead space."),
        (2, "Respiratory Therapy", "Oxygen therapy", 12, "4 Beg / 5 Int / 3 Adv", "100% Verified (0 errors)", "Simple mask washout, Venturi Bernoulli principle, Rule of 4, NRB valves, HFNC dead space, Thorpe tube compensation."),
        (3, "Respiratory Therapy", "Ventilator fundamentals", 12, "3 Beg / 5 Int / 4 Adv", "100% Verified (0 errors)", "PEEP mechanics, Ppeak vs Pplat resistance, static compliance, volume cycling, Auto-PEEP hold, ARDSNet protocol."),
        (4, "Respiratory Therapy", "Respiratory equipment", 12, "4 Beg / 5 Int / 3 Adv", "100% Verified (0 errors)", "HME filters, vibrating mesh nebulizers, ETT cuff manometer (20-30 cmH2O), closed suction, peak flow meters, Wright respirometer."),
        (5, "Anaesthesia Technology", "Anaesthesia equipment identification", 12, "3 Beg / 5 Int / 4 Adv", "100% Verified (0 errors)", "Soda lime reactions, bimetallic vaporizer strip, Desflurane Tec 6, LMA ProSeal, Macintosh vs Miller, videolaryngoscopes, DLTs."),
        (6, "Anaesthesia Technology", "Basic machine components", 12, "4 Beg / 5 Int / 3 Adv", "100% Verified (0 errors)", "O2 flush valve bypass (35-75 L/min), APL valve, rotameter float reading, Common Gas Outlet ISO, Selectatec interlock, Link-25 guard."),
        (7, "Anaesthesia Technology", "Equipment safety checks", 12, "3 Beg / 5 Int / 4 Adv", "100% Verified (0 errors)", "Pin Index Safety System (PISS), fail-safe valve, DISS, negative pressure bulb check, O2 analyzer 2-point calibration, Compound A risk."),
        (8, "Anaesthesia Technology", "Monitoring fundamentals", 12, "3 Beg / 5 Int / 4 Adv", "100% Verified (0 errors)", "Capnography Phases I-0, dual wavelength SpO2 (660/940 nm), PetCO2 loss algorithm, shark fin waveform, TOF ratio >= 0.90, BIS target."),
        (9, "Dialysis Technology", "Principles of hemodialysis", 12, "4 Beg / 4 Int / 4 Adv", "100% Verified (0 errors)", "Fick's diffusion kinetics, TMP ultrafiltration, convective clearance, clearance K formula, KoA, high-flux criteria, single-pool Kt/V."),
        (10, "Dialysis Technology", "Dialysis machine components", 12, "4 Beg / 5 Int / 3 Adv", "100% Verified (0 errors)", "Counter-current dialyzer flow, peristaltic roller pump, conductivity cell (13.5-14.5 mS/cm), dialysate heater (35.5-37C), deaerator."),
        (11, "Dialysis Technology", "Basic alarm recognition", 12, "3 Beg / 5 Int / 4 Adv", "100% Verified (0 errors)", "Venous air bubble detector, optical blood leak detector, high venous pressure kinks, low venous disconnect, hypotonic hemolysis hazard."),
        (12, "Dialysis Technology", "Infection prevention and equipment safety", 12, "3 Beg / 5 Int / 4 Adv", "100% Verified (0 errors)", "AV fistula physical exam (Look/Feel/Listen), total chlorine testing (<0.1 mg/L), RO rejection >=95%, AAMI standards, peracetic acid reuse.")
    ]

    for row_idx, row_data in enumerate(content_data, start=1):
        for col_idx, val in enumerate(row_data):
            if col_idx == 5:
                ws3.write(row_idx, col_idx, val, pass_fmt)
            else:
                ws3.write(row_idx, col_idx, val, cell_fmt)

    # -------------------------------------------------------------
    # SHEET 4: AI Feature Review
    # -------------------------------------------------------------
    ws4 = wb.add_worksheet('AI_Feature_Review')
    ws4.set_column('A:A', 8)
    ws4.set_column('B:B', 24)
    ws4.set_column('C:C', 35)
    ws4.set_column('D:D', 35)
    ws4.set_column('E:E', 15)
    ws4.set_column('F:F', 30)

    headers4 = ["ID", "AI Dimension", "Evaluation Criteria", "Observed Behavior", "Status", "Technical Note / Guardrail"]
    for col_idx, h in enumerate(headers4):
        ws4.write(0, col_idx, h, header_fmt)

    ai_data = [
        ("AI-01", "Online LLM Integration", "Connects to Google Gemini or OpenAI when API key is provided.", "Sends prompt with strict educational persona; returns structured explanation in < 3 seconds.", "Passed", "API key read safely via get_secret() without hardcoding."),
        ("AI-02", "Offline Fallback", "Gracefully falls back to local knowledge retrieval when no API key exists.", "Performs keyword relevance matching across 144 questions and returns exact verified explanation.", "Passed", "Zero crashes when running offline or without credentials."),
        ("AI-03", "Educational Guardrails", "Never prescribes real treatments, gives patient diagnosis, or configures patient settings.", "Prompt explicitly commands: 'Explain technical terms in beginner-friendly language. No clinical prescribing.'", "Passed", "System disclaimer permanently visible beneath output."),
        ("AI-04", "Attribution Transparency", "Distinguishes between textbook reference content and generative AI output.", "Appends explicit source tag: '(Source: Gemini Educational Engine)' or 'Verified Curriculum Match'.", "Passed", "Prevents students from confusing AI approximations with syllabus facts."),
        ("AI-05", "Scope Boundary", "Restricts responses to allied health equipment physics and physiological principles.", "Answers focus on device physics (PISS, Bernoulli, TMP, PEEP) and standard clinical calculations.", "Passed", "Out-of-scope queries gracefully directed back to specialty study menus.")
    ]

    for row_idx, row_data in enumerate(ai_data, start=1):
        for col_idx, val in enumerate(row_data):
            if col_idx == 4:
                ws4.write(row_idx, col_idx, val, pass_fmt)
            else:
                ws4.write(row_idx, col_idx, val, cell_fmt)

    wb.close()
    print("Created MedSkill_AI_App_Review.xlsx successfully.")


def create_improvement_tracker_excel():
    wb = xlsxwriter.Workbook('MedSkill_AI_Improvement_Tracker.xlsx')
    
    header_fmt = wb.add_format({
        'bold': True, 'bg_color': '#1E293B', 'font_color': '#FFFFFF',
        'border': 1, 'align': 'center', 'valign': 'vcenter', 'text_wrap': True
    })
    cell_fmt = wb.add_format({'border': 1, 'valign': 'top', 'text_wrap': True})
    high_fmt = wb.add_format({'border': 1, 'bg_color': '#FEE2E2', 'font_color': '#991B1B', 'bold': True, 'align': 'center'})
    med_fmt = wb.add_format({'border': 1, 'bg_color': '#FEF3C7', 'font_color': '#92400E', 'bold': True, 'align': 'center'})
    low_fmt = wb.add_format({'border': 1, 'bg_color': '#E0F2FE', 'font_color': '#0369A1', 'bold': True, 'align': 'center'})
    done_fmt = wb.add_format({'border': 1, 'bg_color': '#DCFCE7', 'font_color': '#166534', 'bold': True, 'align': 'center'})

    ws = wb.add_worksheet('Prioritized_Improvements')
    ws.set_column('A:A', 10)
    ws.set_column('B:B', 24)
    ws.set_column('C:C', 30)
    ws.set_column('D:D', 12)
    ws.set_column('E:E', 14)
    ws.set_column('F:F', 12)
    ws.set_column('G:G', 32)
    ws.set_column('H:H', 25)
    ws.set_column('I:I', 14)

    headers = [
        "Issue ID", "Stakeholder Evidence", "Identified Problem", "Severity",
        "Priority", "Effort", "Proposed / Implemented Change", "Verification Method", "Status"
    ]
    for col_idx, h in enumerate(headers):
        ws.write(0, col_idx, h, header_fmt)

    tracker_data = [
        ("IMP-01", "User Riddhi & screenshot media_18ae0c6b.png", "White text rendering on light background when mobile/OS is in dark mode.", "High", "Critical", "Low", "Enforced light theme in .streamlit/config.toml and forced dark navy text via !important CSS.", "Visual audit on mobile device with dark mode enabled.", "Implemented (P2)"),
        ("IMP-02", "User Siddhi & Tharun", "Initial question bank had only 24 questions (2 per topic), insufficient for exam prep.", "High", "High", "Medium", "Expanded question bank to exactly 12 questions in EVERY topic (144 questions total).", "Automated validation in test_medskill.py asserting 12 per topic.", "Implemented (P2)"),
        ("IMP-03", "User Naziya & clinical instructors", "Examiners conduct verbal vivas, but application only offered multiple-choice options.", "Medium", "High", "Medium", "Engineered 'Quick Viva Mode' allowing students to type answers and compare against reference model.", "Usability test with 5 students comparing against instructor standard.", "Implemented (P2)"),
        ("IMP-04", "User Bhargav & Atharv", "Users had to restart entire quiz to review 2 missed questions; no targeted retry.", "Medium", "High", "Low", "Added 1-click '⚡ Quick Retry Quiz' button that filters active set to only missed questions.", "Functional test verifying active list length matches missed count.", "Implemented (P2)"),
        ("IMP-05", "User Preethi", "Next Question button rendered beside Check Answer above the explanation, causing confusion.", "Medium", "Medium", "Low", "Relocated Next Question button below feedback and expander card with vibrant blue styling.", "Layout audit ensuring logical top-to-bottom reading sequence.", "Implemented (P2)"),
        ("IMP-06", "User Naveen (ICU posting)", "Hospital basements have no mobile reception; app crashed if API key missing.", "High", "Critical", "Medium", "Built local semantic keyword retrieval fallback in query_optional_ai() with zero crash risk.", "Executed app without GEMINI_API_KEY and verified response.", "Implemented (P2)"),
        ("IMP-07", "User Tharun", "First-year juniors found advanced ventilator equations intimidating without difficulty guidance.", "Low", "Medium", "Low", "Added Beginner, Intermediate, and Advanced difficulty badges and filter dropdown.", "Tested difficulty filtering across all 3 specialties.", "Implemented (P2)"),
        ("IMP-08", "User Atharv", "Students needed concise bullet points rather than long paragraphs right before entering viva.", "Low", "Medium", "Low", "Added expandable '📌 Key Viva Revision Points' card to every single question.", "Verified all 144 questions contain >= 3 bullet points.", "Implemented (P2)"),
        ("IMP-09", "Proposed (Future Phase)", "Students cannot track long-term improvement across multiple days without login.", "Low", "Low", "High", "Introduce optional local browser localStorage or lightweight SQLite profile persistence.", "User study measuring retention over 14-day study period.", "Proposed (P3)"),
        ("IMP-10", "Proposed (Future Phase)", "Students wish to speak oral answers instead of typing on mobile keypad.", "Low", "Low", "High", "Integrate browser Web Speech API for voice-to-text dictation in Quick Viva mode.", "Speech accuracy test in hospital environment with ambient noise.", "Proposed (P3)")
    ]

    for row_idx, row_data in enumerate(tracker_data, start=1):
        for col_idx, val in enumerate(row_data):
            if col_idx == 3:
                ws.write(row_idx, col_idx, val, high_fmt if val == "High" else (med_fmt if val == "Medium" else low_fmt))
            elif col_idx == 4:
                ws.write(row_idx, col_idx, val, high_fmt if val in ["Critical", "High"] else med_fmt)
            elif col_idx == 8:
                ws.write(row_idx, col_idx, val, done_fmt if "Implemented" in val else med_fmt)
            else:
                ws.write(row_idx, col_idx, val, cell_fmt)

    wb.close()
    print("Created MedSkill_AI_Improvement_Tracker.xlsx successfully.")

if __name__ == "__main__":
    create_app_review_excel()
    create_improvement_tracker_excel()
