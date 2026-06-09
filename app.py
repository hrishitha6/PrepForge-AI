import streamlit as st
import re 
from modules.pdf_reader import extract_text_from_pdf
from modules.gemini_client import analyze_resume
st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

.stMetric {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 12px;
}

div[data-testid="stExpander"] {
    border-radius: 12px;
    border: 1px solid #2d3748;
}

.hero-card {
    background: linear-gradient(90deg, #0f172a, #1e293b);
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #334155;
    margin-bottom: 20px;
}

.section-card {
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
    border: 1px solid #334155;
}

</style>
""", unsafe_allow_html=True)
def get_section(text, section_name):
    pattern = rf"=== {section_name} ===(.*?)(?===|\Z)"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return "No data found"
st.set_page_config(page_title="PrepForge AI", page_icon="🚀", layout="wide")
st.title("🚀 PrepForge AI")
st.subheader("AI-Powered Internship Readiness Platform")

st.markdown("""
### Get Internship Ready Faster
Upload your resume, add a job description, and mentor profile to receive personalized readiness insights.
""")

st.markdown("---")

upload_col, input_col = st.columns([1, 2])

with upload_col:
    uploaded_file = st.file_uploader(
        "📄 Upload Resume PDF",
        type=["pdf"]
    )

with input_col:
    job_description = st.text_area(
        "🧾 Job Description",
        height=180
    )

    mentor_profile = st.text_area(
        "👨‍🏫 Mentor Profile",
        height=180
    )

st.markdown("---")
if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    st.subheader("Resume Analysis")
    try:
        analysis = analyze_resume(
            text,
            job_description,
            mentor_profile
        )

    except Exception:

        st.warning(
        "⚠️ Gemini unavailable. Showing demo analysis."
    )

    analysis = """
=== MATCHING SKILLS ===
Python
Machine Learning
Git
Problem Solving

=== MISSING SKILLS ===
Docker
AWS
FastAPI

=== LEARNING ROADMAP ===
Day 1-3: Learn FastAPI
Day 4-6: Learn Docker
Day 7-10: Build Mini Project

=== LEARNING RESOURCES ===
FastAPI Docs
Docker Docs
AWS Skill Builder

=== INTERVIEW QUESTIONS ===
What is REST API?
What is Docker?
Explain Python OOP concepts.

=== PROJECT SUGGESTIONS ===
AI Resume Analyzer
Interview Preparation Assistant

87/100
"""
    st.stop()
    score_match=re.search(r'(\d{1,3})/100', analysis)
    if score_match:
        score = int(score_match.group(1))
        col1, col2, col3 = st.columns([1, 2, 1])

        with col1:
            st.metric(
                label="🎯 Score",
                value=f"{score}/100"
            )

        with col2:
            st.progress(score)
            
            if score >= 85:
                st.success("🟢 Strong Candidate")
            elif score >= 70:
                st.warning("🟡 Moderate Match")
            else:
                st.error("🔴 Needs Improvement")
        
        with col3:
            st.metric(
                label="📌 Status",
                value="Ready"
            )

        stat1, stat2, stat3, stat4 = st.columns(4)

        with stat1:
            st.metric("✅ Matching", "Analyzed")

        with stat2:
            st.metric("❌ Gaps", "Detected")

        with stat3:
            st.metric("📅 Roadmap", "10 Days")

        with stat4:
            if score >= 85:
                mentor_match = "90%"
            elif score >= 70:
                mentor_match = "75%"
            else:
                mentor_match = "60%"

            st.metric(
                "⭐ Mentor Match",
                mentor_match
            )

        risk_col = st.container()

    with risk_col:
        if score >= 85:
            st.success("🟢 Low Internship Risk")
        elif score >= 70:
            st.warning("🟡 Medium Internship Risk")
        else:
            st.error("🔴 High Internship Risk")
                
        st.subheader("📋 Quick Overview")
        st.markdown("---")

        st.markdown("""
<div class='hero-card'>
<h2>🚀 PrepForge AI Dashboard</h2>
<p><b>Resume + Job Description + Mentor Profile</b></p>
<p>AI-Powered Internship Readiness Analysis</p>
</div>
""", unsafe_allow_html=True)
        
        left_col, right_col = st.columns(2)

        with left_col:
            with st.expander("✅ Matching Skills"):
                matching_skills = get_section(
                analysis,
                "MATCHING SKILLS"
            )
                st.success(matching_skills)

            with st.expander("📅 Learning Roadmap"):
                learning_roadmap = get_section(
                    analysis,
                    "LEARNING ROADMAP"
                )
                st.write(learning_roadmap)

            with st.expander("📚 Learning Resources"):
                learning_resources = get_section(
                    analysis,
                    "LEARNING RESOURCES"
                )
                st.info(learning_resources)

        with right_col:
            with st.expander("❌ Missing Skills"):
                missing_skills = get_section(
                analysis,
                "MISSING SKILLS"
            )
                st.error(missing_skills)

            with st.expander("🎤 Interview Questions"):
                interview_questions = get_section(
                analysis,
                "INTERVIEW QUESTIONS"
            )
                st.write(interview_questions)
                
            with st.expander("💡 Project Suggestions"):
                project_suggestions = get_section(
                    analysis,
                    "PROJECT SUGGESTIONS"
                )
                st.write(project_suggestions)

        with st.expander("📊 View Full Analysis"):
            st.write(analysis)
        
        st.download_button(
    "📄 Download Analysis",
    analysis,
    file_name="prepforge_report.txt"
)