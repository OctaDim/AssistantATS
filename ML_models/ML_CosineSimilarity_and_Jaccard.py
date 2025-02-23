from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import jaccard_score
from ML_answers.ML_answers_united import unique_united_answers
from ML_questions.ML_questions_united import unique_united_questions


vectorizer = TfidfVectorizer()
answer_vectors = vectorizer.fit_transform(unique_united_answers)  # Векторизация ответов

for random_question in unique_united_questions:
    query_vector = vectorizer.transform([random_question])
    similarities = cosine_similarity(query_vector, answer_vectors)
    best_match_index = similarities.argmax()
    best_match_answer = unique_united_answers[best_match_index]

    # Jaccard-сходство
    question_words = set(random_question.lower().split())
    answer_words = set(best_match_answer.lower().split())
    jaccard_sim = len(question_words.intersection(answer_words)) / len(question_words.union(answer_words))

    print(f'\nJaccard-сходство: {int(jaccard_sim * 100)} %\n'
          f'Вопрос: "{random_question}"\n'
          f'\tНаиболее подходящий ответ: "{best_match_answer}"\n')
