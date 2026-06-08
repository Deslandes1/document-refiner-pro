import streamlit as st
import zipfile
import io
import base64
from datetime import datetime
from weasyprint import HTML

st.set_page_config(
    page_title="Document Refiner Pro | GLOBALINTERNET.PY",
    page_icon="📄",
    layout="wide"
)

# ========== SYSTEM ACCENT STYLING ==========
st.markdown("""
<style>
    .stApp { background-color: #f0f2f6; }
    .stButton>button { background-color: #2c7be5; color: white; border-radius: 25px; width: 100%; }
    .header-box {
        background-color: #0a4c8c;
        padding: 25px;
        border-radius: 12px;
        color: white;
        margin-bottom: 25px;
    }
</style>
""", unsafe_allow_html=True)

# ========== FIXED EMBEDDED LOGO DATA ==========
# High-fidelity vector graphic with golden star crescent array matching requested profile geometry
LOGO_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 115" width="90" height="105">
    <g transform="translate(0, 15)">
        <circle cx="50" cy="50" r="45" fill="none" stroke="#90e0ef" stroke-width="2" opacity="0.6"/>
        <ellipse cx="50" cy="50" rx="45" ry="14" fill="none" stroke="#00b4d8" stroke-width="1.5" transform="rotate(25 50 50)"/>
        <ellipse cx="50" cy="50" rx="45" ry="14" fill="none" stroke="#00b4d8" stroke-width="1.5" transform="rotate(-25 50 50)"/>
        <circle cx="50" cy="50" r="40" fill="#03045e" stroke="#90e0ef" stroke-width="2.5" />
        <ellipse cx="50" cy="50" rx="40" ry="14" fill="none" stroke="#90e0ef" stroke-width="1.2" opacity="0.85"/>
        <ellipse cx="50" cy="50" rx="14" ry="40" fill="none" stroke="#90e0ef" stroke-width="1.2" opacity="0.85"/>
        <line x1="10" y1="50" x2="90" y2="50" stroke="#90e0ef" stroke-width="1.2" opacity="0.8" />
        <line x1="50" y1="10" x2="50" y2="90" stroke="#90e0ef" stroke-width="1.2" opacity="0.8" />
        <path d="M22,43 Q25,36 32,38 T40,46 T28,53 Z" fill="#0077b6" opacity="0.9"/>
        <path d="M58,33 Q63,38 73,36 T80,48 T63,58 Z" fill="#0077b6" opacity="0.9"/>
        <path d="M42,63 Q47,70 52,66 T59,78 T37,76 Z" fill="#0077b6" opacity="0.9"/>
    </g>
    <g fill="#ffd700" stroke="#ffd700" stroke-width="0.5">
        <text x="16" y="14" font-size="12" text-anchor="middle">★</text>
        <text x="32" y="9" font-size="15" text-anchor="middle">★</text>
        <text x="50" y="7" font-size="19" text-anchor="middle">★</text>
        <text x="68" y="9" font-size="15" text-anchor="middle">★</text>
        <text x="84" y="14" font-size="12" text-anchor="middle">★</text>
    </g>
</svg>"""

B64_LOGO = base64.b64encode(LOGO_SVG.encode('utf-8')).decode('utf-8')
SRC_LOGO = f"data:image/svg+xml;base64,{B64_LOGO}"

# Permanent Sidebar Identity Branding
st.logo(SRC_LOGO, link="https://github.com")

# ========== DATA CACHE TEMPLATES ==========
def get_cv_template():
    return """PROFESSIONAL SUMMARY

Results‑driven Senior Software Architect with 4+ years of experience designing, building, and deploying 37 custom enterprise and AI applications for global clients. Expert in Python ecosystem, Streamlit engineering, advanced AI integration (Groq Llama 3.1), real‑time distributed systems, and cloud architecture. Proven ability to lead full‑cycle product engineering from baseline requirements to scalable cloud production. Fluent in English, French, Spanish, Haitian Creole.

CORE COMPETENCIES

- System Architecture: Distributed real‑time data pipelines, high-throughput observability platforms, API design
- AI & Machine Learning: LLM integration, prompt engineering, anomaly detection, autonomous agent logic
- Full‑Stack Development: Python, Streamlit, Pandas, Plotly, asynchronous REST APIs
- Cloud & DevOps: Streamlit Cloud infrastructure, advanced GitHub version control, secrets management, CI/CD pipelines
- Multilingual Solutions: Cross-border UI/UX adaptation, internationalization, and AI audio synthesis

KEY PROJECTS

System Health AI Monitor | Architect & Creator
Live: https://system-health-ai-monitor-important-9bemdyosmbfmtx4t8wygbv.streamlit.app/
- Designed and deployed an enterprise-grade observability platform that simulates mission-critical server metrics, detects systemic anomalies, and generates AI‑driven predictive insights via Groq Llama 3.1.
- Engineered a multilingual user interface (English, French, Spanish) along with synchronized AI vocal diagnostics leveraging edge‑tts.

SafeHaven – Anti‑Trafficking AI | Lead Developer
Live: https://call-for-code-ai-global-challenge-2026-jimupcwzzyntghxdwxpbg9.streamlit.app/
- Built an AI‑powered early warning intelligence system that processes user‑submitted risk environments, flags human trafficking indicators, and handles anonymous data routing.
- Leveraged Groq LLM backends to generate granular risk matrices and automated situational action plans.

Hospital Management System | Full‑Stack Developer
Live: https://hospital-management-system-software-built-by-gesner-deslandes.streamlit.app/
- Developed an all-in-one hospital management suite spanning modern patient intake, EMR logs, dynamic ledger billing, pharmacy tracking, and an integrated AI diagnostic core.
- Configured real‑time system alerts and dynamic multilingual translation layers.

PROFESSIONAL EXPERIENCE

GLOBALINTERNET.PY – Founder & Engineer‑in‑Chief | 2021 – Present
- Formulated and delivered 37 advanced Python applications ranging from biometric voting engines and custom business intelligence suites to interactive autonomous vehicle simulators.
- Directed all high-level operational phases: strategic architecture design, agile product coding, client discovery, and secure cloud system deployment.
- Maintained a production tech stack focused on Streamlit framework mastery, real-time data streaming, and deep API integrations (Groq, edge-tts).

Be Like Brit Orphanage – Technology Coordinator | 2021 – Present
- Supervise core IT infrastructure, cloud connectivity protocols, security firewalls, and hardware availability matrices for over 50 power users.
- Independently manage full-system troubleshooting and hardware asset management under dynamic infrastructure profiles.

EDUCATION & CERTIFICATIONS

- Senior-Level Software Architecture Portfolio (Continuous Practical Research)
- Vocational Training Certification – Advanced American English
- Office Computing Specialist Certification
- High School Graduate

LANGUAGES

- English – Professional working proficiency
- French – Professional working proficiency
- Spanish – Conversational
- Haitian Creole – Native

REFERENCES

- Teresa Lang Ehlert: tbtrekkin@gmail.com
- Charles Zerr MD: +1 620 952 0074"""

def get_swot_template():
    return """Executive SWOT Analysis

Prepared by: Gesner Deslandes
Date: June 2026
Purpose: Software Architect / Platform Engineer (Contract)

STRENGTHS (Internal)
- Deep technical expertise in Python, full‑stack development, AI/LLM integration, and real‑time system design.
- Proven track record: 37 custom applications delivered to global clients.
- Direct client‑facing experience: requirements gathering, project management, post‑delivery support."""

def get_bio_template():
    return """Executive Bio

Prepared for: Marcy / Career Coach Marcy
Prepared by: Gesner Deslandes
Date: June 2026

Gesner Deslandes is the Founder, Owner, and Engineer‑in‑Chief of GLOBALINTERNET.PY, a software development company that builds custom Python and AI‑powered solutions for clients worldwide."""

def get_cover_body_template():
    today = datetime.now().strftime("%B %d, %Y")
    return f"""{today}

RE: Senior Software Architect / Lead Platform Engineer (Contract) Position

Dear Hiring Manager,

I am writing to formally express my interest in the Senior Software Architect and Platform Engineer contract positions with your organization. Bringing a proven portfolio of 37 custom-engineered Python systems deployed to global production, I offer a potent blend of advanced systems infrastructure engineering, deep AI model integration, and proactive project leadership."""

# ========== INITIALIZE PERSISTENT REPOSITORY STATE ==========
if "cv_text" not in st.session_state:
    st.session_state.cv_text = get_cv_template()
if "swot_text" not in st.session_state:
    st.session_state.swot_text = get_swot_template()
if "bio_text" not in st.session_state:
    st.session_state.bio_text = get_bio_template()
if "cover_text" not in st.session_state:
    st.session_state.cover_text = get_cover_body_template()

# ========== CONTROL CENTER SIDEBAR ==========
with st.sidebar:
    st.title("💼 Workspace Controller")
    doc_type = st.radio("Selected Focus Target:", ["CV (Resume)", "SWOT Analysis", "Executive Bio", "Cover Letter"])
    
    st.markdown("---")
    st.subheader("🎨 Profile Themes")
    bg_options = {
        "Clean White": "#ffffff",
        "Mountain Mist": "linear-gradient(135deg, #e2e2e2 0%, #c9d6ff 100%)",
        "Sky Blue Gradient": "linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)"
    }
    selected_bg = st.selectbox("Document Canvas", list(bg_options.keys()), index=0)
    bg_css = bg_options[selected_bg]
    
    text_color = st.color_picker("Body Text Ink", "#1a2a3a")
    heading_color = st.color_picker("Primary Header Shield", "#0a4c8c")
    font_family = st.selectbox("Typography Family", ["Segoe UI", "Arial", "Georgia", "Roboto"], index=0)

# ========== COMPILER CORE ENGINE ==========
def build_html_document(title, body_text, bg, text_col, heading_col, font, for_pdf=False):
    escaped_body = body_text.replace("\n", "<br>")
    
    # Unified Global Header Canvas Blueprint
    header_html = f"""
    <div style="background-color: {heading_col}; padding: 24px; border-radius: 12px; margin-bottom: 30px; display: table; width: 100%; box-sizing: border-box;">
        <div style="display: table-cell; vertical-align: middle; width: 100px;">
            <img src="{SRC_LOGO}" width="85" height="100" style="display: block;">
        </div>
        <div style="display: table-cell; vertical-align: middle; text-align: right; font-family: 'Segoe UI', sans-serif;">
            <h1 style="margin: 0; color: #ffffff; font-size: 32px; font-weight: bold; letter-spacing: 0.5px;">GESNER DESLANDES</h1>
            <p style="margin: 5px 0; color: #f3f0df; font-size: 14px;">deslandes78@gmail.com | +509 4738 5663 | Haiti</p>
            <p style="margin: 0; color: #ffd700; font-size: 16px; font-weight: bold; letter-spacing: 1px;">SOFTWARE ARCHITECT & AI SOLUTIONS ENGINEER</p>
        </div>
    </div>
    """
    
    container_style = f"background: {bg}; color: {text_col}; font-family: {font}, sans-serif; padding: 40px; border-radius: 16px; min-height: 800px;"
    if for_pdf:
        container_style = f"background: #ffffff; color: #1a2a3a; font-family: {font}, sans-serif; padding: 0px;"

    return f"""<!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            @page {{ size: letter; margin: 2cm; }}
            body {{ margin: 0; padding: 0; background-color: #f0f2f6; }}
            .content-layer {{ {container_style} }}
            h2, h3 {{ color: {heading_col}; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="content-layer">
            {header_html}
            <div style="font-size: 14px; line-height: 1.6; font-family: sans-serif;">
                {escaped_body}
            </div>
        </div>
    </body>
    </html>"""

# ========== PRODUCTION WORKSPACE INTERFACE ==========
st.subheader(f"📝 Content Control Engine: {doc_type}")

# Routing assignment selector
if doc_type == "CV (Resume)":
    st.session_state.cv_text = st.text_area("Live Database Field Editor", value=st.session_state.cv_text, height=400)
    active_payload = st.session_state.cv_text
elif doc_type == "SWOT Analysis":
    st.session_state.swot_text = st.text_area("Live Database Field Editor", value=st.session_state.swot_text, height=400)
    active_payload = st.session_state.swot_text
elif doc_type == "Executive Bio":
    st.session_state.bio_text = st.text_area("Live Database Field Editor", value=st.session_state.bio_text, height=400)
    active_payload = st.session_state.bio_text
else:
    st.session_state.cover_text = st.text_area("Live Database Field Editor", value=st.session_state.cover_text, height=400)
    active_payload = st.session_state.cover_text

# ========== STABLE RENDERING CANVAS WORKAROUND ==========
st.markdown("### 🖥️ Native Live Sandbox Preview")

# Constructing native Streamlit columns to guarantee UI rendering structure remains bulletproof
preview_box = st.container(border=True)
with preview_box:
    col_logo, col_bio = st.columns([1, 4])
    with col_logo:
        st.image(SRC_LOGO, width=100)
    with col_col2 := col_bio:
        st.markdown(f"""
        <div style="text-align: right; font-family: 'Segoe UI', sans-serif; background-color: {heading_color}; padding: 20px; border-radius: 8px; color: white;">
            <h1 style="margin:0; color:white; font-size:26px;">GESNER DESLANDES</h1>
            <p style="margin:2px 0; color:#ffd700; font-weight:bold; font-size:14px;">SOFTWARE ARCHITECT & AI SOLUTIONS ENGINEER</p>
            <p style="margin:0; color:#e0e0e0; font-size:12px;">deslandes78@gmail.com | +509 4738 5663 | Haiti</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown(f"<div style='color: {text_color}; font-family: {font_family}; white-space: pre-wrap;'>{active_payload}</div>", unsafe_allow_html=True)

# ========== EXPORT PIPELINE DISTRIBUTION ==========
st.markdown("### 📥 Document Asset Distribution Channel")

live_pdf_html = build_html_document(doc_type, active_payload, bg_css, text_color, heading_color, font_family, for_pdf=True)
pdf_export_bytes = HTML(string=live_pdf_html).write_pdf()

st.download_button(
    label=f"🏆 Compile & Export {doc_type} to PDF Sheet",
    data=pdf_export_bytes,
    file_name=f"gesner_deslandes_{doc_type.lower().replace(' ', '_')}.pdf",
    mime="application/pdf",
    use_container_width=True
)
