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

# ========== PROFESSIONAL TEMPLATES (same as before) ==========
def get_cv_template():
    return """Gesner Deslandes
deslandes78@gmail.com | +509 4738 5663 | Haiti

SOFTWARE ARCHITECT & AI SOLUTIONS ENGINEER

PROFESSIONAL SUMMARY

Results‑driven Software Architect with 4+ years of experience designing, building, and deploying 37 custom applications for global clients. Expert in Python, Streamlit, AI integration (Groq Llama 3.1), real‑time systems, and cloud deployment. Proven ability to lead full‑cycle product development, from requirements to deployment. Fluent in English, French, Spanish, Haitian Creole.

... (rest of CV as before) ...
"""

def get_swot_template():
    return """Executive SWOT Analysis

Prepared by: Gesner Deslandes
Date: June 2026
Purpose: Software Architect / Platform Engineer (Contract)

... (rest of SWOT as before) ...
"""

def get_bio_template():
    return """Executive Bio

Prepared for: Marcy / Career Coach Marcy
Prepared by: Gesner Deslandes
Date: June 2026

... (rest of Bio as before) ...
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
    
    # Download all as ZIP (PDFs)
    if st.button("📦 Download All Documents as ZIP (PDF)", use_container_width=True):
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zf:
            for name, text in [("CV_Resume", st.session_state.cv_text),
                               ("SWOT_Analysis", st.session_state.swot_text),
                               ("Executive_Bio", st.session_state.bio_text),
                               ("Cover_Letter", st.session_state.cover_text)]:
                html = generate_html(name, text, bg_css, text_color, heading_color, font_family)
                pdf = HTML(string=html).write_pdf()
                zf.writestr(f"{name}.pdf", pdf)
        zip_buffer.seek(0)
        b64 = base64.b64encode(zip_buffer.read()).decode()
        href = f'<a href="data:application/zip;base64,{b64}" download="refined_documents.zip">Click here to download ZIP (PDF)</a>'
        st.markdown(href, unsafe_allow_html=True)

# ========== HELPER FUNCTION ==========
def generate_html(title, content, bg, text_col, heading_col, font):
    if title == "Cover_Letter":
        html_content = f"""
<div style="text-align: center; background: {heading_col}; padding: 1.5rem; border-radius: 15px; margin-bottom: 2rem; color: white;">
    <h1 style="margin: 0; color: white;">Gesner Deslandes</h1>
    <p style="margin: 0.5rem 0 0; opacity: 0.9;">deslandes78@gmail.com | +509 4738 5663 | Haiti</p>
</div>
<div style="margin-bottom: 1rem;">
    {content.replace(chr(10), '<br>')}
</div>
"""
    else:
        lines = content.split("\n")
        html_content = "<br>".join([line if line.strip() == "" else line for line in lines])
    
    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{
            margin: 0;
            padding: 2rem;
            background: #e6e9f0;
            display: flex;
            justify-content: center;
            font-family: '{font}', sans-serif;
        }}
        .document {{
            max-width: 1000px;
            width: 100%;
            background: {bg};
            border-radius: 20px;
            padding: 3rem 2.5rem;
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
            color: {text_col};
        }}
        h1, h2, h3, h4 {{
            color: {heading_col};
            margin-top: 1.2em;
            margin-bottom: 0.5em;
        }}
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

# Live preview (HTML)
st.subheader("📄 Live Preview")
preview_html = generate_html(st.session_state.doc_type.replace(" ", "_"), edited_text, bg_css, text_color, heading_color, font_family)
st.components.v1.html(preview_html, height=650, scrolling=True)

# Download current document as PDF
if st.button("📥 Download Current Document as PDF", use_container_width=True):
    pdf_bytes = HTML(string=preview_html).write_pdf()
    st.download_button(
        label="✅ Click to save PDF",
        data=pdf_bytes,
        file_name=f"{st.session_state.doc_type.lower().replace(' ', '_')}.pdf",
        mime="application/pdf",
        use_container_width=True
    )

st.info("The PDF will preserve all colours, gradients, and fonts. The ZIP download also creates PDFs directly.")
