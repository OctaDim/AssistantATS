import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from ML_answers.ML_answers_united import unique_united_answers
from ML_questions.ML_questions_united import unique_united_questions


vectorizer = TfidfVectorizer()
answer_vectors = vectorizer.fit_transform(unique_united_answers)  # Векторизация ответов

for random_question in unique_united_questions:
    query_vector = vectorizer.transform([random_question])
    similarities = cosine_similarity(query_vector, answer_vectors)

    # Минимаксная нормализация
    min_sim = np.min(similarities)
    max_sim = np.max(similarities)
    normalized_similarities = (similarities - min_sim) / (max_sim - min_sim)

    # Выбор элемента с максимальным значением
    best_match_index = normalized_similarities.argmax()
    best_match_answer = unique_united_answers[best_match_index]

    print(f'\nНормализованное косинусное сходство: {round(similarities.max() * 100)} %\n'
          f'Вопрос: "{random_question}"\n'
          f'\tНаиболее подходящий ответ: "{best_match_answer}"\n')
