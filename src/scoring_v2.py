import json
from datetime import datetime
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from docx import Document

model = SentenceTransformer("all-MiniLM-L6-v2")

RELEVANT_SKILLS = [
    "Python",
    "NLP",
    "Embeddings",
    "Retrieval",
    "Ranking",
    "LLMs",
    "Fine-tuning LLMs",
    "Sentence Transformers",
    "OpenAI Embeddings",
    "BGE",
    "E5",
    "Pinecone",
    "Weaviate",
    "Qdrant",
    "Milvus",
    "OpenSearch",
    "Elasticsearch",
    "FAISS",
    "NDCG",
    "MRR",
    "MAP",
    "LoRA",
    "QLoRA",
    "PEFT",
    "Learning-to-Rank",
    "XGBoost"
]

class CandidateScorer:

    def __init__(self):

        doc = Document("data/job_description.docx")

        jd_text = ""

        for paragraph in doc.paragraphs:
            jd_text += paragraph.text + " "

        self.jd_embedding = model.encode([jd_text])

    def experience_score(self, candidate):
        years = round(candidate["profile"]["years_of_experience"])
        return min(max(years, 0), 9)

    def title_bonus(self, candidate):
        relevant_titles = ['AI Engineer',
'Machine Learning Engineer',
'ML Engineer',
'LLM Engineer',
'NLP Engineer',
'Applied Scientist',
'AI Research Engineer',
'Data Engineer']
        if candidate["profile"]["current_title"] in relevant_titles :
            return 1
        else:
            return 0

    def education_bonus(self, candidate):
        relevant_education = [
        "Computer Science",
        "Computer Engineering",
        "Information Technology",
        "Software Engineering",
        "Artificial Intelligence",
        "Machine Learning"
    ]

        for education in candidate["education"]:
            if education["field_of_study"] in relevant_education:
                return 1

        return 0
        

    def skill_score(self, candidate):

        score = 0

        for skill in candidate["skills"]:

            if skill["name"] in RELEVANT_SKILLS:

                if skill["proficiency"] == "beginner":
                    score += 0.1

                elif skill["proficiency"] == "intermediate":
                    score += 0.2

                elif skill["proficiency"] == "advanced":
                    score += 0.3

        return round(score, 2)

    def assessment_score(self, candidate): 
        score = 0

        assessments = candidate["redrob_signals"]["skill_assessment_scores"]

        for skill, marks in assessments.items():
            if skill in RELEVANT_SKILLS:
                score += marks / 100

        return round(score, 2)
    
    def last_active_score(self, candidate):

        last_active = datetime.strptime(
            candidate["redrob_signals"]["last_active_date"], "%Y-%m-%d"
            )

        today = datetime(2026, 6, 27)   # Dataset reference date
        days = (today - last_active).days

        if days <= 30:
            return 4
        elif days <= 60:
            return 3
        elif days <= 90:
            return 2
        elif days <= 120:
            return 1
        return 0


    def open_to_work_score(self, candidate):
        return 5 if candidate["redrob_signals"]["open_to_work_flag"] else 0


    def notice_period_score(self, candidate):
        notice = candidate["redrob_signals"]["notice_period_days"]

        if notice <= 30:
            return 4
        elif notice <= 60:
            return 2
        elif notice <= 90:
            return 1
        return 0


    def response_rate_score(self, candidate):
        rate = candidate["redrob_signals"]["recruiter_response_rate"] * 100

        if rate <= 20:
            return 1
        elif rate <= 40:
            return 2
        elif rate <= 60:
            return 3
        elif rate <= 80:
            return 4
        return 5


    def profile_completeness_score(self, candidate):
        score = candidate["redrob_signals"]["profile_completeness_score"]

        if score <= 25:
            return 1
        elif score <= 50:
            return 2
        elif score <= 75:
            return 3
        return 4


    def interview_completion_score(self, candidate):
        rate = candidate["redrob_signals"]["interview_completion_rate"] * 100

        if rate <= 30:
            return 1
        elif rate <= 70:
            return 2
        return 3


    def relocation_score(self, candidate):
        return 2 if candidate["redrob_signals"]["willing_to_relocate"] else 0


    def recruiter_signal_score(self, candidate):
        return (
            self.last_active_score(candidate)
            + self.open_to_work_score(candidate)
            + self.notice_period_score(candidate)
            + self.response_rate_score(candidate)
            + self.profile_completeness_score(candidate)
            + self.interview_completion_score(candidate)
            + self.relocation_score(candidate)
        )

    
    def career_history_score(self, candidate):

        career_text = ""

        for job in candidate["career_history"]:
            career_text += (
            job["title"] + " "
            + job["description"] + " "
        )
        
        career_embedding = model.encode([career_text])

        similarity = cosine_similarity(
        career_embedding,
        self.jd_embedding
        )[0][0]
        score = min(similarity * 45, 30)
        return round(score, 2)

    def final_score(self, candidate):

        return round(
        self.experience_score(candidate)
        + self.title_bonus(candidate)
        + self.education_bonus(candidate)
        + self.skill_score(candidate)
        + self.assessment_score(candidate)
        + self.career_history_score(candidate)
        + self.recruiter_signal_score(candidate),
        2
    )

# -------------------------------
# Testing starts here
# -------------------------------

if __name__ == "__main__":

    with open("data/sample_candidates.json", "r") as f:
        candidates = json.load(f)

    scorer = CandidateScorer()
    for candidate in candidates:
        candidate["final_score"] = scorer.final_score(candidate)

    candidates.sort(
    key=lambda x: x["final_score"],
    reverse=True
    )

    print("\nTop 10 Candidates:\n")

    for rank, candidate in enumerate(candidates[:10], start=1):
        print(rank, candidate["candidate_id"], candidate["final_score"])