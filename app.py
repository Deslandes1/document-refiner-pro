import streamlit as st
import zipfile
import io
import base64
from datetime import datetime
from weasyprint import HTML
import colorsys

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
</style>
""", unsafe_allow_html=True)

# ========== FIXED EMBEDDED LOGO DATA ==========
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
st.logo(SRC_LOGO)

# ========== TEMPLATES ==========
def get_cv_template():
    return """PROFESSIONAL SUMMARY
Results‑driven Senior Software Architect with 4+ years of experience designing, building, and deploying 37 custom enterprise and AI applications for global clients. Expert in Python ecosystem, Streamlit engineering, advanced AI integration (Groq Llama 3.1), real‑time distributed systems, and cloud architecture. Proven ability to lead full‑cycle product engineering from baseline requirements to scalable cloud production. Fluent in English, French, Spanish, Haitian Creole.

CORE COMPETENCIES
System Architecture: Distributed real‑time data pipelines, high-throughput observability platforms, API design

AI & Machine Learning: LLM integration, prompt engineering, anomaly detection, autonomous agent logic

Full‑Stack Development: Python, Streamlit, Pandas, Plotly, asynchronous REST APIs

Cloud & DevOps: Streamlit Cloud infrastructure, advanced GitHub version control, secrets management, CI/CD pipelines

Multilingual Solutions: Cross-border UI/UX adaptation, internationalization, and AI audio synthesis

KEY PROJECTS
System Health AI Monitor | Architect & Creator
Live: https://system-health-ai-monitor-important-9bemdyosmbfmtx4t8wygbv.streamlit.app/
Designed and deployed an enterprise-grade observability platform that simulates mission-critical server metrics, detects systemic anomalies, and generates AI‑driven predictive insights via Groq Llama 3.1.
Engineered a multilingual user interface (English, French, Spanish) along with synchronized AI vocal diagnostics leveraging edge‑tts.

SafeHaven – Anti‑Trafficking AI | Lead Developer
Live: https://call-for-code-ai-global-challenge-2026-jimupcwzzyntghxdwxpbg9.streamlit.app/
Built an AI‑powered early warning intelligence system that processes user‑submitted risk environments, flags human trafficking indicators, and handles anonymous data routing.
Leveraged Groq LLM backends to generate granular risk matrices and automated situational action plans.

Hospital Management System | Full‑Stack Developer
Live: https://hospital-management-system-software-built-by-gesner-deslandes.streamlit.app/
Developed an all-in-one hospital management suite spanning modern patient intake, EMR logs, dynamic ledger billing, pharmacy tracking, and an integrated AI diagnostic core.
Configured real‑time system alerts and dynamic multilingual translation layers.

PROFESSIONAL EXPERIENCE
GLOBALINTERNET.PY – Founder & Engineer‑in‑Chief | 2021 – Present
Formulated and delivered 37 advanced Python applications ranging from biometric voting engines and custom business intelligence suites to interactive autonomous vehicle simulators.
Directed all high-level operational phases: strategic architecture design, agile product coding, client discovery, and secure cloud system deployment.
Maintained a production tech stack focused on Streamlit framework mastery, real-time data streaming, and deep API integrations (Groq, edge-tts).

Be Like Brit Orphanage – Technology Coordinator | 2021 – Present
Supervise core IT infrastructure, cloud connectivity protocols, security firewalls, and hardware availability matrices for over 50 power users.
Independently manage full-system troubleshooting and hardware asset management under dynamic infrastructure profiles.

EDUCATION & CERTIFICATIONS
Senior-Level Software Architecture Portfolio (Continuous Practical Research)
Vocational Training Certification – Advanced American English
Office Computing Specialist Certification
High School Graduate

LANGUAGES
English – Professional working proficiency
French – Professional working proficiency
Spanish – Conversational
Haitian Creole – Native

REFERENCES
Teresa Lang Ehlert: tbtrekkin@gmail.com
Charles Zerr MD: +1 620 952 0074"""

def get_swot_template():
    return """Executive SWOT Analysis

Prepared by: GESNER DESLANDES
Date: June 2026
Purpose: Software Architect / Platform Engineer (Contract)

STRENGTHS (Internal)
- Deep technical expertise in Python, full‑stack development, AI/LLM integration, and real‑time system design.
- Proven track record: 37 custom applications delivered to global clients.
- Direct client‑facing experience: requirements gathering, project management, post‑delivery support.
- Self‑motivated, highly organised, and effective in fully remote environments.
- Willing to travel when required.
- Multilingual: English, French, Spanish, Haitian Creole.
- Entrepreneurial mindset (founder of GlobalInternet.py) combined with hands‑on coding.

WEAKNESSES (Internal)
- Limited experience in large corporate team structures (mostly solo projects).
- No formal computer science degree (compensated by portfolio and practical results).
- Based in Haiti – potential time zone differences with USA/Canada.
- Lacks enterprise‑level Agile/Scrum certifications (actively learning).

OPPORTUNITIES (External)
- Leverage technical background into a senior architecture or platform engineering role within a structured organisation.
- Transition from founder to collaborative team environment offering mentorship and growth.
- Expand professional network in North American and European markets.
- Use multilingual skills to support international clients and cross‑border teams.

THREATS (External)
- Competitive job market for senior tech roles.
- Preference for candidates with local degrees or specific cloud certifications.
- Economic and political situation in Haiti may affect travel or visa processes (fully remote is preferred).

CONCLUSION
Gesner Deslandes brings a rare combination of software architecture skills, AI integration, and direct client success. His ability to deliver production‑ready systems end‑to‑end makes him a strong candidate for senior‑level contract roles. With the right opportunity and mentorship, he will deliver significant value.
"""

def get_bio_template():
    return """Executive Bio

Prepared for: Marcy / Career Coach Marcy
Prepared by: GESNER DESLANDES
Date: June 2026

GESNER DESLANDES is the Founder, Owner, and Engineer‑in‑Chief of GLOBALINTERNET.PY, a software development company that builds custom Python and AI‑powered solutions for clients worldwide. With over four years of hands‑on experience, he has delivered 37 unique software products, including real‑time system health monitors, AI‑powered anti‑trafficking platforms, hospital management systems, and multilingual educational tools.

His technical expertise spans system architecture, full‑stack development (Python, Streamlit, Pandas, Plotly), AI integration (Groq Llama 3.1), cloud deployment (Streamlit Cloud, GitHub), and real‑time observability. He designs and builds end‑to‑end solutions that solve real problems – from anomaly detection to multilingual AI voice synthesis.

Beyond coding, Gesner has substantial client‑facing experience. He communicates directly with international clients, gathers requirements, manages projects, and ensures timely, quality delivery. His leadership background includes managing IT infrastructure at the Be Like Brit Orphanage, leading reconstruction teams as an NGO interpreter, and coordinating logistics for the J/P Haitian Relief Organization.

Fluent in English, French, Spanish, and Haitian Creole, Gesner is highly self‑motivated, organised, and proven to work effectively in remote environments. He is also willing to travel when necessary.

He is now seeking a contract Software Architect or Platform Engineer role where he can apply his unique combination of technical depth and product delivery to help organisations scale their systems efficiently.
"""

def get_cover_body_template():
    today = datetime.now().strftime("%B %d, %Y")
    return f"""{today}

RE: Senior Software Architect / Lead Platform Engineer (Contract) Position

Dear Hiring Manager,

I am writing to formally express my interest in the Senior Software Architect and Platform Engineer contract positions with your organization. Bringing a proven portfolio of 37 custom-engineered Python systems deployed to global production, I offer a potent blend of advanced systems infrastructure engineering, deep AI model integration, and proactive project leadership.

My recent flagship project – the System Health AI Monitor – demonstrates my ability to design enterprise‑grade observability platforms that combine real‑time metric streaming, automated anomaly detection, and AI‑generated predictive insights using Groq Llama 3.1. I have also built multilingual anti‑trafficking intelligence systems, full‑stack hospital management suites, and AI diagnostic assistants.

I am fully remote, available immediately, and willing to travel when required. I look forward to discussing how my experience in architecting scalable, AI‑enabled systems can add value to your engineering teams.

Sincerely,
Gesner Deslandes
Engineer‑in‑Chief, GlobalInternet.py
(509) 4738 5663 | deslandes78@gmail.com
"""

# ========== HELPER: get luminance from hex color ==========
def get_luminance(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) != 6:
        return 0.5  # fallback
    r = int(hex_color[0:2], 16) / 255.0
    g = int(hex_color[2:4], 16) / 255.0
    b = int(hex_color[4:6], 16) / 255.0
    # Standard luminance formula
    return 0.299 * r + 0.587 * g + 0.114 * b

# ========== THEME PRESETS ==========
BACKGROUND_PRESETS = {
    "CV (Resume)": "#ffffff",
    "SWOT Analysis": "linear-gradient(135deg, #e2e2e2 0%, #c9d6ff 100%)",
    "Executive Bio": "linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)",
    "Cover Letter": "#ffffff"
}

HEADER_COLOR_PRESETS = {
    "CV (Resume)": "#0a4c8c",
    "SWOT Analysis": "#1e293b",
    "Executive Bio": "#312e81",
    "Cover Letter": "#0f766e"
}

# ========== INITIALISE SESSION STATE ==========
if "cv_text" not in st.session_state:
    st.session_state.cv_text = get_cv_template()
if "swot_text" not in st.session_state:
    st.session_state.swot_text = get_swot_template()
if "bio_text" not in st.session_state:
    st.session_state.bio_text = get_bio_template()
if "cover_text" not in st.session_state:
    st.session_state.cover_text = get_cover_body_template()
if "last_doc_type" not in st.session_state:
    st.session_state.last_doc_type = "CV (Resume)"

# ========== SIDEBAR ==========
with st.sidebar:
    st.title("💼 Workspace Controller")
    doc_type = st.radio("Selected Focus Target:", ["CV (Resume)", "SWOT Analysis", "Executive Bio", "Cover Letter"])
    
    st.markdown("---")
    st.subheader("🎨 Profile Themes")
    
    # Reset colour pickers when document type changes
    if doc_type != st.session_state.last_doc_type:
        st.session_state.last_doc_type = doc_type
        st.rerun()
    
    # Background colour picker (solid only for auto text to work)
    default_bg = BACKGROUND_PRESETS[doc_type]
    bg_css = st.color_picker("Document Background Color", default_bg)
    
    header_color = st.color_picker("Primary Header Shield", HEADER_COLOR_PRESETS[doc_type])
    
    # Auto text colour option
    auto_text = st.checkbox("Auto Text Color (based on background)", value=True)
    
    if auto_text:
        # For solid background colours (ignore gradients), auto-select black or white
        # Since we use a color picker, bg_css is a solid hex color.
        luminance = get_luminance(bg_css)
        text_color = "#ffffff" if luminance < 0.5 else "#1a2a3a"
    else:
        text_color = st.color_picker("Body Text Ink", "#1a2a3a")
    
    font_family = st.selectbox("Typography Family", ["Segoe UI", "Arial", "Georgia", "Roboto"], index=0)

# ========== HTML GENERATOR ==========
def build_html_document(title, body_text, bg, text_col, heading_col, font, for_pdf=False):
    escaped_body = body_text.replace("\n", "<br>")
    
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
    
    if for_pdf:
        page_margin = "1.5cm"
        return f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>{title}</title>
<style>
@page {{ size: Letter; margin: {page_margin}; }}
body {{ margin: 0; padding: 0; background: {bg}; }}
.document-content {{ background: {bg}; color: {text_col}; font-family: {font}, sans-serif; padding: 0; }}
h2, h3, h4 {{ color: {heading_col}; }}
hr {{ margin: 1.5em 0; border: 1px solid {heading_col}; opacity: 0.3; }}
</style>
</head>
<body><div class="document-content">{header_html}<div style="font-size: 11pt; line-height: 1.5;">{escaped_body}</div></div></body>
</html>"""
    else:
        return f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>{title}</title>
<style>
body {{ margin: 20px; background: #f0f2f6; }}
.document-card {{ background: {bg}; color: {text_col}; font-family: {font}, sans-serif; padding: 30px; border-radius: 16px; box-shadow: 0 8px 20px rgba(0,0,0,0.1); }}
h2, h3, h4 {{ color: {heading_col}; }}
hr {{ margin: 1.5em 0; border: 1px solid {heading_col}; opacity: 0.3; }}
</style>
</head>
<body><div class="document-card">{header_html}<div>{escaped_body}</div></div></body>
</html>"""

# ========== EDITOR & PREVIEW ==========
st.subheader(f"📝 Content Control Engine: {doc_type}")

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

st.markdown("### 🖥️ Native Live Sandbox Preview")
st.markdown(f"<div style='background: {bg_css}; padding: 30px; border-radius: 12px; margin-bottom: 20px; border: 1px solid #ddd;'>", unsafe_allow_html=True)

col_logo, col_bio = st.columns([1, 4])
with col_logo:
    st.image(SRC_LOGO, width=100)
with col_bio:
    st.markdown(f"""
    <div style="text-align: right; font-family: 'Segoe UI', sans-serif; background-color: {header_color}; padding: 20px; border-radius: 8px; color: white;">
        <h1 style="margin:0; color:white; font-size:26px;">GESNER DESLANDES</h1>
        <p style="margin:2px 0; color:#ffd700; font-weight:bold; font-size:14px;">SOFTWARE ARCHITECT & AI SOLUTIONS ENGINEER</p>
        <p style="margin:0; color:#e0e0e0; font-size:12px;">deslandes78@gmail.com | +509 4738 5663 | Haiti</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown(f"<div style='color: {text_color}; font-family: {font_family}; white-space: pre-wrap;'>{active_payload}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ========== PDF EXPORT ==========
st.markdown("### 📥 Document Asset Distribution Channel")
live_pdf_html = build_html_document(doc_type, active_payload, bg_css, text_color, header_color, font_family, for_pdf=True)
pdf_export_bytes = HTML(string=live_pdf_html).write_pdf()
st.download_button(
    label=f"🏆 Compile & Export {doc_type} to PDF Sheet",
    data=pdf_export_bytes,
    file_name=f"gesner_deslandes_{doc_type.lower().replace(' ', '_')}.pdf",
    mime="application/pdf",
    use_container_width=True
)
