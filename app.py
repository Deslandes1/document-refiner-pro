import streamlit as st
import zipfile
import io
import base64
from datetime import datetime
from weasyprint import HTML

st.set_page_config(
    page_title="Document Refiner Pro | GlobalInternet.py",
    page_icon="📄",
    layout="wide"
)

st.markdown("""
<style>
    .stApp { background-color: #f0f2f6; }
    .stButton>button { background-color: #2c7be5; color: white; border-radius: 25px; width: 100%; }
</style>
""", unsafe_allow_html=True)

# ========== PROFESSIONAL TEMPLATES ==========
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

def get_cover_body_template():
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
    st.session_state.cover_text = get_cover_body_template()

# ========== SIDEBAR ==========
with st.sidebar:
    st.title("🎨 Document Refiner Pro")
    st.markdown("---")
    doc_type = st.radio("Select Document", ["CV (Resume)", "SWOT Analysis", "Executive Bio", "Cover Letter"], index=0)
    st.session_state.doc_type = doc_type
    
    st.markdown("---")
    st.subheader("🎨 Document Styling")
    bg_options = {
        "Sky Blue Gradient": "linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)",
        "Ocean Deep": "linear-gradient(135deg, #1e3c72 0%, #2a5298 100%)",
        "Sunset": "linear-gradient(135deg, #f5af19 0%, #f12711 100%)",
        "Mountain Mist": "linear-gradient(135deg, #e2e2e2 0%, #c9d6ff 100%)",
        "Dark Elegant": "linear-gradient(135deg, #0f2027 0%, #203a43 100%)",
        "Clean White": "#ffffff"
    }
    selected_bg = st.selectbox("Document Background", list(bg_options.keys()), index=0)
    bg_css = bg_options[selected_bg]
    
    text_color = st.color_picker("Text Color", "#1a2a3a")
    heading_color = st.color_picker("Heading Color", "#0a4c8c")
    font_family = st.selectbox("Font Family", ["Segoe UI", "Arial", "Georgia", "Roboto", "Calibri"], index=0)
    
    st.markdown("---")
    st.caption("Built by Gesner Deslandes | GlobalInternet.py")
    
    # Download all as ZIP (PDF)
    if st.button("📦 Download All Documents as ZIP (PDF)", use_container_width=True):
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zf:
            for name, text in [("CV_Resume", st.session_state.cv_text),
                               ("SWOT_Analysis", st.session_state.swot_text),
                               ("Executive_Bio", st.session_state.bio_text),
                               ("Cover_Letter", st.session_state.cover_text)]:
                html_str = generate_html(name, text, bg_css, text_color, heading_color, font_family, pdf_mode=True)
                pdf_bytes = HTML(string=html_str).write_pdf()
                zf.writestr(f"{name}.pdf", pdf_bytes)
        zip_buffer.seek(0)
        b64 = base64.b64encode(zip_buffer.read()).decode()
        href = f'<a href="data:application/zip;base64,{b64}" download="refined_documents.zip">Click here to download ZIP (PDF)</a>'
        st.markdown(href, unsafe_allow_html=True)

# ========== HELPER FUNCTION ==========
def generate_html(title, content, bg, text_col, heading_col, font, pdf_mode=False):
    if title == "Cover_Letter":
        html_content = f"""
<div style="text-align: center; background: {heading_col}; padding: 1rem; border-radius: 10px; margin-bottom: 1.5rem; color: white;">
    <h1 style="margin: 0; color: white; font-size: 1.5rem;">Gesner Deslandes</h1>
    <p style="margin: 0.3rem 0 0; opacity: 0.9;">deslandes78@gmail.com | +509 4738 5663 | Haiti</p>
</div>
<div>
    {content.replace(chr(10), '<br>')}
</div>
"""
    else:
        lines = content.split("\n")
        html_content = "<br>".join([line if line.strip() == "" else line for line in lines])
    
    if pdf_mode:
        # Full-page PDF style sheet handling background propagation cleanly
        style_extra = f"""
            @page {{
                size: Letter;
                margin: 1.5cm;
                background: {bg};
            }}
            html, body {{
                margin: 0;
                padding: 0;
                background: transparent;
                font-family: {font}, sans-serif;
                color: {text_col};
            }}
            .document {{
                width: 100%;
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                word-wrap: break-word;
            }}
            h1, h2, h3, h4 {{
                color: {heading_col};
                margin-top: 1em;
                margin-bottom: 0.5em;
                page-break-after: avoid;
            }}
        """
    else:
        # Screen preview: card format retained
        style_extra = f"""
            body {{
                margin: 0;
                padding: 2rem;
                background: #e6e9f0;
                font-family: {font}, sans-serif;
            }}
            .document {{
                max-width: 1000px;
                margin: 0 auto;
                background: {bg};
                border-radius: 20px;
                padding: 3rem 2.5rem;
                box-shadow: 0 20px 40px rgba(0,0,0,0.2);
                color: {text_col};
                word-wrap: break-word;
            }}
            h1, h2, h3, h4 {{
                color: {heading_col};
                margin-top: 1.2em;
                margin-bottom: 0.5em;
            }}
        """
    
    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        {style_extra}
        hr {{
            margin: 1.5em 0;
            border: 1px solid {heading_col};
            opacity: 0.3;
        }}
    </style>
</head>
<body>
    <div class="document">
        {html_content}
    </div>
</body>
</html>"""

# ========== MAIN AREA ==========
st.title(f"✍️ Edit & Preview: {st.session_state.doc_type}")

current_text = {
    "CV (Resume)": st.session_state.cv_text,
    "SWOT Analysis": st.session_state.swot_text,
    "Executive Bio": st.session_state.bio_text,
    "Cover Letter": st.session_state.cover_text
}[st.session_state.doc_type]

edited_text = st.text_area("Edit your document here (plain text – you can adjust any section)",
                            value=current_text,
                            height=500)

# Save changes
if st.session_state.doc_type == "CV (Resume)":
    st.session_state.cv_text = edited_text
elif st.session_state.doc_type == "SWOT Analysis":
    st.session_state.swot_text = edited_text
elif st.session_state.doc_type == "Executive Bio":
    st.session_state.bio_text = edited_text
else:
    st.session_state.cover_text = edited_text

# Live preview (screen mode)
st.subheader("📄 Live Preview")
preview_html = generate_html(st.session_state.doc_type.replace(" ", "_"), edited_text, bg_css, text_color, heading_color, font_family, pdf_mode=False)
st.components.v1.html(preview_html, height=650, scrolling=True)

# Compilation and Native Streamlit handling for Single Document Download
pdf_html = generate_html(st.session_state.doc_type.replace(" ", "_"), edited_text, bg_css, text_color, heading_color, font_family, pdf_mode=True)
pdf_bytes = HTML(string=pdf_html).write_pdf()

st.download_button(
    label="📥 Download Current Document as PDF",
    data=pdf_bytes,
    file_name=f"{st.session_state.doc_type.lower().replace(' ', '_')}.pdf",
    mime="application/pdf",
    use_container_width=True
)

st.info("💡 The PDF now fills the entire letter‑size sheet with the chosen background – no white margins or frames.")
