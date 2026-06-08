import streamlit as st
import zipfile
import io
import base64
import asyncio
import tempfile
import os
from datetime import datetime
from weasyprint import HTML
import edge_tts

st.set_page_config(
    page_title="Document Refiner Pro | GLOBALINTERNET.PY",
    page_icon="📄",
    layout="wide"
)

# ========== LANGUAGE DICTIONARIES ==========
TEXTS = {
    "English": {
        "title": "📄 Document Refiner Pro",
        "workspace": "💼 Workspace Controller",
        "focus": "Selected Focus Target:",
        "theme": "🎨 Profile Themes",
        "bg_mode": "Background mode",
        "preset": "Preset Theme",
        "custom_bg": "Custom Colour",
        "header_shield": "Primary Header Shield",
        "auto_text": "Auto Text Color (based on background)",
        "body_text": "Body Text Ink",
        "typography": "Typography Family",
        "editor": "📝 Content Control Engine:",
        "live_preview": "🖥️ Native Live Sandbox Preview",
        "export": "📥 Document Asset Distribution Channel",
        "export_btn": "🏆 Compile & Export {doc} to PDF Sheet",
        "fallback_btn": "⬇️ Fallback Export {doc} (White Background)",
        "read_btn": "🔊 Read this document aloud",
        "explain_btn": "🎙️ App Explanation",
        "explain_title": "How Document Refiner Pro works",
        "explain_text_en": "Document Refiner Pro allows you to edit and style professional documents (CV, SWOT Analysis, Executive Bio, Cover Letter). You can change background color, header shield color, text color, and font. The live preview updates instantly. Then you can download a polished PDF. This tool uses WeasyPrint for PDF generation and edge-tts for AI voice reading.",
        "explain_text_fr": "Document Refiner Pro vous permet d'éditer et de styliser des documents professionnels (CV, analyse SWOT, biographie, lettre de motivation). Vous pouvez changer la couleur de fond, la couleur de l'en‑tête, la couleur du texte et la police. L'aperçu en direct se met à jour instantanément. Vous pouvez ensuite télécharger un PDF soigné. Cet outil utilise WeasyPrint pour la génération de PDF et edge-tts pour la lecture vocale IA.",
        "explain_text_es": "Document Refiner Pro le permite editar y diseñar documentos profesionales (CV, análisis FODA, biografía ejecutiva, carta de presentación). Puede cambiar el color de fondo, el color del encabezado, el color del texto y la fuente. La vista previa en vivo se actualiza al instante. Luego puede descargar un PDF pulido. Esta herramienta utiliza WeasyPrint para generar PDF y edge-tts para lectura por voz IA."
    },
    "French": {
        "title": "📄 Document Refiner Pro",
        "workspace": "💼 Contrôleur de l'espace de travail",
        "focus": "Cible sélectionnée :",
        "theme": "🎨 Thèmes de profil",
        "bg_mode": "Mode d'arrière‑plan",
        "preset": "Thème prédéfini",
        "custom_bg": "Couleur personnalisée",
        "header_shield": "Couleur de l'en‑tête",
        "auto_text": "Couleur automatique (selon fond)",
        "body_text": "Couleur du texte",
        "typography": "Famille de polices",
        "editor": "📝 Moteur d'édition :",
        "live_preview": "🖥️ Aperçu en direct",
        "export": "📥 Canal de distribution",
        "export_btn": "🏆 Générer et exporter {doc} en PDF",
        "fallback_btn": "⬇️ Export de secours {doc} (fond blanc)",
        "read_btn": "🔊 Lire ce document à voix haute",
        "explain_btn": "🎙️ Explication de l'application",
        "explain_title": "Comment fonctionne Document Refiner Pro",
        "explain_text_en": "Document Refiner Pro vous permet d'éditer et de styliser des documents professionnels...",
        "explain_text_fr": "Document Refiner Pro vous permet d'éditer et de styliser des documents professionnels (CV, analyse SWOT, biographie, lettre de motivation). Vous pouvez changer la couleur de fond, la couleur de l'en‑tête, la couleur du texte et la police. L'aperçu en direct se met à jour instantanément. Vous pouvez ensuite télécharger un PDF soigné. Cet outil utilise WeasyPrint pour la génération de PDF et edge-tts pour la lecture vocale IA.",
        "explain_text_es": "Document Refiner Pro le permite editar y diseñar documentos profesionales..."
    },
    "Spanish": {
        "title": "📄 Document Refiner Pro",
        "workspace": "💼 Controlador del espacio de trabajo",
        "focus": "Objetivo seleccionado:",
        "theme": "🎨 Temas de perfil",
        "bg_mode": "Modo de fondo",
        "preset": "Tema predefinido",
        "custom_bg": "Color personalizado",
        "header_shield": "Color del encabezado",
        "auto_text": "Color automático (según fondo)",
        "body_text": "Color del texto",
        "typography": "Familia de fuentes",
        "editor": "📝 Editor de contenido:",
        "live_preview": "🖥️ Vista previa en vivo",
        "export": "📥 Canal de distribución",
        "export_btn": "🏆 Compilar y exportar {doc} a PDF",
        "fallback_btn": "⬇️ Exportación de respaldo {doc} (fondo blanco)",
        "read_btn": "🔊 Leer este documento en voz alta",
        "explain_btn": "🎙️ Explicación de la aplicación",
        "explain_title": "Cómo funciona Document Refiner Pro",
        "explain_text_en": "Document Refiner Pro le permite editar y diseñar documentos profesionales...",
        "explain_text_fr": "Document Refiner Pro vous permet d'éditer et de styliser des documents professionnels...",
        "explain_text_es": "Document Refiner Pro le permite editar y diseñar documentos profesionales (CV, análisis FODA, biografía ejecutiva, carta de presentación). Puede cambiar el color de fondo, el color del encabezado, el color del texto y la fuente. La vista previa en vivo se actualiza al instante. Luego puede descargar un PDF pulido. Esta herramienta utiliza WeasyPrint para generar PDF y edge-tts para lectura por voz IA."
    }
}

# ========== VOICE MAPPING ==========
VOICE_MAP = {
    "English": "en-US-JennyNeural",
    "French": "fr-FR-DeniseNeural",
    "Spanish": "es-ES-ElviraNeural"
}

# ========== LOGO ==========
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

# ========== TEMPLATES (unchanged) ==========
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

# ========== PRESETS ==========
BACKGROUND_PRESETS = {
    "CV (Resume)": "#ffffff",
    "SWOT Analysis": "linear-gradient(135deg, #e2e2e2 0%, #c9d6ff 100%)",
    "Executive Bio": "#ffffff",
    "Cover Letter": "#ffffff"
}
HEADER_COLOR_PRESETS = {
    "CV (Resume)": "#0a4c8c",
    "SWOT Analysis": "#1e293b",
    "Executive Bio": "#312e81",
    "Cover Letter": "#0f766e"
}

# ========== HELPERS ==========
def get_luminance(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) != 6:
        return 0.5
    r = int(hex_color[0:2], 16) / 255.0
    g = int(hex_color[2:4], 16) / 255.0
    b = int(hex_color[4:6], 16) / 255.0
    return 0.299 * r + 0.587 * g + 0.114 * b

async def text_to_speech(text, voice, output_path):
    comm = edge_tts.Communicate(text, voice)
    await comm.save(output_path)

def generate_audio(text, lang):
    voice = VOICE_MAP.get(lang, "en-US-JennyNeural")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp_path = tmp.name
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(text_to_speech(text, voice, tmp_path))
    loop.close()
    with open(tmp_path, "rb") as f:
        audio_bytes = f.read()
    os.unlink(tmp_path)
    return audio_bytes

# ========== SESSION STATE ==========
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
if "lang" not in st.session_state:
    st.session_state.lang = "English"

# ========== SIDEBAR ==========
with st.sidebar:
    lang = st.selectbox("🌐 Language", ["English", "French", "Spanish"], key="lang_selector")
    if lang != st.session_state.lang:
        st.session_state.lang = lang
        st.rerun()
    texts = TEXTS[st.session_state.lang]
    
    st.title(texts["workspace"])
    doc_type = st.radio(texts["focus"], ["CV (Resume)", "SWOT Analysis", "Executive Bio", "Cover Letter"])
    
    st.markdown("---")
    st.subheader(texts["theme"])
    
    if doc_type != st.session_state.last_doc_type:
        st.session_state.last_doc_type = doc_type
        st.rerun()
    
    bg_mode = st.radio(texts["bg_mode"], [texts["preset"], texts["custom_bg"]], index=0)
    if bg_mode == texts["preset"]:
        bg_css = BACKGROUND_PRESETS[doc_type]
    else:
        default_solid = "#ffffff"
        bg_css = st.color_picker(texts["custom_bg"], default_solid)
    
    header_color = st.color_picker(texts["header_shield"], HEADER_COLOR_PRESETS[doc_type])
    auto_text = st.checkbox(texts["auto_text"], value=True)
    if auto_text:
        if bg_css.startswith("linear-gradient"):
            text_color = "#1a2a3a"
        else:
            luminance = get_luminance(bg_css)
            text_color = "#ffffff" if luminance < 0.5 else "#1a2a3a"
    else:
        text_color = st.color_picker(texts["body_text"], "#1a2a3a")
    font_family = st.selectbox(texts["typography"], ["Segoe UI", "Arial", "Georgia", "Roboto"], index=0)
    
    st.markdown("---")
    if st.button(texts["explain_btn"], use_container_width=True):
        explanation = texts["explain_text_" + st.session_state.lang.split("_")[0][:2].lower()]
        if not explanation:
            explanation = texts["explain_text_en"]
        audio_bytes = generate_audio(explanation, st.session_state.lang)
        st.audio(audio_bytes, format="audio/mp3")

# ========== DOCUMENT EDITOR ==========
st.subheader(texts["editor"].format(doc_type))

if doc_type == "CV (Resume)":
    st.session_state.cv_text = st.text_area("", value=st.session_state.cv_text, height=400)
    active_payload = st.session_state.cv_text
elif doc_type == "SWOT Analysis":
    st.session_state.swot_text = st.text_area("", value=st.session_state.swot_text, height=400)
    active_payload = st.session_state.swot_text
elif doc_type == "Executive Bio":
    st.session_state.bio_text = st.text_area("", value=st.session_state.bio_text, height=400)
    active_payload = st.session_state.bio_text
else:
    st.session_state.cover_text = st.text_area("", value=st.session_state.cover_text, height=400)
    active_payload = st.session_state.cover_text

# Read document aloud button
if st.button(texts["read_btn"]):
    with st.spinner("Generating speech..."):
        audio_bytes = generate_audio(active_payload, st.session_state.lang)
        st.audio(audio_bytes, format="audio/mp3")

# ========== PREVIEW ==========
st.markdown(f"### {texts['live_preview']}")
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
st.markdown(f"### {texts['export']}")

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

try:
    pdf_html = build_html_document(doc_type, active_payload, bg_css, text_color, header_color, font_family, for_pdf=True)
    pdf_bytes = HTML(string=pdf_html).write_pdf()
    st.download_button(
        label=texts["export_btn"].format(doc=doc_type),
        data=pdf_bytes,
        file_name=f"gesner_deslandes_{doc_type.lower().replace(' ', '_')}.pdf",
        mime="application/pdf",
        use_container_width=True
    )
except Exception as e:
    st.error(f"PDF error: {e}")
    # Fallback with white background
    fallback_html = build_html_document(doc_type, active_payload, "#ffffff", "#1a2a3a", header_color, font_family, for_pdf=True)
    fallback_bytes = HTML(string=fallback_html).write_pdf()
    st.download_button(
        label=texts["fallback_btn"].format(doc=doc_type),
        data=fallback_bytes,
        file_name=f"gesner_deslandes_{doc_type.lower().replace(' ', '_')}_fallback.pdf",
        mime="application/pdf",
        use_container_width=True
    )
