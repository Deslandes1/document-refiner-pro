import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Document Refiner Pro | GlobalInternet.py",
    page_icon="📄",
    layout="wide"
)

# ========== PROFESSIONAL TEMPLATES (same as before) ==========
def get_cv_template():
    return """Gesner Deslandes
deslandes78@gmail.com | +509 4738 5663 | Haiti

SOFTWARE ARCHITECT & AI SOLUTIONS ENGINEER

PROFESSIONAL SUMMARY

Results‑driven Software Architect with 4+ years of experience designing, building, and deploying 37 custom applications for global clients. Expert in Python, Streamlit, AI integration (Groq Llama 3.1), real‑time systems, and cloud deployment. Proven ability to lead full‑cycle product development, from requirements to deployment. Fluent in English, French, Spanish, Haitian Creole.

CORE COMPETENCIES

- System Architecture: Real‑time data pipelines, observability platforms, API design
- AI & Machine Learning: LLM integration, prompt engineering, anomaly detection
- Full‑Stack Development: Python, Streamlit, Pandas, Plotly, REST APIs
- Cloud & DevOps: Streamlit Cloud, GitHub, secrets management, CI/CD concepts
- Multilingual Solutions: English, French, Spanish UI and AI voice synthesis

KEY PROJECTS

System Health AI Monitor | Architect & Creator
Live: https://system-health-ai-monitor-important-9bemdyosmbfmtx4t8wygbv.streamlit.app/
- Designed and deployed a real‑time observability tool that simulates server metrics, detects anomalies, and provides AI‑powered predictive insights using Groq Llama 3.1.
- Integrated multilingual UI (English, French, Spanish) and AI voice explanation using edge‑tts.

SafeHaven – Anti‑Trafficking AI | Lead Developer
Live: https://call-for-code-ai-global-challenge-2026-jimupcwzzyntghxdwxpbg9.streamlit.app/
- Built an AI‑powered early warning system that analyzes user‑submitted situations, flags trafficking indicators, and provides anonymous reporting.
- Used Groq LLM to generate risk assessments and actionable advice.

Hospital Management System | Full‑Stack Developer
Live: https://hospital-management-system-software-built-by-gesner-deslandes.streamlit.app/
- Developed a complete hospital management suite with patient registration, EMR, billing, pharmacy, lab, radiology, and AI diagnostic assistant.
- Integrated real‑time alerts and multilingual support.

PROFESSIONAL EXPERIENCE

GlobalInternet.py – Founder & Engineer‑in‑Chief | 2021 – Present
- Delivered 37 custom Python applications (voting systems, BI dashboards, AI chatbots, educational platforms, self‑driving car simulator).
- Led all phases: client consultation, requirements gathering, architecture design, coding, deployment, and documentation.
- Managed full‑stack development using Streamlit, Pandas, Plotly, and integrated third‑party APIs (Groq, edge‑tts).
- Deployed applications on Streamlit Cloud; used GitHub for version control.

Be Like Brit Orphanage – Technology Coordinator | 2021 – Present
- Manage IT infrastructure (laptops, tablets, Zoom, daily support) for 50+ users.
- Troubleshoot hardware/software issues independently.

EDUCATION & CERTIFICATIONS

- Self‑taught Software Engineer (continuous learning)
- Vocational Training – American English
- Office Computing Certification (2000)
- High School Graduate

LANGUAGES

- English – Professional working proficiency
- French – Professional working proficiency
- Spanish – Conversational
- Haitian Creole – Native

REFERENCES

- Teresa Lang Ehlert: tbtrekkin@gmail.com
- Charles Zerr MD: +1 620 952 0074
"""

def get_swot_template():
    return """Executive SWOT Analysis

Prepared by: Gesner Deslandes
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
Prepared by: Gesner Deslandes
Date: June 2026

Gesner Deslandes is the Founder, Owner, and Engineer‑in‑Chief of GlobalInternet.py, a software development company that builds custom Python and AI‑powered solutions for clients worldwide. With over four years of hands‑on experience, he has delivered 37 unique software products, including real‑time system health monitors, AI‑powered anti‑trafficking platforms, hospital management systems, and multilingual educational tools.

His technical expertise spans system architecture, full‑stack development (Python, Streamlit, Pandas, Plotly), AI integration (Groq Llama 3.1), cloud deployment (Streamlit Cloud, GitHub), and real‑time observability. He designs and builds end‑to‑end solutions that solve real problems – from anomaly detection to multilingual AI voice synthesis.

Beyond coding, Gesner has substantial client‑facing experience. He communicates directly with international clients, gathers requirements, manages projects, and ensures timely, quality delivery. His leadership background includes managing IT infrastructure at the Be Like Brit Orphanage, leading reconstruction teams as an NGO interpreter, and coordinating logistics for the J/P Haitian Relief Organization.

Fluent in English, French, Spanish, and Haitian Creole, Gesner is highly self‑motivated, organised, and proven to work effectively in remote environments. He is also willing to travel when necessary.

He is now seeking a contract Software Architect or Platform Engineer role where he can apply his unique combination of technical depth and product delivery to help organisations scale their systems efficiently.
"""

def get_cover_template():
    today = datetime.now().strftime("%B %d, %Y")
    return f"""{today}

RE: Software Architect (Contract) Role

Dear Hiring Manager,

I am writing to express my strong interest in the Software Architect (Contract) role. With over four years of experience designing, building, and deploying 37 custom Python applications for global clients, I bring a rare combination of hands‑on system architecture, AI integration, and client‑facing delivery.

My recent project – the System Health AI Monitor – demonstrates my ability to design real‑time observability tools that integrate AI for predictive anomaly detection. It simulates server metrics, automatically alerts on anomalies, and uses Groq Llama 3.1 to provide actionable recommendations. This project showcases my architecture‑level thinking and full‑stack implementation.

I have also delivered AI‑powered anti‑trafficking platforms, hospital management systems with AI diagnostic assistants, and multilingual educational software. I manage the entire software lifecycle: requirements, architecture, coding, deployment, documentation, and client support.

I am fully remote, available immediately, and willing to travel when required. I look forward to discussing how my experience in building scalable, AI‑enabled systems can add value to your engineering teams.

Sincerely,
Gesner Deslandes
Engineer‑in‑Chief, GlobalInternet.py
(509) 4738 5663 | deslandes78@gmail.com
"""

# ========== SESSION STATE ==========
if "doc_type" not in st.session_state:
    st.session_state.doc_type = "CV (Resume)"
if "cv_text" not in st.session_state:
    st.session_state.cv_text = get_cv_template()
if "swot_text" not in st.session_state:
    st.session_state.swot_text = get_swot_template()
if "bio_text" not in st.session_state:
    st.session_state.bio_text = get_bio_template()
if "cover_text" not in st.session_state:
    st.session_state.cover_text = get_cover_template()

# ========== SIDEBAR ==========
with st.sidebar:
    st.title("📄 Document Refiner Pro")
    st.markdown("---")
    doc_type = st.radio("Select Document", ["CV (Resume)", "SWOT Analysis", "Executive Bio", "Cover Letter"], index=0)
    st.session_state.doc_type = doc_type
    st.markdown("---")
    st.caption("Built by Gesner Deslandes | GlobalInternet.py")

# ========== MAIN AREA ==========
st.title(f"✍️ Edit & Download: {st.session_state.doc_type}")

current_text = {
    "CV (Resume)": st.session_state.cv_text,
    "SWOT Analysis": st.session_state.swot_text,
    "Executive Bio": st.session_state.bio_text,
    "Cover Letter": st.session_state.cover_text
}[st.session_state.doc_type]

edited_text = st.text_area("Edit your document here (plain text)", value=current_text, height=500)

# Save changes
if st.session_state.doc_type == "CV (Resume)":
    st.session_state.cv_text = edited_text
elif st.session_state.doc_type == "SWOT Analysis":
    st.session_state.swot_text = edited_text
elif st.session_state.doc_type == "Executive Bio":
    st.session_state.bio_text = edited_text
else:
    st.session_state.cover_text = edited_text

# Download as plain text file
st.download_button(
    label="📥 Download as TXT File",
    data=edited_text,
    file_name=f"{st.session_state.doc_type.lower().replace(' ', '_')}.txt",
    mime="text/plain",
    use_container_width=True
)

st.info("This downloads a plain text file. You can open it in any text editor (including Opera).")
