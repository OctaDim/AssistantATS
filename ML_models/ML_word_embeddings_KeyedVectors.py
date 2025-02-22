from gensim.models import KeyedVectors
import numpy as np
from torch import cosine_similarity


# Загрузка предобученной модели Word2Vec
model = KeyedVectors.load_word2vec_format('path/to/word2vec.bin', binary=True)

# Функция для получения вектора текста
def text_to_vector(text):
    words = text.split()
    vectors = [model[word] for word in words if word in model]
    return np.mean(vectors, axis=0) if vectors else np.zeros(model.vector_size)

# Список ответов
answers = [
    "Как получить паспорт в 14 лет?",
    "Где оформить загранпаспорт?",
    "Какие документы нужны для замены паспорта?"
]

# Текстовый запрос
query = "Как сделать паспорт в 14 лет?"

# Векторизация текстов
query_vector = text_to_vector(query)
answer_vectors = [text_to_vector(answer) for answer in answers]

# Вычисление косинусного сходства
similarities = [cosine_similarity([query_vector], [av])[0][0] for av in answer_vectors]
best_match_index = np.argmax(similarities)
print("Наиболее подходящий ответ:", answers[best_match_index])
