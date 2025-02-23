from torch import cosine_similarity
from transformers import BertTokenizer, BertModel
import torch  # Импортируем torch для работы с тензорами
import numpy as np

from ML_answers.ML_answers_united import unique_united_answers
from ML_questions.ML_questions_united import unique_united_questions


# Загрузка предобученной модели и токенизатора
tokenizer = BertTokenizer.from_pretrained('cointegrated/rubert-tiny')
model = BertModel.from_pretrained('cointegrated/rubert-tiny')


# Функция для получения эмбеддинга текста
def text_to_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()


answer_embeddings = [text_to_embedding(answer) for answer in unique_united_answers]  # Векторизация ответов

for random_question in unique_united_questions:
    query_embedding = text_to_embedding(random_question)  # Векторизация

    # Преобразуем массивы NumPy в тензоры PyTorch
    query_embedding_tensor = torch.tensor(query_embedding)
    answer_embeddings_tensors = [torch.tensor(ae) for ae in answer_embeddings]

    # Вычисление косинусного сходства
    similarities = [cosine_similarity(query_embedding_tensor, ae).item() for ae in answer_embeddings_tensors]
    best_match_index = np.argmax(similarities)
    best_match_answer = unique_united_answers[best_match_index]
    # print(similarities)

    print(f'\nКосинусное сходство: {round(max(similarities) * 100)} %\n'
          f'Вопрос: "{random_question}"\n'
          f'\tНаиболее подходящий ответ: "{best_match_answer}"\n')
