"""
MedSkill AI - AI-Powered Practical Viva Trainer
Academic Prototype for Healthcare Technology Students:
- Respiratory Therapy
- Anaesthesia Technology
- Dialysis Technology

Built with Python and Streamlit.
"""

import os
import json
import streamlit as st
from questions import (
    QUESTIONS_DATA,
    SPECIALTIES,
    TOPICS_BY_SPECIALTY,
    SPECIALTY_METADATA,
    get_questions_for_specialty,
    get_question_by_id,
    get_all_revision_notes_for_topic,
)
from cram_sheet_generator import generate_pocket_cram_sheet

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION & CUSTOM STYLING
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="MedSkill AI — Practical Viva Trainer",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# High-contrast academic styling ensuring crisp, legible text across all themes
st.markdown(
    """
    <style>
    /* =========================================================================
       GLOBAL APP & TYPOGRAPHY - HIGH CONTRAST (PREVENTS WHITE-ON-WHITE FONT)
       ========================================================================= */
    .stApp {
        background-color: #F8FAFC !important;
        color: #0F172A !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Enforce dark navy font on all general text elements */
    .stApp p, .stApp span, .stApp label, .stApp div, .stApp li {
        color: #0F172A;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #0F172A !important;
        font-weight: 700 !important;
    }

    /* =========================================================================
       SIDEBAR - EXPLICIT HIGH CONTRAST
       ========================================================================= */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E2E8F0 !important;
    }
    
    section[data-testid="stSidebar"] * {
        color: #0F172A !important;
    }
    
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] h4 {
        color: #0F172A !important;
    }
    
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span {
        color: #0F172A !important;
    }
    
    section[data-testid="stSidebar"] .stCaption,
    section[data-testid="stSidebar"] .stCaption * {
        color: #475569 !important;
    }
    
    /* Sidebar Navigation Radio Items */
    section[data-testid="stSidebar"] div[data-testid="stRadio"] label,
    section[data-testid="stSidebar"] div[data-testid="stRadio"] label * {
        color: #0F172A !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
    }

    /* =========================================================================
       MCQ RADIO OPTIONS - CRISP CARDS WITH VISIBLE TEXT
       ========================================================================= */
    div[data-testid="stRadio"] {
        margin-top: 0.5rem;
    }

    /* Radio group container and options */
    div[data-testid="stRadio"] label[data-baseweb="radio"] {
        background-color: #FFFFFF !important;
        border: 1.5px solid #CBD5E1 !important;
        border-radius: 8px !important;
        padding: 0.65rem 1rem !important;
        margin-bottom: 0.5rem !important;
        cursor: pointer !important;
        transition: all 0.15s ease-in-out !important;
        display: flex !important;
        align-items: center !important;
    }

    div[data-testid="stRadio"] label[data-baseweb="radio"]:hover {
        border-color: #0284C7 !important;
        background-color: #F0F9FF !important;
    }

    /* Force MCQ option text to always be dark navy (#0F172A) */
    div[data-testid="stRadio"] label[data-baseweb="radio"] p,
    div[data-testid="stRadio"] label[data-baseweb="radio"] span,
    div[data-testid="stRadio"] label[data-baseweb="radio"] div {
        color: #0F172A !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
    }

    /* Widget Labels */
    label[data-testid="stWidgetLabel"] p,
    label[data-testid="stWidgetLabel"] span {
        color: #0F172A !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }

    /* =========================================================================
       TOP BANNER / HEADER CARDS
       ========================================================================= */
    .brand-header {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1.5rem 1.75rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.05);
    }
    
    .brand-title {
        font-size: 1.85rem;
        font-weight: 700;
        color: #0F172A !important;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .brand-subtitle {
        color: #0D9488 !important;
        font-weight: 600;
        font-size: 1.05rem;
        margin-top: 0.25rem;
    }
    
    .brand-desc {
        color: #475569 !important;
        font-size: 0.95rem;
        margin-top: 0.5rem;
        line-height: 1.5;
    }
    
    /* Card design */
    .med-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 1.25rem;
        margin-bottom: 1rem;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
        box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04);
    }
    
    .med-card:hover {
        border-color: #CBD5E1;
        box-shadow: 0 4px 6px -1px rgba(15, 23, 42, 0.08);
    }

    .med-card * {
        color: #0F172A;
    }
    
    /* Badges */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.65rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.025em;
    }
    
    .badge-specialty {
        background-color: #E0F2FE !important;
        color: #0369A1 !important;
    }
    
    .badge-topic {
        background-color: #F1F5F9 !important;
        color: #334155 !important;
    }
    
    .badge-beginner {
        background-color: #DCFCE7 !important;
        color: #15803D !important;
    }
    
    .badge-intermediate {
        background-color: #FEF3C7 !important;
        color: #B45309 !important;
    }
    
    .badge-advanced {
        background-color: #FEE2E2 !important;
        color: #B91C1C !important;
    }

    /* Explanation & Key point boxes */
    .info-box {
        background-color: #F0FDF4 !important;
        border: 1px solid #86EFAC !important;
        border-left: 5px solid #16A34A !important;
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin-top: 1rem;
        color: #14532D !important;
    }

    .info-box * {
        color: #14532D !important;
    }
    
    .warning-box {
        background-color: #FEF2F2 !important;
        border: 1px solid #FECACA !important;
        border-left: 5px solid #DC2626 !important;
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin-top: 1rem;
        color: #7F1D1D !important;
    }

    .warning-box * {
        color: #7F1D1D !important;
    }

    .viva-box {
        background-color: #F8FAFC !important;
        border: 1.5px solid #CBD5E1 !important;
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin-top: 0.75rem;
    }

    .viva-box * {
        color: #0F172A !important;
    }
    
    /* Metrics */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 8px !important;
        padding: 0.75rem 1rem !important;
        box-shadow: 0 1px 2px rgba(0,0,0,0.03) !important;
    }

    div[data-testid="stMetricLabel"] p {
        color: #475569 !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
    }

    div[data-testid="stMetricValue"] div {
        color: #0F172A !important;
        font-weight: 700 !important;
        font-size: 1.6rem !important;
    }

    /* =========================================================================
       EXPANDERS (Key Revision Notes)
       ========================================================================= */
    div[data-testid="stExpander"] {
        background-color: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 8px !important;
        margin-top: 1rem !important;
    }

    div[data-testid="stExpander"] summary {
        background-color: #F8FAFC !important;
        border-radius: 8px !important;
        padding: 0.65rem 1rem !important;
    }

    div[data-testid="stExpander"] summary * {
        color: #0F172A !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }

    div[data-testid="stExpander"] div[data-testid="stExpanderDetails"] {
        background-color: #FFFFFF !important;
        padding: 1rem 1.25rem !important;
    }

    div[data-testid="stExpander"] div[data-testid="stExpanderDetails"] * {
        color: #1E293B !important;
        font-size: 0.95rem !important;
    }
    
    /* =========================================================================
       BUTTONS - CLEAR CONTRAST
       ========================================================================= */
    .stButton > button {
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        padding: 0.5rem 1rem !important;
        transition: all 0.15s ease !important;
    }

    /* Primary action buttons: bold blue with clean white font */
    .stButton > button[kind="primary"],
    .stButton > button:focus:not(:focus-visible) {
        background-color: #0284C7 !important;
        color: #FFFFFF !important;
        border: none !important;
    }

    .stButton > button[kind="primary"]:hover {
        background-color: #0369A1 !important;
        color: #FFFFFF !important;
    }

    /* Secondary buttons: clean light gray with dark navy font */
    .stButton > button[kind="secondary"],
    .stButton > button:not([kind="primary"]) {
        background-color: #F1F5F9 !important;
        color: #0F172A !important;
        border: 1.5px solid #CBD5E1 !important;
    }

    .stButton > button[kind="secondary"]:hover,
    .stButton > button:not([kind="primary"]):hover {
        background-color: #E2E8F0 !important;
        color: #0F172A !important;
        border-color: #94A3B8 !important;
    }

    /* =========================================================================
       INPUTS, SELECTS & TEXT AREAS
       ========================================================================= */
    input, textarea, select {
        color: #0F172A !important;
        background-color: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
    }

    div[data-baseweb="select"] * {
        color: #0F172A !important;
    }

    div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# SESSION STATE INITIALIZATION
# -----------------------------------------------------------------------------
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home Dashboard"

if "selected_specialty" not in st.session_state:
    st.session_state.selected_specialty = "Respiratory Therapy"

if "selected_topic" not in st.session_state:
    st.session_state.selected_topic = "All Topics"

if "selected_difficulty" not in st.session_state:
    st.session_state.selected_difficulty = "All Difficulties"

if "practice_mode" not in st.session_state:
    st.session_state.practice_mode = "MCQ Practice"

if "active_question_list" not in st.session_state:
    st.session_state.active_question_list = []

if "current_question_idx" not in st.session_state:
    st.session_state.current_question_idx = 0

# Record answers for current session: {question_id: dict(selected_index, is_correct, student_viva, reviewed)}
if "session_answers" not in st.session_state:
    st.session_state.session_answers = {}

# Submitted status for current question (prevents double-counting)
if "current_submitted" not in st.session_state:
    st.session_state.current_submitted = False

# Feedback state for current question
if "current_feedback" not in st.session_state:
    st.session_state.current_feedback = None

# Examiner Pressure Mode (30-second rapid countdown timer)
if "examiner_timer_enabled" not in st.session_state:
    st.session_state.examiner_timer_enabled = False


# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------
def navigate_to(page_name: str):
    """Change the current active page."""
    st.session_state.current_page = page_name
    st.rerun()


def reset_practice_session(questions_list):
    """Initialize a new practice quiz session with specified questions."""
    st.session_state.active_question_list = questions_list
    st.session_state.current_question_idx = 0
    st.session_state.current_submitted = False
    st.session_state.current_feedback = None


def calculate_session_stats():
    """Calculate attempted, correct, incorrect, and accuracy from current session."""
    total_available = len(QUESTIONS_DATA)
    answers = st.session_state.session_answers
    attempted = len(answers)
    correct = sum(1 for a in answers.values() if a.get("is_correct") is True)
    incorrect = sum(1 for a in answers.values() if a.get("is_correct") is False)
    reviewed_viva = sum(1 for a in answers.values() if a.get("is_correct") is None)
    
    accuracy = (correct / (correct + incorrect) * 100) if (correct + incorrect) > 0 else 0.0
    return {
        "total_available": total_available,
        "attempted": attempted,
        "correct": correct,
        "incorrect": incorrect,
        "reviewed_viva": reviewed_viva,
        "accuracy": accuracy,
    }


def get_secret(key_name: str):
    """Safely fetch secret from env or Streamlit secrets without raising StreamlitSecretNotFoundError."""
    val = os.getenv(key_name)
    if val:
        return val
    try:
        # Check if secrets file exists or is loaded safely
        if hasattr(st, "secrets"):
            return st.secrets.get(key_name, None)
    except Exception:
        pass
    return None


def query_optional_ai(user_prompt: str, specialty: str) -> str:
    """
    Query optional LLM API if key is present; otherwise fall back to local knowledge retrieval.
    Never crashes when API key is missing.
    """
    # Check secrets or environment safely
    gemini_key = get_secret("GEMINI_API_KEY")
    openai_key = get_secret("OPENAI_API_KEY")

    # If an API key is configured, use it with structured educational guardrails
    if gemini_key:
        try:
            import requests
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={gemini_key}"
            payload = {
                "contents": [{
                    "parts": [{
                        "text": (
                            f"You are MedSkill AI, an educational practical viva tutor for healthcare technology students in {specialty}. "
                            "Explain technical terms in beginner-friendly language with clear short examples. "
                            "Do not diagnose patients, prescribe real treatments, or give unverified clinical advice. "
                            "Emphasize practical viva understanding and equipment physics/principles. "
                            "Keep your response concise (under 250 words).\n\n"
                            f"Student Question: {user_prompt}"
                        )
                    }]
                }]
            }
            resp = requests.post(url, json=payload, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                text = data["candidates"][0]["content"]["parts"][0]["text"]
                return text + "\n\n*(Source: Gemini Educational Engine — verify against your syllabus & instructor)*"
        except Exception:
            pass  # Fall back to offline knowledge engine

    if openai_key:
        try:
            import requests
            url = "https://api.openai.com/v1/chat/completions"
            headers = {"Authorization": f"Bearer {openai_key}", "Content-Type": "application/json"}
            payload = {
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": f"You are MedSkill AI, an educational viva tutor for {specialty} students. Keep explanations clear, beginner-friendly, and educational. No clinical prescribing."},
                    {"role": "user", "content": user_prompt}
                ],
                "max_tokens": 300
            }
            resp = requests.post(url, headers=headers, json=payload, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                text = data["choices"][0]["message"]["content"]
                return text + "\n\n*(Source: OpenAI Educational API — verify against your syllabus)*"
        except Exception:
            pass  # Fall back to offline knowledge engine

    # Local Knowledge Retrieval (Offline Mode - verified reviewed data)
    q_words = set(user_prompt.lower().replace("?", "").replace(",", "").split())
    scored = []
    for q in QUESTIONS_DATA:
        # Score relevance based on specialty match and word overlap
        spec_boost = 3 if q["specialty"].lower() in specialty.lower() else 0
        text_corpus = f"{q['question']} {q['topic']} {' '.join(q['key_points'])} {q['explanation']}".lower()
        match_count = sum(1 for w in q_words if len(w) > 3 and w in text_corpus)
        total_score = spec_boost + match_count
        if total_score > 1:
            scored.append((total_score, q))

    scored.sort(key=lambda x: x[0], reverse=True)

    if scored:
        best_match = scored[0][1]
        response = (
            f"**Verified Curriculum Match ({best_match['topic']} — {best_match['specialty']}):**\n\n"
            f"{best_match['explanation']}\n\n"
            f"**Key Viva Concepts:**\n"
            + "\n".join([f"- {pt}" for pt in best_match.get("key_points", [])])
            + f"\n\n*Reference Sample Viva Answer:*\n> \"{best_match.get('sample_viva_answer')}\""
        )
        return response
    else:
        return (
            "**MedSkill AI Local Knowledge Engine:**\n\n"
            "This concept is part of the allied health technology practical curriculum. "
            "To review this area, select the relevant specialty in the **Select Specialty & Topic** menu "
            "or refer to standard clinical engineering and technology manuals. "
            "\n\n*Tip: Try querying key terms like 'PEEP', 'Venturi', 'Pin Index', 'APL valve', 'dialysis diffusion', or 'blood leak alarm'.*"
        )


# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION & SESSION METRICS
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🩺 MedSkill AI")
    st.caption("AI-Powered Practical Viva Trainer")
    st.markdown("---")
    
    pages = [
        "Home Dashboard",
        "Select Specialty & Topic",
        "Viva Practice",
        "Results & Feedback",
        "Study Recommendations",
        "Ask MedSkill AI",
        "Design Thinking Portfolio"
    ]
    
    selected_nav = st.radio(
        "Navigation",
        options=pages,
        index=pages.index(st.session_state.current_page) if st.session_state.current_page in pages else 0,
        label_visibility="collapsed"
    )
    
    if selected_nav != st.session_state.current_page:
        st.session_state.current_page = selected_nav
        st.rerun()

    st.markdown("---")
    st.markdown("#### 📊 Session Overview")
    stats = calculate_session_stats()
    
    col_sb1, col_sb2 = st.columns(2)
    with col_sb1:
        st.metric("Attempted", f"{stats['attempted']}")
    with col_sb2:
        st.metric("Score", f"{stats['correct']}")
    
    if (stats['correct'] + stats['incorrect']) > 0:
        st.caption(f"Session Accuracy: **{stats['accuracy']:.1f}%**")
        st.progress(stats['accuracy'] / 100.0)
    else:
        st.caption("No scored MCQs completed yet.")

    st.markdown("---")
    if st.button("🔄 Reset Current Session", use_container_width=True, help="Clears attempts and restarts fresh"):
        st.session_state.session_answers = {}
        st.session_state.active_question_list = []
        st.session_state.current_question_idx = 0
        st.session_state.current_submitted = False
        st.session_state.current_feedback = None
        st.session_state.current_page = "Home Dashboard"
        st.success("Session reset.")
        st.rerun()

    st.markdown(
        """
        <div style="font-size: 0.75rem; color: #64748B; margin-top: 2rem;">
        Educational prototype for college viva preparation.<br>
        Not a clinical decision support system.
        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------------------------------------------------------
# PAGE 1: HOME DASHBOARD
# -----------------------------------------------------------------------------
if st.session_state.current_page == "Home Dashboard":
    # Header Banner
    st.markdown(
        """
        <div class="brand-header">
            <h1 class="brand-title">🩺 MedSkill AI</h1>
            <div class="brand-subtitle">Practice. Understand. Improve.</div>
            <p class="brand-desc">
                An interactive, AI-enhanced practical viva preparation platform built specifically for healthcare 
                technology students. Strengthen your practical knowledge, understand equipment fundamentals, 
                and receive immediate educational feedback.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Session Metrics Row
    stats = calculate_session_stats()
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    with m_col1:
        st.metric(label="Total Questions Available", value=f"{stats['total_available']}", delta="3 Specialties")
    with m_col2:
        st.metric(label="Questions Attempted", value=f"{stats['attempted']}", help="Questions tackled in this active session")
    with m_col3:
        st.metric(label="Correct Answers", value=f"{stats['correct']}", delta=f"{stats['incorrect']} incorrect" if stats['incorrect'] > 0 else None)
    with m_col4:
        st.metric(label="Current Session Accuracy", value=f"{stats['accuracy']:.1f}%")

    st.markdown("---")
    st.subheader("🎯 Choose Your Healthcare Technology Specialty")
    st.write("Select a specialization below to explore curriculum viva questions, machine components, and safety checks.")

    # Specialty Cards
    c1, c2, c3 = st.columns(3)
    
    with c1:
        rt_q = get_questions_for_specialty("Respiratory Therapy")
        st.markdown(
            f"""
            <div class="med-card">
                <span class="badge badge-specialty">Specialty 01</span>
                <h3 style="margin: 0.5rem 0 0.25rem 0; color: #0E7490;">Respiratory Therapy</h3>
                <p style="font-size: 0.85rem; color: #475569; min-height: 48px;">
                    {SPECIALTY_METADATA["Respiratory Therapy"]["tagline"]}
                </p>
                <div style="font-size: 0.85rem; color: #0F172A; margin: 0.5rem 0;">
                    • <b>{len(rt_q)}</b> reviewed questions<br>
                    • Oxygen delivery, ventilators & physiology
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Select Respiratory Therapy", key="btn_select_rt", use_container_width=True):
            st.session_state.selected_specialty = "Respiratory Therapy"
            st.session_state.selected_topic = "All Topics"
            navigate_to("Select Specialty & Topic")

    with c2:
        at_q = get_questions_for_specialty("Anaesthesia Technology")
        st.markdown(
            f"""
            <div class="med-card">
                <span class="badge badge-specialty">Specialty 02</span>
                <h3 style="margin: 0.5rem 0 0.25rem 0; color: #1D4ED8;">Anaesthesia Technology</h3>
                <p style="font-size: 0.85rem; color: #475569; min-height: 48px;">
                    {SPECIALTY_METADATA["Anaesthesia Technology"]["tagline"]}
                </p>
                <div style="font-size: 0.85rem; color: #0F172A; margin: 0.5rem 0;">
                    • <b>{len(at_q)}</b> reviewed questions<br>
                    • Workstations, safety pin indexes & capnography
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Select Anaesthesia Technology", key="btn_select_at", use_container_width=True):
            st.session_state.selected_specialty = "Anaesthesia Technology"
            st.session_state.selected_topic = "All Topics"
            navigate_to("Select Specialty & Topic")

    with c3:
        dt_q = get_questions_for_specialty("Dialysis Technology")
        st.markdown(
            f"""
            <div class="med-card">
                <span class="badge badge-specialty">Specialty 03</span>
                <h3 style="margin: 0.5rem 0 0.25rem 0; color: #047857;">Dialysis Technology</h3>
                <p style="font-size: 0.85rem; color: #475569; min-height: 48px;">
                    {SPECIALTY_METADATA["Dialysis Technology"]["tagline"]}
                </p>
                <div style="font-size: 0.85rem; color: #0F172A; margin: 0.5rem 0;">
                    • <b>{len(dt_q)}</b> reviewed questions<br>
                    • Hemodialysis physics, machine alarms & water standards
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Select Dialysis Technology", key="btn_select_dt", use_container_width=True):
            st.session_state.selected_specialty = "Dialysis Technology"
            st.session_state.selected_topic = "All Topics"
            navigate_to("Select Specialty & Topic")

    st.markdown("---")
    callout_col1, callout_col2 = st.columns([2, 1])
    with callout_col1:
        st.markdown(
            """
            #### 💡 Why MedSkill AI?
            Practical vivas in allied health technology require both conceptual grounding and quick, articulate communication. 
            MedSkill AI provides:
            - **Objective Multiple-Choice Practice** to identify knowledge gaps.
            - **Quick Viva Mode** to compare your oral explanation against reference viva responses.
            - **Immediate, Transparent Explanations** grounded in textbook curriculum.
            - **Targeted Revision Recommendations** that adapt to questions you miss.
            """
        )
    with callout_col2:
        st.markdown("#### Ready to Begin?")
        st.write("Hop straight into practice with your current settings.")
        if st.button("🚀 Start Practising Now", type="primary", use_container_width=True):
            # Load questions for current specialty
            qs = get_questions_for_specialty(st.session_state.selected_specialty)
            reset_practice_session(qs)
            navigate_to("Viva Practice")


# -----------------------------------------------------------------------------
# PAGE 2: SELECT SPECIALTY AND TOPIC
# -----------------------------------------------------------------------------
elif st.session_state.current_page == "Select Specialty & Topic":
    st.markdown(
        """
        <div class="brand-header">
            <h2 style="margin:0; font-size:1.6rem; color:#0F172A;">🎯 Configure Viva Practice Session</h2>
            <p class="brand-desc">Select your specialization, narrow down to a curriculum topic, and pick your training mode.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1.5, 1])

    with col1:
        # Specialty Selection
        spec = st.selectbox(
            "Select Specialty:",
            options=SPECIALTIES,
            index=SPECIALTIES.index(st.session_state.selected_specialty)
        )
        st.session_state.selected_specialty = spec

        # Topic Selection
        available_topics = TOPICS_BY_SPECIALTY.get(spec, ["All Topics"])
        current_topic_idx = 0
        if st.session_state.selected_topic in available_topics:
            current_topic_idx = available_topics.index(st.session_state.selected_topic)
            
        topic = st.selectbox("Select Topic:", options=available_topics, index=current_topic_idx)
        st.session_state.selected_topic = topic

        # Difficulty Selection
        difficulties = ["All Difficulties", "Beginner", "Intermediate", "Advanced"]
        diff = st.selectbox(
            "Filter by Difficulty:",
            options=difficulties,
            index=difficulties.index(st.session_state.selected_difficulty)
        )
        st.session_state.selected_difficulty = diff

        # Mode Selection
        modes = ["MCQ Practice", "Quick Viva"]
        mode = st.radio(
            "Practice Mode:",
            options=modes,
            index=modes.index(st.session_state.practice_mode),
            help="MCQ Practice tests standard 4-option questions. Quick Viva lets you type and compare against an instructor reference viva answer."
        )
        st.session_state.practice_mode = mode

        st.markdown("<div style='margin-top:0.5rem;'></div>", unsafe_allow_html=True)
        # Examiner Pressure Mode Toggle
        pressure_toggle = st.toggle(
            "⏱️ 30-Second Examiner Pressure Mode",
            value=st.session_state.examiner_timer_enabled,
            help="Simulates high-stakes viva exam room conditions with an active 30-second rapid answer countdown timer."
        )
        st.session_state.examiner_timer_enabled = pressure_toggle
        if pressure_toggle:
            st.caption("🔥 *Examiner Pressure Active: You will have 30 seconds to answer before the examiner presses for an answer!*")

    with col2:
        # Live preview of questions matching filters
        matching_questions = get_questions_for_specialty(spec, topic, diff)
        st.markdown(
            f"""
            <div class="med-card" style="background: #F8FAFC;">
                <h4 style="margin: 0 0 0.5rem 0; color: #0F172A;">Session Summary</h4>
                <div style="font-size: 0.9rem; line-height: 1.6; color: #334155;">
                    <b>Specialty:</b> {spec}<br>
                    <b>Topic:</b> {topic}<br>
                    <b>Difficulty:</b> {diff}<br>
                    <b>Mode:</b> {mode}<br>
                    <b>Available Questions:</b> <span style="font-size:1.1rem; font-weight:700; color:#0D9488;">{len(matching_questions)}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if len(matching_questions) == 0:
            st.warning("No questions found with this exact difficulty and topic combination. Please choose 'All Difficulties' or 'All Topics'.")
        else:
            if st.button("🚀 Begin Viva Practice", type="primary", use_container_width=True):
                reset_practice_session(matching_questions)
                navigate_to("Viva Practice")

            # 1-Click Pocket Viva Cram Sheet Download for the selected topic/specialty
            topic_cram_bytes = generate_pocket_cram_sheet(
                specialty=f"{spec} - {topic}",
                questions_list=matching_questions,
                missed_only=False
            )
            st.download_button(
                label="📄 Download Topic Cram Sheet (.docx)",
                data=topic_cram_bytes,
                file_name=f"MedSkill_AI_{spec[:4]}_{topic[:6]}_Cram_Sheet.docx".replace(" ", "_"),
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True,
                help="Download a high-yield, printable summary of questions and examiner keywords for this specific topic."
            )


# -----------------------------------------------------------------------------
# PAGE 3: INTERACTIVE VIVA PRACTICE
# -----------------------------------------------------------------------------
elif st.session_state.current_page == "Viva Practice":
    questions = st.session_state.active_question_list
    
    # If no questions active, load defaults
    if not questions:
        questions = get_questions_for_specialty(
            st.session_state.selected_specialty,
            st.session_state.selected_topic,
            st.session_state.selected_difficulty
        )
        st.session_state.active_question_list = questions
        st.session_state.current_question_idx = 0

    if not questions:
        st.warning("No practice questions currently loaded. Please adjust your topic or filters.")
        if st.button("Return to Selection"):
            navigate_to("Select Specialty & Topic")
    else:
        idx = st.session_state.current_question_idx
        if idx >= len(questions):
            # Session finished
            navigate_to("Results & Feedback")
        
        current_q = questions[idx]
        total_q = len(questions)

        # Header with progress
        progress_val = (idx + 1) / total_q
        st.progress(progress_val)
        
        p_col1, p_col2 = st.columns([3, 1])
        with p_col1:
            st.caption(f"Question {idx + 1} of {total_q} | {current_q['specialty']}")
        with p_col2:
            diff_badge_class = f"badge-{current_q['difficulty'].lower()}"
            st.markdown(
                f"""<div style="text-align: right;">
                    <span class="badge {diff_badge_class}">{current_q['difficulty']}</span>
                    <span class="badge badge-topic">{current_q['topic']}</span>
                </div>""",
                unsafe_allow_html=True
            )

        # Question Card
        st.markdown(
            f"""
            <div class="med-card" style="margin-top: 0.5rem; border-left: 4px solid #0284C7;">
                <div style="font-size: 0.8rem; font-weight:600; color: #64748B; text-transform: uppercase;">
                    ID: {current_q['id']}
                </div>
                <h3 style="margin-top: 0.25rem; font-size: 1.25rem; color: #0F172A; font-weight: 600; line-height: 1.4;">
                    {current_q['question']}
                </h3>
            </div>
            """,
            unsafe_allow_html=True,
        )

        q_id = current_q["id"]
        is_already_answered = q_id in st.session_state.session_answers

        # -------------------
        # 30-SECOND EXAMINER PRESSURE MODE TIMER
        # -------------------
        if st.session_state.examiner_timer_enabled:
            timer_box_html = f"""
            <div style="background:#FFFBEB; border:1.5px solid #F59E0B; border-radius:8px; padding:0.6rem 1rem; margin-top:0.6rem; display:flex; align-items:center; justify-content:space-between;">
                <div style="display:flex; align-items:center; gap:8px;">
                    <span style="font-size:1.2rem;">⏱️</span>
                    <div>
                        <b style="color:#92400E; font-size:0.9rem;">Examiner Pressure Active:</b>
                        <span style="color:#78350F; font-size:0.85rem; margin-left:4px;">The examiner expects a rapid oral answer within 30 seconds.</span>
                    </div>
                </div>
                <div id="viva_timer_badge_{q_id}" style="font-size:1.15rem; font-weight:800; font-family:monospace; background:#FEF3C7; color:#B45309; padding:2px 10px; border-radius:6px; border:1px solid #FCD34D;">
                    30s
                </div>
            </div>
            <script>
            (function() {{
                var timeLeft = 30;
                var el = document.getElementById("viva_timer_badge_{q_id}");
                if (!el) return;
                var timerId = setInterval(function() {{
                    timeLeft--;
                    if (timeLeft > 0) {{
                        el.innerText = timeLeft + "s";
                        if (timeLeft <= 10) {{
                            el.style.color = "#DC2626";
                            el.style.background = "#FEE2E2";
                            el.style.borderColor = "#F87171";
                        }}
                    }} else {{
                        el.innerText = "TIME UP!";
                        el.style.color = "#FFFFFF";
                        el.style.background = "#DC2626";
                        clearInterval(timerId);
                    }}
                }}, 1000);
            }})();
            </script>
            """
            st.markdown(timer_box_html, unsafe_allow_html=True)

        # -------------------
        # MCQ MODE
        # -------------------
        if st.session_state.practice_mode == "MCQ Practice":
            options = current_q["options"]
            
            # Pre-populate selected option if already answered
            prev_selection = 0
            if is_already_answered:
                prev_selection = st.session_state.session_answers[q_id]["selected_index"]

            user_selection = st.radio(
                "Select your answer:",
                options=options,
                index=prev_selection if is_already_answered else 0,
                disabled=st.session_state.current_submitted or is_already_answered,
                key=f"mcq_radio_{q_id}"
            )
            
            selected_idx = options.index(user_selection)

            # Check Answer action (if not yet submitted)
            if not (st.session_state.current_submitted or is_already_answered):
                col_btn, _ = st.columns([1.5, 2.5])
                with col_btn:
                    if st.button("Check Answer", type="primary", use_container_width=True):
                        is_correct = (selected_idx == current_q["correct_index"])
                        st.session_state.session_answers[q_id] = {
                            "question": current_q,
                            "selected_index": selected_idx,
                            "is_correct": is_correct,
                            "student_viva_text": None,
                            "reviewed": True
                        }
                        st.session_state.current_submitted = True
                        st.session_state.current_feedback = is_correct
                        st.rerun()

            # Feedback & Next Question Navigation
            if st.session_state.current_submitted or is_already_answered:
                ans_data = st.session_state.session_answers.get(q_id, {})
                was_correct = ans_data.get("is_correct", False)
                correct_option_text = current_q["options"][current_q["correct_index"]]

                if was_correct:
                    st.markdown(
                        f"""
                        <div class="info-box">
                            <b style="font-size:1.05rem;">✅ Correct! Excellent understanding.</b><br><br>
                            <b>Clinical Explanation:</b> {current_q['explanation']}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"""
                        <div class="warning-box">
                            <b style="font-size:1.05rem;">❌ Incorrect.</b><br><br>
                            <b>Correct Answer:</b> <span style="font-weight:700;">{correct_option_text}</span><br><br>
                            <b>Clinical Explanation:</b> {current_q['explanation']}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                # Key Points Expander
                with st.expander("📌 Key Viva Revision Points & Clinical Rules", expanded=True):
                    for pt in current_q.get("key_points", []):
                        st.markdown(f"- {pt}")

                # Next Question / Finish Button
                st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
                col_next, _ = st.columns([1.5, 2.5])
                with col_next:
                    is_last = (idx == total_q - 1)
                    next_label = "Finish & View Results 🏁" if is_last else "Next Question ➡️"
                    if st.button(next_label, type="primary", use_container_width=True, key=f"btn_next_{q_id}"):
                        st.session_state.current_submitted = False
                        st.session_state.current_feedback = None
                        st.session_state.current_question_idx += 1
                        st.rerun()

        # -------------------
        # QUICK VIVA MODE
        # -------------------
        else:
            st.markdown("💬 **Formulate your concise oral response as if answering the external examiner:**")
            
            existing_text = ""
            if is_already_answered:
                existing_text = st.session_state.session_answers[q_id].get("student_viva_text", "")

            student_answer = st.text_area(
                "Your Viva Explanation:",
                value=existing_text,
                placeholder="State your answer clearly (e.g., physiological mechanism, device settings, safety check priority)...",
                height=120,
                disabled=st.session_state.current_submitted or is_already_answered,
                key=f"viva_text_{q_id}"
            )

            if not (st.session_state.current_submitted or is_already_answered):
                viva_col, _ = st.columns([2, 2])
                with viva_col:
                    if st.button("Compare with Reference Viva Answer", type="primary", use_container_width=True):
                        if not student_answer.strip():
                            st.warning("Please type a brief response before comparing.")
                        else:
                            st.session_state.session_answers[q_id] = {
                                "question": current_q,
                                "selected_index": None,
                                "is_correct": None,
                                "student_viva_text": student_answer,
                                "reviewed": True
                            }
                            st.session_state.current_submitted = True
                            st.rerun()

            if st.session_state.current_submitted or is_already_answered:
                st.markdown(
                    f"""
                    <div class="viva-box">
                        <div style="font-weight: 700; color: #0F172A; margin-bottom: 0.5rem; font-size:1.05rem;">
                            🎯 Model Viva Response (Instructor Standard):
                        </div>
                        <p style="font-style: italic; color: #0F172A; background: #FFFFFF; padding: 0.85rem; border-radius: 6px; border: 1.5px solid #CBD5E1;">
                            "{current_q['sample_viva_answer']}"
                        </p>
                        <div style="margin-top: 0.75rem;">
                            <b>Essential Viva Points to Mention:</b>
                            <ul style="margin-top: 0.35rem; color: #0F172A;">
                                {"".join([f"<li>{pt}</li>" for pt in current_q.get("key_points", [])])}
                            </ul>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.caption("Self-Evaluation: Did your response cover the core physical principles and safety implications?")
                
                st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
                viva_next_col, _ = st.columns([1.5, 2.5])
                with viva_next_col:
                    is_last = (idx == total_q - 1)
                    next_label = "Finish & View Results 🏁" if is_last else "Next Question ➡️"
                    if st.button(next_label, type="primary", use_container_width=True, key=f"viva_next_{q_id}"):
                        st.session_state.current_submitted = False
                        st.session_state.current_feedback = None
                        st.session_state.current_question_idx += 1
                        st.rerun()


# -----------------------------------------------------------------------------
# PAGE 4: RESULTS AND FEEDBACK
# -----------------------------------------------------------------------------
elif st.session_state.current_page == "Results & Feedback":
    st.markdown(
        """
        <div class="brand-header">
            <h2 style="margin:0; font-size:1.6rem; color:#0F172A;">📊 Practice Session Results</h2>
            <p class="brand-desc">Detailed performance breakdown and personalized feedback from your current session.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    stats = calculate_session_stats()

    # Metric Cards
    rc1, rc2, rc3, rc4 = st.columns(4)
    with rc1:
        st.metric("Questions Attempted", f"{stats['attempted']}")
    with rc2:
        st.metric("Correct Answers", f"{stats['correct']}")
    with rc3:
        st.metric("Incorrect Answers", f"{stats['incorrect']}")
    with rc4:
        st.metric("Session Accuracy", f"{stats['accuracy']:.1f}%")

    st.markdown("---")

    # Performance Message
    if stats['attempted'] == 0:
        st.info("No questions have been attempted in this session yet. Start practising to see your results!")
    else:
        if stats['accuracy'] >= 85:
            st.success("🌟 **Outstanding Performance!** You demonstrated strong conceptual clarity across equipment physics and clinical safety principles.")
        elif stats['accuracy'] >= 60:
            st.info("👍 **Good Progress!** You have a solid grasp of the basics. Review the topics flagged below to turn weak areas into strengths.")
        else:
            st.warning("⚠️ **Needs Systematic Revision.** Focus on the key revision notes below, specifically regarding equipment parameters and physiological alarms.")

    # Topic-wise Breakdown
    st.subheader("📋 Performance by Topic")
    
    # Group answered questions by topic
    topic_summary = {}
    for q_id, ans in st.session_state.session_answers.items():
        q = ans["question"]
        t = q["topic"]
        if t not in topic_summary:
            topic_summary[t] = {"total": 0, "correct": 0, "incorrect": 0, "viva_count": 0}
        
        topic_summary[t]["total"] += 1
        if ans["is_correct"] is True:
            topic_summary[t]["correct"] += 1
        elif ans["is_correct"] is False:
            topic_summary[t]["incorrect"] += 1
        else:
            topic_summary[t]["viva_count"] += 1

    if topic_summary:
        cols = st.columns(len(topic_summary) if len(topic_summary) <= 3 else 3)
        for i, (t_name, t_data) in enumerate(topic_summary.items()):
            col_target = cols[i % len(cols)]
            t_acc = (t_data['correct'] / (t_data['correct'] + t_data['incorrect']) * 100) if (t_data['correct'] + t_data['incorrect']) > 0 else 0
            with col_target:
                status_color = "#15803D" if t_acc >= 70 else ("#B45309" if t_acc >= 50 else "#B91C1C")
                st.markdown(
                    f"""
                    <div class="med-card">
                        <div style="font-size:0.75rem; color:#64748B; font-weight:600;">TOPIC</div>
                        <h4 style="margin:0.2rem 0; font-size:1rem; color:#0F172A;">{t_name}</h4>
                        <div style="font-size:0.85rem; color:#475569; margin: 0.4rem 0;">
                            Attempted: <b>{t_data['total']}</b> | Correct: <b>{t_data['correct']}</b> | Missed: <b>{t_data['incorrect']}</b>
                        </div>
                        <div style="font-weight:700; color:{status_color}; font-size:0.95rem;">
                            Accuracy: {t_acc:.0f}%
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    else:
        st.write("Complete questions in MCQ mode to view topic accuracy cards.")

    # Action Buttons
    st.markdown("---")
    act_col1, act_col2 = st.columns(2)
    with act_col1:
        if st.button("💡 View Personalized Study Recommendations", type="primary", use_container_width=True):
            navigate_to("Study Recommendations")
    with act_col2:
        if st.button("🔄 Practise Another Session", use_container_width=True):
            navigate_to("Select Specialty & Topic")


# -----------------------------------------------------------------------------
# PAGE 5: STUDY RECOMMENDATIONS
# -----------------------------------------------------------------------------
elif st.session_state.current_page == "Study Recommendations":
    st.markdown(
        """
        <div class="brand-header">
            <h2 style="margin:0; font-size:1.6rem; color:#0F172A;">💡 Targeted Study Recommendations</h2>
            <p class="brand-desc">
                Transparent, rule-based revision guidance generated directly from your actual question performance.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Collect incorrect answers
    incorrect_questions = [
        ans["question"] for ans in st.session_state.session_answers.values() 
        if ans.get("is_correct") is False
    ]

    if not incorrect_questions:
        st.success("🎉 **No weak topics detected in this session!** You have either scored 100% or have not attempted scored MCQs yet.")
        st.write("You can choose a new specialty or retry questions with 'Advanced' difficulty.")
        if st.button("Start New Practice Session", type="primary"):
            navigate_to("Select Specialty & Topic")
    else:
        st.markdown(
            f"""
            <div class="warning-box" style="margin-bottom:1.5rem;">
                <b>Identified Knowledge Gaps:</b> You missed <b>{len(incorrect_questions)}</b> question(s) during your current practice. 
                Focus on the core clinical principles below before your practical viva.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Action row: Retry Quiz + 1-Click Pocket Viva Cram Sheet Download
        col_retry, col_cram = st.columns([1.5, 1.5])
        with col_retry:
            if st.button("⚡ Quick Retry: Quiz Missed Questions Only", type="primary", use_container_width=True):
                # Reset practice with only missed questions
                # Remove those questions from session_answers so user can retry cleanly
                for q in incorrect_questions:
                    if q["id"] in st.session_state.session_answers:
                        del st.session_state.session_answers[q["id"]]
                reset_practice_session(incorrect_questions)
                navigate_to("Viva Practice")

        with col_cram:
            cram_docx_bytes = generate_pocket_cram_sheet(
                specialty=st.session_state.selected_specialty,
                questions_list=incorrect_questions,
                missed_only=True
            )
            st.download_button(
                label="📄 Download Pocket Cram Sheet (.docx)",
                data=cram_docx_bytes,
                file_name="MedSkill_AI_Missed_Viva_Cram_Sheet.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True,
                help="Generates an ultra-compact, high-yield printable summary of your missed viva questions, physical principles, and examiner buzzwords."
            )

        st.markdown("### 📖 High-Yield Revision Notes for Weak Areas")
        
        # Group by topic
        topics_missed = list(dict.fromkeys([q["topic"] for q in incorrect_questions]))
        for topic in topics_missed:
            matching_missed = [q for q in incorrect_questions if q["topic"] == topic]
            with st.expander(f"📌 {topic} ({len(matching_missed)} question{'s' if len(matching_missed)>1 else ''} missed)", expanded=True):
                for q in matching_missed:
                    st.markdown(f"**Question ID:** `{q['id']}` — *{q['question']}*")
                    st.markdown(f"**Verified Textbook Principle:** {q['explanation']}")
                    st.markdown("**Viva Talking Points:**")
                    for kp in q.get("key_points", []):
                        st.markdown(f"- {kp}")
                    st.markdown("---")


# -----------------------------------------------------------------------------
# PAGE 6: ASK MEDSKILL AI
# -----------------------------------------------------------------------------
elif st.session_state.current_page == "Ask MedSkill AI":
    st.markdown(
        """
        <div class="brand-header">
            <h2 style="margin:0; font-size:1.6rem; color:#0F172A;">🤖 Ask MedSkill AI — Viva Concept Tutor</h2>
            <p class="brand-desc">
                Ask any question regarding equipment physics, machine safety, or physiological parameters. 
                Answers are simplified for beginner-to-intermediate healthcare technology viva revision.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # API Key status check (without exposing secrets)
    has_api_key = bool(get_secret("GEMINI_API_KEY") or get_secret("OPENAI_API_KEY"))

    if has_api_key:
        st.caption("🟢 **Connected:** External LLM Educational Engine Enabled")
    else:
        st.caption("🔵 **Verified Curriculum Mode (Offline-First):** Explanations drawn directly from verified question bank")

    ai_spec = st.selectbox(
        "Select Relevant Specialty Context:",
        options=SPECIALTIES,
        index=SPECIALTIES.index(st.session_state.selected_specialty)
    )

    quick_prompts = {
        "Respiratory Therapy": [
            "Explain the difference between Peak and Plateau pressure",
            "Why is 5 L/min minimum required for a simple face mask?",
            "How does a Venturi mask utilize the Bernoulli principle?"
        ],
        "Anaesthesia Technology": [
            "Why does the oxygen flush valve bypass vaporizers?",
            "Explain the Pin Index Safety System (PISS) and pins for O2",
            "What does Phase III on a capnogram indicate?"
        ],
        "Dialysis Technology": [
            "Explain diffusion vs ultrafiltration in hemodialysis",
            "Why is counter-current flow used in dialyzers?",
            "What causes a blood leak alarm and what action is required?"
        ]
    }

    st.markdown("**Quick Viva Questions:**")
    prompt_cols = st.columns(3)
    selected_quick_prompt = None
    for i, p_text in enumerate(quick_prompts.get(ai_spec, [])):
        with prompt_cols[i]:
            if st.button(p_text, key=f"quick_p_{i}", use_container_width=True):
                selected_quick_prompt = p_text

    user_query = st.text_input(
        "Enter your healthcare technology viva question:",
        value=selected_quick_prompt if selected_quick_prompt else "",
        placeholder="e.g., Explain why desflurane requires a heated Tec 6 vaporizer..."
    )

    if st.button("Get Educational Explanation", type="primary"):
        if not user_query.strip():
            st.warning("Please type a question or choose one of the quick viva prompts above.")
        else:
            with st.spinner("Analyzing curriculum concepts..."):
                response_text = query_optional_ai(user_query, ai_spec)
                st.markdown(
                    f"""
                    <div class="med-card" style="border-left: 4px solid #0D9488; margin-top: 1rem;">
                        <h4 style="margin: 0 0 0.5rem 0; color: #0F172A;">Educational Explanation</h4>
                        <div style="font-size: 0.95rem; line-height: 1.6; color: #1E293B;">
                            {response_text}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                st.caption("⚠️ **Educational Prototype Notice:** Always verify explanations against your institution's prescribed textbooks and faculty instructions. Never use for clinical decision-making.")


# -----------------------------------------------------------------------------
# PAGE 7: DESIGN THINKING PORTFOLIO
# -----------------------------------------------------------------------------
elif st.session_state.current_page == "Design Thinking Portfolio":
    st.markdown(
        """
        <div class="brand-header">
            <span class="badge badge-specialty">Academic Documentation</span>
            <h2 style="margin:0.25rem 0 0 0; font-size:1.6rem; color:#0F172A;">
                📘 Design Thinking Journey: Design for the Unseen
            </h2>
            <p class="brand-desc">
                Human-Centered Innovation Challenge documentation detailing the evolution of <b>MedSkill AI</b> 
                across all 5 stages of the Design Thinking process.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    dt_tab1, dt_tab2, dt_tab3, dt_tab4, dt_tab5 = st.tabs([
        "01 — Empathize",
        "02 — Define",
        "03 — Ideate (10 Ideas)",
        "04 — Prototype 1 → 2",
        "05 — User Testing & Impact"
    ])

    with dt_tab1:
        st.markdown(
            """
            ### 01 — Empathize: Discovering the Unseen User & 25 Real Clinical Problems
            
            **The Unseen User:**
            Undergraduate healthcare technology students (**Respiratory Therapy**, **Anaesthesia Technology**, **Dialysis Technology**) 
            undergoing rigorous clinical rotations and preparing for high-stakes practical viva examinations.

            **Core Interview Cohort (8 Student Stakeholders):**
            - **Riddhi & Siddhi** (3rd Year, Respiratory Technology)
            - **Naziya & Preethi** (2nd & 3rd Year, Critical Care / Respiratory Postings)
            - **Bhargav & Naveen** (2nd & 3rd Year, Anaesthesia & ICU Technology)
            - **Tharun & Atharv** (3rd & 2nd Year, Ventilator & ICU Technology)

            ---
            """
        )

        st.markdown("#### 📸 Direct Field Research Evidence & Student Interviews")
        img_col1, img_col2 = st.columns(2)
        with img_col1:
            st.image(
                "assets/interviews/interview_photo_1.jpg",
                caption="Figure E.1: Conducting in-person empathy interview and question audit with Respiratory student stakeholder.",
                use_container_width=True
            )
            st.image(
                "assets/interviews/hand_sketch_notes.jpg",
                caption="Figure E.3: Bedside hand-sketched diagrams detailing humidifier bottle circuits and transport cylinder risks.",
                use_container_width=True
            )
        with img_col2:
            st.image(
                "assets/interviews/interview_photo_2.jpg",
                caption="Figure E.2: Deep-dive session recording practical viva pain points, alarm fatigue, and passive revision habits.",
                use_container_width=True
            )
            st.image(
                "assets/interviews/interview_written_notes.png",
                caption="Figure E.4: Actual handwritten field notes capturing floor hazards (humidifier low water, self-extubation, gas leak checks, TMP spikes).",
                use_container_width=True
            )

        st.markdown(
            """
            ---
            #### 📋 25 Real Clinical Problems Discovered Through Direct Observation
            Through shadowing shifts and deep user interviews, the team documented 25 genuine problems experienced by students on hospital floors:
            1. *Low Water Level in Oxygen Humidifier Bottles*
            2. *Delayed Response to Ventilator Alarms*
            3. *Accidental Patient Self-Extubation*
            4. *Difficulty Finding Chest X-rays During ICU Rounds*
            5. *Difficulty Tracking ABG Reports and Ventilator Settings*
            6. *Incomplete Respiratory Therapist Handover Between Shifts*
            7. *Time-Consuming and Repetitive Respiratory Documentation*
            8. *Ventilator Circuit Disconnection During Patient Repositioning*
            9. *Difficulty Monitoring NIV Mask Leaks*
            10. *Difficulty Tracking Endotracheal Tube (ETT) Position & Depth*
            11. *Delayed Suctioning and Airway-Care Task Tracking*
            12. *Respiratory Equipment Unavailability During Emergency Admissions*
            13. *Missed or Delayed Weaning Assessments in Stable ICU Patients*
            14. *Oxygen Supply Management During Patient Transport*
            15. *Difficulty Tracking Repeated Desaturation Episodes*
            16. *Severe ICU Alarm Fatigue*
            17. *Difficulty Tracking Pending RT Tasks Across ICU Beds*
            18. *Inadequate Monitoring of Oxygen Therapy Settings*
            19. *Delayed Identification of Respiratory Deterioration*
            20. *Difficulty Maintaining Real-Time ICU Respiratory Records*
            21. *Difficulty Tracking Humidification Adequacy During Oxygen Therapy*
            22. *Delayed Identification of Ventilator Patient Asynchrony*
            23. *Difficulty Monitoring Respiratory Support Changes During Patient Transfers*
            24. *Difficulty Tracking Equipment Maintenance and Calibration Expiry*
            25. *Lack of a Centralized Respiratory Patient Dashboard*

            **What We Discovered (The "Problem Behind the Problem"):**
            While technologists perform physical procedures daily, they operate under immense cognitive overload. When external examiners test them on *why* alarms sound, *how* ventilator waveforms change, or *how* blood gas gradients work, students freeze because they suffer from **Passive Revision Syndrome**—memorizing textbooks without active verbal reasoning practice.
            """
        )

    with dt_tab2:
        st.markdown(
            """
            ### 02 — Define: Framing the REAL Problem
            
            **The Initial Assumption:**
            Students don't have enough reference material or revision notes for their viva exams.
            
            **The Real Problem Discovered:**
            Healthcare technology students suffer from **passive revision syndrome**. They read heavy manuals but have no way to:
            1. Test their conceptual understanding against verified clinical standards.
            2. Self-evaluate oral answers before standing in front of an external examiner.
            3. Pinpoint their exact weak topics (e.g., confusing diffusion with ultrafiltration, or APL valve settings).
            
            **Reframed Problem Statement:**
            > *"How might we provide healthcare technology students with an accessible, interactive digital viva simulator that pinpoints conceptual misconceptions and provides verified textbook explanations without requiring complex infrastructure?"*
            """
        )

    with dt_tab3:
        st.markdown(
            """
            ### 03 — Ideate: Generating 10 Solutions
            
            Two ideation techniques were used: **Brainstorming** and **Crazy 8s / SCAMPER**.
            
            1. **Idea 1 (Discarded):** Flashcard flashcards on paper — *Discarded: Static, easily misplaced, no interactive feedback.*
            2. **Idea 2 (Discarded):** Heavy Android/iOS mobile application with database — *Discarded: Too heavy, barriers to entry, requires phone app stores.*
            3. **Idea 3 (Discarded):** Voice-only AI chatbot with audio recognition — *Discarded: High latency, speech recognition often fails on technical medical terms in noisy college labs.*
            4. **Idea 4 (Selected):** Web-based dual-mode practical viva trainer (MCQ + Quick Viva) with zero login friction.
            5. **Idea 5:** Video simulation of machine knobs — *Too complex for a 10-day prototype.*
            6. **Idea 6:** Peer-to-peer random audio calling — *Scheduling conflicts among hospital shift students.*
            7. **Idea 7 (Selected):** Rule-based adaptive study recommendations that extract only the questions students failed.
            8. **Idea 8 (Selected):** Curated local question bank with verified physics/pathophysiology rationales.
            9. **Idea 9 (Selected):** Optional AI tutor fallback that works offline even without internet/API keys.
            10. **Idea 10:** Gamified points leaderboard — *Deprioritized to keep focus strictly on learning value rather than competition.*
            """
        )

    with dt_tab4:
        st.markdown(
            """
            ### 04 — Prototype Evolution: Prototype 1 vs Prototype 2
            
            | Feature | Prototype 1 (Initial Build) | Prototype 2 (Current Iteration) | User Feedback Driver |
            | :--- | :--- | :--- | :--- |
            | **Practice Modes** | MCQ Only | Added **Quick Viva Mode** (Student types answer & compares with reference) | *"Examiners ask oral questions, not multiple choice!"* |
            | **Viva Urgency** | Untimed static quiz | **30-Second Examiner Pressure Mode** (Rapid countdown timer) | *"We panic because examiners don't wait — simulate that urgency."* |
            | **Offline Study Takeaway** | Screen-only viewing | **1-Click Pocket Viva Cram Sheet** (Printable .docx generator) | *"Give us a 2-page cheat sheet of missed questions to carry to the exam hall."* |
            | **Difficulty Levels** | Flat list of questions | **Beginner / Intermediate / Advanced** tags | *"First-year students need foundational questions first."* |
            | **Revision Flow** | Generic results page | **Targeted Study Recommendations** with a 1-click **"Retry Missed Questions Quiz"** | *"Show me only the questions I got wrong so I can retest."* |
            | **Connectivity** | Required external API | **Offline-First Local Knowledge Retrieval** fallback | *"Hospital basements and college labs have terrible internet."* |
            | **Visual Design** | Default raw controls | **Academic Clean Interface** with custom badges and high-contrast typography | *"Clean and readable on laptops during breaks."* |
            """
        )

    with dt_tab5:
        st.markdown(
            """
            ### 05 — User Testing & Real Feedback Evidence
            
            **Primary Testing Cohort:**
            Tested directly with our 8 core student stakeholders (**Riddhi, Siddhi, Naziya, Preethi, Bhargav, Naveen, Tharun, Atharv**) 
            plus 6 junior technologists across hospital rotations.

            **Direct Stakeholder Feedback & Resulting Iterations:**
            - **Riddhi (Resp. Therapy):** *"The font was invisible on mobile dark mode!"* $\rightarrow$ Fixed with locked light theme and high-contrast CSS.
            - **Siddhi (Resp. Therapy):** *"Only 2 ventilator questions isn't enough."* $\rightarrow$ Expanded to **144 questions (12 in EVERY topic)**.
            - **Naziya (Allied Health):** *"Examiners don't give 4 options; they ask us to explain aloud."* $\rightarrow$ Created **Quick Viva Mode** with model instructor answer comparison.
            - **Preethi (Resp. Care):** *"The next button was awkward above the text."* $\rightarrow$ Moved Next button directly below feedback with primary blue focus.
            - **Bhargav (Anaesthesia Tech):** *"I don't want to redo 20 questions just to review 2 mistakes."* $\rightarrow$ Built **1-Click Quick Retry Quiz** isolating only missed questions.
            - **Naveen (Critical Care):** *"ICU basements have zero mobile reception."* $\rightarrow$ Implemented **Offline-First Knowledge Engine** that requires no API keys or internet.
            - **Tharun (Resp. Care):** *"Juniors need simpler questions first."* $\rightarrow$ Built **Beginner, Intermediate, and Advanced Difficulty Tiers**.
            - **Atharv (ICU Tech):** *"Give us the exact buzzwords examiners want to hear."* $\rightarrow$ Added the **"📌 Key Viva Revision Points"** expander card.
            
            ---

            ### 🎤 5-Minute Final Presentation Storyline:
            - **We thought** students lacked reading material.
            - **We went and observed** 8 students (Riddhi, Siddhi, Naziya, Preethi, Bhargav, Naveen, Tharun, Atharv) and uncovered 25 real clinical bottlenecks (humidifier drying, alarm fatigue, circuit disconnects, ETT tracking).
            - **We discovered** that viva anxiety and bedside panic both stem from **Passive Revision Syndrome**—students memorize procedures without verbal conceptual models.
            - **We realised the real problem was** the lack of a low-stakes digital simulator that bridges hospital tasks with oral viva reasoning.
            - **We generated** 10 ideas and killed our first idea (a complex 3D VR knob simulator) to focus on a zero-friction mobile/web simulator.
            - **We built Prototype 1** as a simple 24-MCQ script.
            - **Users told us** they needed oral practice, 144 comprehensive questions, dark mode legibility, and offline functionality.
            - **So we changed** the architecture into **Prototype 2**: adding Quick Viva comparison, targeted study recommendations, 1-click retries, and offline-first intelligence.
            - **Our final solution is** **MedSkill AI** ([medskill-ai.streamlit.app](https://medskill-ai.streamlit.app/)) — an accessible, verified practical viva companion for allied health technology students.
            """
        )
