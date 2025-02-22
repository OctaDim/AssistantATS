import torch
from gensim.models import FastText
import numpy as np
from torch import cosine_similarity

# Загрузка предобученной модели Word2Vec
model = FastText.load_fasttext_format('path/to/fasttext.model')  # Укажите правильный путь

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

# Преобразуем массивы NumPy в тензоры PyTorch
query_vector_tensor = torch.tensor(query_vector, dtype=torch.float32)
answer_vectors_tensors = [torch.tensor(av, dtype=torch.float32) for av in answer_vectors]

# Вычисление косинусного сходства
similarities = [cosine_similarity(query_vector_tensor.unsqueeze(0), av.unsqueeze(0)).item() for av in answer_vectors_tensors]
best_match_index = np.argmax(similarities)
print("Наиболее подходящий ответ:", answers[best_match_index])
