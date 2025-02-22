from torch import cosine_similarity
from transformers import BertTokenizer, BertModel
import torch  # Импортируем torch для работы с тензорами
import numpy as np

from ML_answers.ML_answers_united import united_answers
from ML_questions.ML_questions_united import united_questions


# Загрузка предобученной модели и токенизатора
tokenizer = BertTokenizer.from_pretrained('cointegrated/rubert-tiny')
model = BertModel.from_pretrained('cointegrated/rubert-tiny')

# Функция для получения эмбеддинга текста
def text_to_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()

answers = united_answers  # Список ответов
answer_embeddings = [text_to_embedding(answer) for answer in answers]  # Векторизация ответов

for question in united_questions:
    query_embedding = text_to_embedding(question)  # Векторизация

    # Преобразуем массивы NumPy в тензоры PyTorch
    query_embedding_tensor = torch.tensor(query_embedding)
    answer_embeddings_tensors = [torch.tensor(ae) for ae in answer_embeddings]

    # Вычисление косинусного сходства
    similarities = [cosine_similarity(query_embedding_tensor, ae).item() for ae in answer_embeddings_tensors]
    best_match_index = np.argmax(similarities)

    print(f'\nВопрос: "{question}"\n'
          f'\tНаиболее подходящий ответ: "{answers[best_match_index]}"\n')
