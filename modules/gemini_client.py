from urllib import response
import google.generativeai as genai
from dotenv import load_dotenv
import os
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
1. Resume Summary
2. Internship Readiness Score (0-100)
3. Matching Skills
4. Missing Skills
5. Skill Gaps
6. Personalized 10-Day Learning Roadmap
7. Interview Preparation Topics
8. Mentor-Specific Preparation Advice
9. Questions To Ask The Mentor
10. Technologies The Mentor Likely Values
11. Final Internship Readiness Assessment
12. Top 10 Likely Interview Questions
13. Technical Questions Based On Candidate Resume
14. Technical Questions Based On Job Description
15. Behavioral Questions
16. Topics To Revise Before Interview
17. Mock Interview Tips
18. Recommended Learning Resources
19. Best Courses For Missing Skills
20. Project Suggestions To Improve Readiness

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

=== SCORE ===

=== RESUME SUMMARY ===

=== MATCHING SKILLS ===

=== MISSING SKILLS ===

=== SKILL GAPS ===

=== LEARNING ROADMAP ===

=== INTERVIEW PREPARATION ===

=== MENTOR ADVICE ===

=== QUESTIONS FOR MENTOR ===

=== TECHNOLOGIES MENTOR VALUES ===

=== FINAL ASSESSMENT ===

=== INTERVIEW QUESTIONS ===

=== TECHNICAL QUESTIONS RESUME ===

=== TECHNICAL QUESTIONS JD ===

=== BEHAVIORAL QUESTIONS ===

=== TOPICS TO REVISE ===

=== MOCK INTERVIEW TIPS ===

=== LEARNING RESOURCES ===

=== COURSES ===

=== PROJECT SUGGESTIONS ===

Return your response EXACTLY in this format:

=== MATCHING SKILLS ===
skill1
skill2
skill3

=== MISSING SKILLS ===
skill1
skill2
skill3

=== LEARNING ROADMAP ===
roadmap content

=== INTERVIEW QUESTIONS ===
questions

=== LEARNING RESOURCES ===
resources

=== PROJECT SUGGESTIONS ===
projects

=== FULL ANALYSIS ===
full analysis

Resume:

{resume_text}

Job Description:

{job_description}

Mentor Profile:

{mentor_profile}
"""
    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print("GEMINI ERROR:", str(e))
        raise e