from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resumes(resumes, job_desc):
    all_texts = resumes + [job_desc]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(all_texts)
    
    similarity_scores = cosine_similarity(vectors[:-1], vectors[-1])
    ranked = sorted(enumerate(similarity_scores), key=lambda x: x[1], reverse=True)
    return ranked