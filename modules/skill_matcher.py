import re
SKILLS_JD=["Python",
    "Java",
    "C++",
    "JavaScript",
    "HTML",
    "CSS",
    "React",
    "Node.js",
    "SQL",
    "MySQL",
    "MongoDB",
    "Git",
    "GitHub",
    "Docker",
    "AWS",
    "FastAPI",
    "Django",
    "Machine Learning",
    "Data Structures",
    "Algorithms",
    "Problem Solving"]
def extract_skills(text):
    found=[]
    for skill in SKILLS_JD:
        if re.search(rf"\b{re.escape(skill)}\b", text, re.IGNORECASE):
            found.append(skill)
    return list(set(found))
def compare_skills(resume_text,jd_text):
    resume_skills=extract_skills(resume_text)
    jd_skills=extract_skills(jd_text)
    matching =list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))
    return matching, missing
def calculate_score(matching, missing):
    total_skills = len(matching) + len(missing)
    if total_skills == 0:
        return 0
    score = int((len(matching) / total_skills) * 100)
    return score
def get_score_breakdown(matching, missing):
    total = len(matching) + len(missing)
    if total == 0:
        return 0, 0, 0
    skill_coverage = int((len(matching) / total) * 100)
    technical_match = skill_coverage
    resume_strength = min(
        100,
        60 + len(matching) * 5
    )
    return (
        technical_match,
        resume_strength,
        skill_coverage
    )