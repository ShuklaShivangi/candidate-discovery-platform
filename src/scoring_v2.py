import json

class CandidateScorer:

    def __init__(self, job_description):
        self.job_description = job_description

    def experience_score(self, candidate):
        years = round(candidate["profile"]["years_of_experience"])
        return min(max(years, 0), 9)

    def title_bonus(self, candidate):
        relevant_title = ['AI Engineer',
'Machine Learning Engineer',
'ML Engineer',
'LLM Engineer',
'NLP Engineer',
'Applied Scientist',
'AI Research Engineer',
'Data Engineer']
        if candidate["profile"]["current_title"] in relevant_title :
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
        pass

    def assessment_score(self, candidate):
        pass

    def career_history_score(self, candidate):
        pass

    def recruiter_signal_score(self, candidate):
        pass

    def final_score(self, candidate):
        pass

# -------------------------------
# Testing starts here
# -------------------------------

if __name__ == "__main__":

    with open("data/sample_candidates.json", "r") as f:
        candidates = json.load(f)

    candidate = candidates[0]
    scorer = CandidateScorer(None)
    print("Experience:", scorer.experience_score(candidate))
    print("Title:", scorer.title_bonus(candidate))
    print("Education:", scorer.education_bonus(candidate))