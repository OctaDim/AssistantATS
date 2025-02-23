from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from ML_answers.ML_answers_united import unique_united_answers
from ML_questions.ML_questions_united import unique_united_questions


vectorizer = TfidfVectorizer()
answer_vectors = vectorizer.fit_transform(unique_united_answers)  # Векторизация ответов

for question in unique_united_questions:
    query_vector = vectorizer.transform([question])  # Векторизация вопроса
    # Вычисление косинусного сходства
    similarities = cosine_similarity(query_vector, answer_vectors)

    best_match_index = similarities.argmax()
    best_match_answer = unique_united_answers[best_match_index]

    # Нормализация сходства по длине ответа
    normalized_similarity = similarities.max()
    # normalized_similarity = similarities.max() / np.log(len(best_match_answer.split()))

    print(f'\nКосинусное сходство: {int(normalized_similarity * 100)} %\n'
          f'Вопрос: "{question}"\n'
          f'\tНаиболее подходящий ответ: "{best_match_answer}"\n')
