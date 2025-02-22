import random
import re

from ML_answers.ML_answers_united import united_answers


global_str = ", ".join(united_answers)
valid_global_str = re.sub(pattern=r"[^a-zA-Zа-яА-Я0-9 ]",
                          repl="", string=global_str)
print(valid_global_str)
global_list = valid_global_str.split(" ")
unique_words_set = set(global_list)
unique_words_list = list(unique_words_set)
unique_words_list = [word.lower() for word in unique_words_list]
print(unique_words_list)

random_questions = []
for _ in range(500):
    random_number = random.randint(3, 10)
    random_words = random.sample(unique_words_list, random_number)
    random_words = " ".join(random_words)
    random_questions.append(random_words)

print(random_questions)
