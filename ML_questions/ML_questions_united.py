import random

from ML_questions.ML_questions_crazy_auto_generated import (
    auto_generated_crazy_questions)
from ML_questions.ML_questions_custom_pre_defined import (
    pre_defined_questions)
from ML_questions.ML_questions_passport_14_years import (
    all_questions_passport_14_years)
from ML_questions.ML_questions_passport_20_years import (
    all_questions_passport_20_years)
from ML_questions.ML_questions_passport_45_years import (
    all_questions_passport_45_years)


random_united_questions = []
random_united_questions.extend(all_questions_passport_14_years)
random_united_questions.extend(all_questions_passport_20_years)
random_united_questions.extend(all_questions_passport_45_years)
random.shuffle(random_united_questions)
# print(random_united_questions)


random_united_questions = pre_defined_questions + random_united_questions
# print(random_united_questions)

random_united_questions.extend(auto_generated_crazy_questions)
# print(random_united_questions)

# unique_united_questions = list(set(random_united_questions))
unique_united_questions = []
for question in random_united_questions:
    if question not in unique_united_questions:
        unique_united_questions.append(question)

# print(unique_united_questions)
