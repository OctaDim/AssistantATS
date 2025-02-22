import re


QUESTIONS_PASSPORT_CHANGE_DATA = [
    ("(|утерял|уворовали|исчез|потерянный|утерянный) паспорт (как|как можно|как мне)? ?(сделать новый|получить новый)?","0.0"),
    ("(как|как можно)? ?(заменить|переделать)? ?(плохой|испорченный|хуевый|порванный|намоченный) паспорт", "0.0"),
    ("(плохой|испорченный|хуевый|порванный|намоченный) паспорт (как|как можно)? ?(заменить|переделать)? ", "0.0"),
]


test_phrases = [
    # " паспорт  сделать новый",
    "намоченный паспорт как",
]

for q in QUESTIONS_PASSPORT_CHANGE_DATA:
    for test_phrase in test_phrases:
        if re.search(q[0], test_phrase, flags=re.U):
            print(q, test_phrase, " <= SUCCESSFULLY")
            continue
    print(q, " <= FAULT")
