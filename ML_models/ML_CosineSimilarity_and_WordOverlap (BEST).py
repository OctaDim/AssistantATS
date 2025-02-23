import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from ML_answers.ML_answers_united import unique_united_answers
from ML_questions.ML_questions_united import unique_united_questions


# Векторизация ответов
vectorizer = TfidfVectorizer()
answer_vectors = vectorizer.fit_transform(unique_united_answers)

for question in unique_united_questions:
    # Векторизация вопроса
    query_vector = vectorizer.transform([question])

    # Вычисление косинусного сходства
    similarities = cosine_similarity(query_vector, answer_vectors)

    if similarities.size > 0:
        # Подсчет коэффициента перекрытия слов для каждого ответа
        question_words = set(question.lower().split())
        word_overlap_ratios = []
        for answer in unique_united_answers:
            answer_words = set(answer.lower().split())
            common_words = question_words.intersection(answer_words)
            if len(question_words) > 0:
                # word_overlap_ratio = len(common_words) / len(question_words)
                word_overlap_ratio = len(common_words) / len(answer_words)
            else:
                word_overlap_ratio = 0
            word_overlap_ratios.append(word_overlap_ratio)

        # Взвешенная оценка: комбинация косинусного сходства и коэффициента перекрытия слов
        cosine_similarity_weight = 1 * similarities[0]
        word_overlap_weight = 1 * np.array(word_overlap_ratios)
        weighted_scores = (cosine_similarity_weight + word_overlap_weight) / 2

        # 40% GOOD RESULTS

        # Сортировка индексов по убыванию взвешенной оценки
        sorted_indices = np.argsort(-weighted_scores)  # Используем отрицательные значения для сортировки по убыванию

        # Наиболее подходящий ответ
        best_match_index = sorted_indices[0]
        best_match_answer = unique_united_answers[best_match_index]
        best_match_score = weighted_scores[best_match_index]

        # Менее подходящие ответы (следующие по сходству)
        less_match_answer_1 = unique_united_answers[sorted_indices[1]]
        less_match_score_1 = weighted_scores[sorted_indices[1]]

        less_match_answer_2 = unique_united_answers[sorted_indices[2]]
        less_match_score_2 = weighted_scores[sorted_indices[2]]

        less_match_answer_3 = unique_united_answers[sorted_indices[3]]
        less_match_score_3 = weighted_scores[sorted_indices[3]]

        less_match_answer_4 = unique_united_answers[sorted_indices[4]]
        less_match_score_4 = weighted_scores[sorted_indices[4]]

        # Вывод результатов
        print(f'\nВопрос: "{question}"')

        if round(best_match_score * 100) >= 40:
            print(f'\tПодходящие ответы найдены (OK)')
            print(f'\tНаиболее подходящий ответ (*****): "{best_match_answer}"'
                  f'\t({round(best_match_score * 100)} %)\n'
                  f'\tМенее подходящий ответ 1 (****): "{less_match_answer_1}"'
                  f'\t({round(less_match_score_1 * 100)} %)\n'
                  f'\tМенее подходящий ответ 2 (***): "{less_match_answer_2}"'
                  f'\t({round(less_match_score_2 * 100)} %)\n'
                  f'\tМенее подходящий ответ 3 (**): "{less_match_answer_3}"'
                  f'\t({round(less_match_score_3 * 100)} %)\n'
                  f'\tМенее подходящий ответ 4 (*): "{less_match_answer_4}"'
                  f'\t({round(less_match_score_4 * 100)} %)\n')
        else:
            print(f'\tПодходящего ответа не найдено (XX)')
            print(f'\tНеподходящий ответ 0 (xxxxx): "{best_match_answer}"'
                  f'\t({round(best_match_score * 100)} %)\n'
                  f'\tНеподходящий ответ 1 (xxxx): "{less_match_answer_1}"'
                  f'\t({round(less_match_score_1 * 100)} %)\n'
                  f'\tНеподходящий ответ 2 (xxx): "{less_match_answer_2}"'
                  f'\t({round(less_match_score_2 * 100)} %)\n'
                  f'\tНеподходящий ответ 3 (xx): "{less_match_answer_3}"'
                  f'\t({round(less_match_score_3 * 100)} %)\n'
                  f'\tНеподходящий ответ 4 (x): "{less_match_answer_4}"'
                  f'\t({round(less_match_score_4 * 100)} %)\n')
    else:
        print(f'\nОшибка: Не удалось вычислить сходство для вопроса: "{question}"')
