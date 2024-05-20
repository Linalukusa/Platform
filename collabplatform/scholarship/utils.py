import re
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from authentication.models import StudentProfile
from .models import Scholarship

# Define the threshold for similarity
threshold = 0.7  # Adjust based on your needs

def preprocess_text(text):
    # Tokenize text and remove non-alphanumeric characters
    return re.findall(r'\w+', text.lower())

def compute_similarity(text1, text2):
    vectorizer = TfidfVectorizer(tokenizer=preprocess_text)
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(tfidf_matrix)[0, 1]
    return similarity

def meets_eligibility_criteria(student: StudentProfile, scholarships: List[Scholarship]) -> List[Scholarship]:
    eligible_scholarships = []
    student_major_text = student.major.lower()
    student_education_level_text = student.education_level.lower()

    for scholarship in scholarships:
        scholarship_description_text = scholarship.description.lower()

        # Compute cosine similarity between scholarship description and student's major/education level
        major_similarity = compute_similarity(scholarship_description_text, student_major_text)
        education_level_similarity = compute_similarity(scholarship_description_text, student_education_level_text)

        # Check if average similarity is above the threshold
        if (major_similarity + education_level_similarity) / 2 > threshold:
            eligible_scholarships.append(scholarship)
            continue  # Skip to next scholarship as we have found a match

        # Token-based matching for major and education level
        scholarship_description_tokens = set(preprocess_text(scholarship.description))
        student_major_tokens = set(preprocess_text(student.major))
        student_education_level_tokens = set(preprocess_text(student.education_level))

        if scholarship_description_tokens.intersection(student_major_tokens) or scholarship_description_tokens.intersection(student_education_level_tokens):
            eligible_scholarships.append(scholarship)
            continue  # Skip to next scholarship as we have found a match

        # Check if the student's income matches
        income_ranges = {
            '0-10k': (0, 10000),
            '10k-30k': (10000, 30000),
            '30k-50k': (30000, 50000),
            '50k-75k': (50000, 75000),
            '75k-100k': (75000, 100000),
            '100k+': (100000, float('inf'))
        }

        income_range = income_ranges.get(student.annual_family_income)
        if income_range and income_range[0] <= scholarship.amount <= income_range[1]:
            eligible_scholarships.append(scholarship)
            continue  # Skip to next scholarship as we have found a match

        # Check if the student's education level matches
        if scholarship.applicable_education_level.lower() == student.education_level.lower():
            eligible_scholarships.append(scholarship)
            continue  # Skip to next scholarship as we have found a match

        # Check if the student's major matches
        if scholarship.major.lower() == student.major.lower():
            eligible_scholarships.append(scholarship)

    return eligible_scholarships

def gale_shapley_match_students_to_scholarships(students: List[StudentProfile], scholarships: List[Scholarship]) -> dict:
    student_preferences = {student: meets_eligibility_criteria(student, scholarships) for student in students}
    scholarship_preferences = {scholarship: [] for scholarship in scholarships}

    for student, eligible_scholarships in student_preferences.items():
        for scholarship in eligible_scholarships:
            scholarship_preferences[scholarship].append(student)

    student_matching = {}
    scholarship_matching = {}

    while student_preferences:
        student, student_choices = student_preferences.popitem()
        matched = False
        for scholarship in student_choices:
            if student in scholarship_preferences[scholarship]:
                student_matching.setdefault(student, []).append(scholarship)
                scholarship_matching.setdefault(scholarship, []).append(student)
                matched = True
        # If no match found for the student, add an empty list to maintain consistency
        if not matched:
            student_matching.setdefault(student, [])

    return student_matching
