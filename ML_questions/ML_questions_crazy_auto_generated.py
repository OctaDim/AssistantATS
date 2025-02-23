import random
import re

from ML_questions.ML_questions_custom_pre_defined import pre_defined_questions
from ML_questions.ML_questions_passport_14_years import all_questions_passport_14_years
from ML_questions.ML_questions_passport_20_years import all_questions_passport_20_years
from ML_questions.ML_questions_passport_45_years import all_questions_passport_45_years


all_questions = []
all_questions.extend(all_questions_passport_14_years)
all_questions.extend(all_questions_passport_20_years)
all_questions.extend(all_questions_passport_45_years)
all_questions.extend(pre_defined_questions)

all_questions_global_str = ", ".join(all_questions)
all_questions_valid_global_str = re.sub(
    pattern=r"[^a-zA-Zа-яА-Я0-9 ]",
    repl="", string=all_questions_global_str)

# print(all_questions_valid_global_str)

all_questions_words_global_list = all_questions_valid_global_str.split(" ")
all_questions_words_unique_set = set(all_questions_words_global_list)
all_questions_words_unique_list = list(all_questions_words_unique_set)

for index in range(len(all_questions_words_unique_list)):
    lowered_word = all_questions_words_unique_list[index].lower()
    all_questions_words_unique_list[index] = lowered_word

# print(all_questions_words_unique_list)

auto_generated_crazy_questions = []
for _ in range(15):
    random_number = random.randint(1, 10)
    random_words = random.sample(all_questions_words_unique_list, random_number)
    random_words = " ".join(random_words)
    auto_generated_crazy_questions.append(random_words)

# print(auto_generated_crazy_questions)
