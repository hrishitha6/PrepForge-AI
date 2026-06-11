import google.generativeai as genai
from dotenv import load_dotenv
import os
import time
load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
print("API KEY FOUND:", bool(api_key))
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")
def analyze_resume(resume_text, job_description, mentor_profile):
    prompt=f"""
You are an internship readiness expert.
    
Analyze the candidate's resume against the job description.

Provide:
 Internship Readiness Score (out of 100)
1. Score
2. Matching Skills
3. Missing Skills
4. Learning Roadmap
5. Interview Questions
6. Learning Resources
7. Project Suggestions

Calculate an Internship Readiness Score out of 100.

Scoring Criteria:
- Resume Quality (25 points)
- Technical Skills Match (25 points)
- Project Strength (20 points)
- Job Description Alignment (15 points)
- Mentor Alignment (15 points)

Provide:
- Final Score
- Score Breakdown
- Reasoning for each category

For every missing skill, recommend:
- Free learning resources
- YouTube channels
- Courses
- Practice websites
- Mini project ideas

Make recommendations specific and actionable.

Return the response in EXACTLY this format:

=== LEARNING ROADMAP ===

=== INTERVIEW QUESTIONS ===

=== LEARNING RESOURCES ===

=== PROJECT SUGGESTIONS ===

Return your response EXACTLY in this format:

=== LEARNING ROADMAP ===
roadmap content

=== INTERVIEW QUESTIONS ===
questions

=== LEARNING RESOURCES ===
resources

=== PROJECT SUGGESTIONS ===
projects

Resume:

{resume_text}

Job Description:

{job_description}

Mentor Profile:

{mentor_profile}
"""
    try:
        start = time.time()
        print("Sending request to Gemini...")
        response = model.generate_content(prompt)
        print("Received response from Gemini")
        print("TIME TAKEN:", time.time() - start)
        return response.text
    except Exception as e:
        print("GEMINI ERROR:", str(e))
        raise e