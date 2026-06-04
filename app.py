import streamlit as st
from modules.pdf_reader import extract_text_from_pdf
from modules.gemini_client import analyze_resume
st.set_page_config(page_title="PrepForge AI", page_icon="🚀", layout="wide")
st.title("🚀 PrepForge AI")
st.subheader("AI-Powered Internship Readiness Platform")
st.write("""Upload your Resume,
    Job Description,
    and Mentor Profile
    to get personalized insights.""")
uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"])
job_description = st.text_area("Job Description",height=250)
mentor_profile=st.text_area("Mentor Profile", height=250)
if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    st.subheader("Resume Analysis")
    analysis = analyze_resume(text, job_description, mentor_profile)
    st.write(analysis)