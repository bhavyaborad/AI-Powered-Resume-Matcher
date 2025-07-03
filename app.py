import streamlit as st
from model import match_resumes

st.title("AI-Powered Resume Matcher")

st.write("Upload resumes and a job description to find the best match.")

uploaded_resumes = st.file_uploader("Upload Resumes (.txt)", type="txt", accept_multiple_files=True)
job_description = st.text_area("Paste Job Description")

if st.button("Match"):
    if uploaded_resumes and job_description:
        resume_texts = [res.read().decode("utf-8") for res in uploaded_resumes]
        results = match_resumes(resume_texts, job_description)
        for idx, score in results:
            st.write(f"Resume {idx+1} Match Score: {score:.2f}")
    else:
        st.warning("Please upload resumes and paste a job description.")