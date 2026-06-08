import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Document Refiner Pro | GlobalInternet.py",
    page_icon="📄",
    layout="wide"
)

# ========== CUSTOM CSS for the preview (dynamic) ==========
# We'll use a placeholder; actual styling will be injected in the preview.

st.markdown("""
<style>
    .stApp {
        background-color: #f0f2f6;
    }
    .preview-box {
        background-color: white;
        border-radius: 15px;
        padding: 2rem;
        margin-top: 1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .stButton>button {
        background-color: #2c7be5;
        color: white;
        border-radius: 25px;
    }
</style>
""", unsafe_allow_html=True)

# ========== INITIAL CONTENT (your refined documents) ==========
default_cv = """Gesner Deslandes
deslandes78@gmail.com | +509 4738 5663 | Haiti | DOB: 20/11/79

Software Builder | Python Developer | AI Enthusiast | Technology Coordinator

Professional Objective

Seeking a partnership or client‑facing role where technical expertise and relationship management intersect. Open to collaborating with global companies to deliver high‑value solutions, bridge technical delivery with client success, and contribute to business growth. Available for remote work and willing to travel when required.

Exceptionally driven leader and manager with over 4 years of experience building custom Python software for international clients. Proven ability to learn quickly, solve complex problems, and deliver production‑ready applications.

Technical Skills

Languages: Python (advanced), JavaScript, HTML/CSS, SQL
Frameworks & Libraries: Streamlit, TensorFlow, OpenCV, Pygame, Pandas, NumPy
Tools & Platforms: Git, GitHub, Supabase, VS Code, Linux, Windows
Areas: Web applications, AI/ML models, automation, data dashboards, educational software, hardware integration, self‑driving simulations
Other: Full‑cycle software development (requirements → deployment), API integration, database design, technical documentation

Professional Experience

GlobalInternet.py – Founder, Owner & Director – Python Software Builder
2021 – Present
- Built and delivered 37 custom Python applications to clients worldwide (see portfolio).
- Developed AI‑powered solutions including chatbots, image classifiers, and medical literature assistants.
- Created full‑stack web applications (voting systems, school management, business dashboards).
- Designed educational software with audio support and multi‑language interfaces.
- Wrote clean, maintainable code; managed version control with Git/GitHub.
- Deployed apps on Streamlit Cloud; integrated Supabase for real‑time features.

Be Like Brit Orphanage – Haiti – Technology Coordinator
2021 – Present
- Manage IT infrastructure: laptops, tablets, Zoom meetings, daily technical support.
- Troubleshoot hardware and software issues independently.
- Ensure smooth digital operations for educational and administrative teams.
- Transferable skills: problem‑solving, user support, system maintenance.

Interpreting Tourist Services – Haiti – CEO
- Organized personalized tourism for NGOs and individuals.
- Transferable skills: client communication, project management, logistics.

Additional Roles (transferable skills)
- Accounting Assistant – Be Like Brit.org
- Document Translator – United Kingdom Glossary & United States Work‑Rise Company
- J/P Haitian Relief Organization – Fleet Manager / Dispatcher / Driver / Translator for Structural Engineering Team
- International Medical Team – Driver and Pharmaceutical Assistant
- International Child Care – Medical Interpreter
- Can‑Do (NGO) – Team Leader and Interpreter
- Printing Company – Driver
- Be Like Brit – Secondary English Teacher (Preschool to NS4) – September 2020

Software Portfolio (37 Products – All Built with Python)

Full source code, documentation, and deployment guides included.
View the complete portfolio: https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/

(Full list available upon request – over 37 applications from voting software to self‑driving car simulator.)

Education & Training

- Vocational Training School – American English
- Diesel Institute of Haiti – Diesel Mechanic
- Office Computing Certification (October 2000)
- High School Graduate

Languages

- English – Professional working proficiency
- French – Professional working proficiency
- Spanish – Conversational
- Haitian Creole – Native

References

- Teresa Lang Ehlert: tbtrekkin@gmail.com
- Charles Zerr MD: +1 620 952 0074
"""

default_swot = """Executive SWOT Analysis

Prepared by: Gesner Deslandes
Date: June 2026
Purpose: Partnership / Client‑Facing Opportunities

Strengths (Internal)

- Strong technical foundation in Python, WordPress, full‑stack development, and AI/ML.
- Proven ability to build and deliver 37 custom software applications to global clients.
- Direct client‑facing experience including requirements gathering, project management, and post‑delivery support.
- Self‑motivated, organized, and effective in remote work environments.
- Willing to travel when required.
- Multilingual: English, French, Spanish, Haitian Creole.
- Demonstrated leadership as founder of GlobalInternet.py and former team leader roles.
- Fast learner and adaptable to new technologies.

Weaknesses (Internal)

- Limited experience in large corporate team structures.
- No formal computer science degree (compensated by practical experience and portfolio).
- Based in Haiti – potential time zone differences with USA and Canada.
- Less exposure to enterprise‑level project management frameworks (e.g., Agile/Scrum certifications).

Opportunities (External)

- Leverage technical background into client‑facing partnership, customer success, or technical account management roles.
- Grow within a structured organization with clear career progression.
- Expand professional network in the USA and Canadian markets.
- Use multilingual skills to support international clients.
- Potential to transition from founder to a collaborative team environment that offers mentorship and resources.

Threats (External)

- Highly competitive job market for client‑facing tech roles.
- Preference for candidates with local degrees or specific industry certifications.
- Economic and political instability in Haiti may affect travel or visa processes.
- Remote work may limit visibility compared to onsite candidates.

Conclusion

Gesner Deslandes brings a rare combination of technical depth and client‑centric experience. His strengths in Python development, AI solutions, and direct client communication are highly transferable to partnership or customer success roles. With the right opportunity and mentorship, he can deliver significant value to a forward‑looking organization.
"""

default_bio = """Executive Bio

Prepared for: Marcy / Career Coach Marcy (Certified Career & Business Coach, Recruiter & HR Professional)
Prepared by: Gesner Deslandes
Date: June 2026

Gesner Deslandes is the Founder, Owner, and Engineer‑in‑Chief of GlobalInternet.py, a software development company that builds custom Python and WordPress solutions for clients worldwide. With over four years of hands‑on experience, he has delivered 37 unique software products, including AI‑powered chatbots, secure voting systems, full‑stack web applications, educational platforms, and a self‑driving car simulator.

His technical expertise spans Python, JavaScript, HTML/CSS, SQL, and frameworks such as Streamlit, TensorFlow, and Pandas. He is also proficient in WordPress development, including page builders like Elementor, WPBakery, and Gutenberg, as well as child theme customization. Gesner manages the full software development lifecycle – from client consultation to deployment and documentation – making him an effective bridge between technical delivery and client success.

Beyond coding, he has substantial client‑facing experience: communicating directly with international clients, gathering requirements, managing projects, and ensuring timely, quality delivery. His leadership background includes managing IT infrastructure at the Be Like Brit Orphanage, leading reconstruction teams as an NGO interpreter, and coordinating logistics as a fleet manager for the J/P Haitian Relief Organization.

Gesner is fluent in English, French, Spanish, and Haitian Creole. He is highly self‑motivated, organized, and proven to work effectively in remote environments. He is also willing to travel when necessary.

He is now seeking a partnership or client‑facing role where he can apply his unique combination of technical depth and relationship management to help an organization grow while continuing his own professional development.
"""

default_cover = """Dear Hiring Team,

I am writing to express my strong interest in the Software Architect (Contract) role. With over four years of experience designing, building, and deploying 37 custom Python applications for global clients, I bring a rare combination of hands‑on system architecture, AI integration, and client‑facing delivery.

My recent project – the System Health AI Monitor – demonstrates my ability to design real‑time observability tools that integrate AI for predictive anomaly detection. I have also built multilingual platforms, AI‑powered diagnostic assistants, and full‑stack web applications from concept to deployment.

I am fully remote, available immediately, and willing to travel. I look forward to discussing how my architecture‑level thinking can add value to your team.

Sincerely,
Gesner Deslandes
Engineer‑in‑Chief, GlobalInternet.py
(509) 4738 5663 | deslandes78@gmail.com
"""

# ========== SESSION STATE ==========
if "doc_type" not in st.session_state:
    st.session_state.doc_type = "CV (Resume)"
if "cv_text" not in st.session_state:
    st.session_state.cv_text = default_cv
if "swot_text" not in st.session_state:
    st.session_state.swot_text = default_swot
if "bio_text" not in st.session_state:
    st.session_state.bio_text = default_bio
if "cover_text" not in st.session_state:
    st.session_state.cover_text = default_cover

# ========== SIDEBAR ==========
with st.sidebar:
    st.title("🎨 Document Refiner Pro")
    st.markdown("---")
    doc_type = st.radio("Select Document", ["CV (Resume)", "SWOT Analysis", "Executive Bio", "Cover Letter"], index=0)
    st.session_state.doc_type = doc_type
    
    st.markdown("---")
    st.subheader("🎨 Style Settings")
    bg_options = {
        "Sky Blue Gradient": "linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)",
        "Ocean Deep": "linear-gradient(135deg, #1e3c72 0%, #2a5298 100%)",
        "Sunset": "linear-gradient(135deg, #f5af19 0%, #f12711 100%)",
        "Mountain Mist": "linear-gradient(135deg, #e2e2e2 0%, #c9d6ff 100%)",
        "Dark Elegant": "linear-gradient(135deg, #0f2027 0%, #203a43 100%)",
        "Clean White": "#ffffff"
    }
    selected_bg = st.selectbox("Background Style", list(bg_options.keys()), index=0)
    bg_css = bg_options[selected_bg]
    
    text_color = st.color_picker("Text Color", "#1a2a3a")
    accent_color = st.color_picker("Accent Color (headings)", "#0a4c8c")
    st.markdown("---")
    st.caption("Built by Gesner Deslandes | GlobalInternet.py")

# ========== MAIN AREA ==========
st.title(f"✍️ Edit & Preview: {st.session_state.doc_type}")

# Editor
edited_text = st.text_area("Edit your document here (plain text, you can format with simple markdown)", 
                           value={
                               "CV (Resume)": st.session_state.cv_text,
                               "SWOT Analysis": st.session_state.swot_text,
                               "Executive Bio": st.session_state.bio_text,
                               "Cover Letter": st.session_state.cover_text
                           }[st.session_state.doc_type],
                           height=400)

# Save edits back to session state
if st.session_state.doc_type == "CV (Resume)":
    st.session_state.cv_text = edited_text
elif st.session_state.doc_type == "SWOT Analysis":
    st.session_state.swot_text = edited_text
elif st.session_state.doc_type == "Executive Bio":
    st.session_state.bio_text = edited_text
else:
    st.session_state.cover_text = edited_text

# Preview with live styling
st.subheader("📄 Live Preview (Stylized)")
preview_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            background: {bg_css};
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding: 2rem;
            margin: 0;
            color: {text_color};
        }}
        .document-container {{
            max-width: 900px;
            margin: 0 auto;
            background: rgba(255,255,255,0.85);
            border-radius: 20px;
            padding: 2rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            backdrop-filter: blur(2px);
        }}
        h1, h2, h3, h4 {{
            color: {accent_color};
        }}
        hr {{
            border: 1px solid {accent_color};
        }}
        .footer {{
            text-align: center;
            margin-top: 2rem;
            font-size: 0.8rem;
            color: {text_color};
            opacity: 0.7;
        }}
    </style>
</head>
<body>
    <div class="document-container">
        {edited_text.replace(chr(10), '<br>')}
        <div class="footer">
            Document refined by Gesner Deslandes – GlobalInternet.py
        </div>
    </div>
</body>
</html>
"""

st.components.v1.html(preview_html, height=600, scrolling=True)

# Download button
st.download_button(
    label="📥 Download as HTML (then open in browser and print to PDF)",
    data=preview_html,
    file_name=f"{st.session_state.doc_type.lower().replace(' ', '_')}_refined.html",
    mime="text/html",
    use_container_width=True
)

st.info("Tip: After downloading, open the HTML file in your browser, press Ctrl+P (or Cmd+P) and choose 'Save as PDF' to get a professional PDF document.")
