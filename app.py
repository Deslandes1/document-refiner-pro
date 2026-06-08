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

GlobalInternet.py – Founder & Engineer‑in‑Chief | 2021 – Present
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

RE: Senior Software Architect / Lead Platform Engineer (Contract) Position

Dear Hiring Manager,

I am writing to formally express my interest in the Senior Software Architect and Platform Engineer contract positions with your organization. Bringing a proven portfolio of 37 custom-engineered Python systems deployed to global production, I offer a potent blend of advanced systems infrastructure engineering, deep AI model integration, and proactive project leadership.

Throughout my tenure as Engineer-in-Chief at GlobalInternet.py, I have specialized in building robust solutions to complex computational problems. My recent system, the System Health AI Monitor, directly demonstrates my capacity to design and architect real-time observability platforms. This production tool simulates complex infrastructure metrics, executes multi-threaded anomaly tracking, and interfaces with specialized Groq Llama 3.1 pipelines to render instant, context-aware architectural feedback. 

Furthermore, I have architected high-impact solutions encompassing multilingual educational framework packages, enterprise asset software, and safety platforms built around international security models. I directly command the entire lifecycle of software execution—translating rough client operational hurdles into scalable system schemas, optimizing code maintainability via clean Python logic, writing comprehensive unit pipelines, and provisioning reliable, low-latency live operations on Streamlit Cloud using GitHub workflows.

Operating at a senior architectural tier, my capability to manage both codebases and client deliverables provides business units with an independent execution resource. I am fully prepared to manage high-availability systems remotely, synchronize across distributed international timelines, and travel on-site to assist core engineering squads whenever your roadmap dictates.

I welcome the opportunity to dive deep into your active platform milestones and outline exactly how my specialized AI integration workflows can immediately accelerate your team's velocity. Thank you for your time, consideration, and leadership review.

Sincerely,
Gesner Deslandes
Engineer‑in‑Chief, GlobalInternet.py
(509) 4738 5663 | deslandes78@gmail.com
"""

# ========== GLOBAL SVG BRAND COMPONENTS ==========
SVG_GLOBE_WITH_STARS = """
<div style="position: relative; width: 85px; height: 85px;">
    <!-- Golden Shining Stars Arc -->
    <div style="position: absolute; top: -14px; left: 50%; transform: translateX(-50%); display: flex; gap: 4px; z-index: 10; white-space: nowrap;">
        <span style="color: #ffd700; font-size: 13px; text-shadow: 0 0 6px #fff, 0 0 12px #ffd700;">★</span>
        <span style="color: #ffd700; font-size: 17px; text-shadow: 0 0 8px #fff, 0 0 16px #ffd700; margin-top: -3px;">★</span>
        <span style="color: #ffd700; font-size: 21px; text-shadow: 0 0 10px #fff, 0 0 20px #ffd700; margin-top: -6px;">★</span>
        <span style="color: #ffd700; font-size: 17px; text-shadow: 0 0 8px #fff, 0 0 16px #ffd700; margin-top: -3px;">★</span>
        <span style="color: #ffd700; font-size: 13px; text-shadow: 0 0 6px #fff, 0 0 12px #ffd700;">★</span>
    </div>
    <!-- Glow Effect Layer -->
    <div style="position: absolute; width: 75px; height: 75px; border-radius: 50%; background: radial-gradient(circle, rgba(0,180,216,0.45) 0%, transparent 70%); top: 5px; left: 5px;"></div>
    <!-- Custom Vector Blue Globe Logo -->
    <svg viewBox="0 0 100 100" style="width: 75px; height: 75px; position: absolute; top: 5px; left: 5px; filter: drop-shadow(0 0 6px rgba(0,180,216,0.85));">
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
    </svg>
</div>
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
    lines = content.split("\n")
    formatted_body = "<br>".join([line if line.strip() == "" else line for line in lines])

    if title in ["CV_Resume", "CV (Resume)"]:
        html_content = f"""
<div style="
    background: {heading_col};
    padding: 1.8rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    color: white;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 8px 24px rgba(0,0,0,0.15);
    min-height: 125px;
">
    <div style="display: flex; align-items: center; padding-left: 5px;">
        {SVG_GLOBE_WITH_STARS}
    </div>
    <div style="flex-grow: 1; text-align: right; font-family: 'Segoe UI', sans-serif; padding-left: 15px;">
        <h1 style="margin: 0; color: white; font-size: 2.1rem; font-weight: bold; line-height: 1.1;">Gesner Deslandes</h1>
        <p style="margin: 0.4rem 0 0.2rem; color: #f3f0df; font-size: 0.95rem; opacity: 0.9;">deslandes78@gmail.com | +509 4738 5663 | Haiti</p>
        <p style="margin: 0; color: #ffd700; font-size: 1.15rem; font-weight: bold; letter-spacing: 0.7px;">SOFTWARE ARCHITECT & AI SOLUTIONS ENGINEER</p>
    </div>
</div>
<div>
    {formatted_body}
</div>
"""
    elif title in ["Cover_Letter", "Cover Letter"]:
        html_content = f"""
<div style="
    background: {heading_col};
    padding: 1.8rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    color: white;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 8px 24px rgba(0,0,0,0.15);
    min-height: 125px;
">
    <div style="display: flex; align-items: center; padding-left: 5px;">
        {SVG_GLOBE_WITH_STARS}
    </div>
    <div style="flex-grow: 1; text-align: right; font-family: 'Segoe UI', sans-serif; padding-left: 15px;">
        <h1 style="margin: 0; color: white; font-size: 2.1rem; font-weight: bold; line-height: 1.1;">Gesner Deslandes</h1>
        <p style="margin: 0.4rem 0 0.2rem; color: #f3f0df; font-size: 0.95rem; opacity: 0.9;">deslandes78@gmail.com | +509 4738 5663 | Haiti</p>
        <p style="margin: 0; color: #ffd700; font-size: 1.15rem; font-weight: bold; letter-spacing: 0.7px;">SOFTWARE ARCHITECT & AI SOLUTIONS ENGINEER</p>
    </div>
</div>
<div>
    {formatted_body}
</div>
"""
    elif title in ["SWOT_Analysis", "SWOT Analysis"]:
        sea_bg_url = "http://googleusercontent.com/image_collection/image_retrieval/15036641857447707388_0"
        html_content = f"""
<div style="
    background: linear-gradient(rgba(15, 32, 39, 0.45), rgba(15, 32, 39, 0.75)), url('{sea_bg_url}') no-repeat center center;
    background-size: cover;
    padding: 1.8rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    color: white;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 8px 24px rgba(0,0,0,0.15);
    border: 1px solid rgba(255, 255, 255, 0.2);
    min-height: 125px;
">
    <div style="display: flex; align-items: center; padding-left: 5px;">
        {SVG_GLOBE_WITH_STARS}
    </div>
    <div style="flex-grow: 1; text-align: right; font-family: 'Georgia', serif; padding-left: 15px;">
        <h2 style="margin: 0; color: #ffd700; font-size: 1.55rem; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.85); line-height: 1.25;">Gesner Deslandes - Executive SWOT</h2>
        <p style="margin: 0.35rem 0 0; color: #f3f0df; font-size: 0.95rem; font-style: italic; opacity: 0.95; font-family: 'Segoe UI', sans-serif; letter-spacing: 0.5px; text-shadow: 1.5px 1.5px 3px rgba(0,0,0,0.85);">Engineer In Chief - Strategic Career Positioning</p>
    </div>
</div>
<div>
    {formatted_body}
</div>
"""
    elif title in ["Executive_Bio", "Executive Bio"]:
        html_content = f"""
<div style="
    background: {heading_col};
    padding: 1.8rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    color: white;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 8px 24px rgba(0,0,0,0.15);
    min-height: 125px;
">
    <div style="display: flex; align-items: center; padding-left: 5px;">
        {SVG_GLOBE_WITH_STARS}
    </div>
    <div style="flex-grow: 1; text-align: right; font-family: 'Georgia', serif; padding-left: 15px;">
        <h2 style="margin: 0; color: #ffd700; font-size: 1.65rem; font-weight: bold; line-height: 1.25; text-shadow: 1px 1px 3px rgba(0,0,0,0.5);">Gesner Deslandes - Executive Bio</h2>
    </div>
</div>
<div>
    {formatted_body}
</div>
"""
    else:
        html_content = f"<div>{formatted_body}</div>"
    
    if pdf_mode:
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
                padding: 0.5cm 1cm;
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

# Pre-generate current document bytes for seamless layout delivery
pdf_html = generate_html(st.session_state.doc_type.replace(" ", "_"), edited_text, bg_css, text_color, heading_color, font_family, pdf_mode=True)
pdf_bytes = HTML(string=pdf_html).write_pdf()

st.download_button(
    label="📥 Download Current Document as PDF",
    data=pdf_bytes,
    file_name=f"{st.session_state.doc_type.lower().replace(' ', '_')}.pdf",
    mime="application/pdf",
    use_container_width=True
)

st.info("💡 The PDF now fills the entire letter‑size sheet with safe internal content gutters – edge-to-edge colors with clean padding.")
