from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from ML_answers.ML_answers_united import united_answers
from ML_questions.ML_questions_united import united_questions


answers = united_answers  # Список ответов
vectorizer = TfidfVectorizer()
answer_vectors = vectorizer.fit_transform(answers)  # Векторизация ответов

for question in united_questions:
    query_vector = vectorizer.transform([question])  # Векторизация вопроса

    # Вычисление косинусного сходства
    similarities = cosine_similarity(query_vector, answer_vectors)
    best_match_index = similarities.argmax()

    print(f'\nВопрос: "{question}"\n'
          f'\tНаиболее подходящий ответ: "{answers[best_match_index]}"\n')
