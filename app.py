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
Gesner Deslandes brings a rare combination of software architecture skills, AI integration, and direct client success. His ability to deliver production‑ready systems end‑to‑end makes him a strong candidate for senior‑level contract roles. With the right opportunity and mentorship
