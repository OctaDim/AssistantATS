import exrex

from re_expressions.regexp_passport import (
    QUESTIONS_PASSPORT_14_YEARS)


TEST_QUESTIONS = QUESTIONS_PASSPORT_14_YEARS


def generate_all_matches(regex):
    try:
        return list(exrex.generate(regex))
    except Exception as error:
        print(f"Regex expression error: {regex}")
        print(f"Exception error: {error}")
        return []


expressions_counter = 0
expressions_set = set()
for index, (regex, wav_number) in enumerate(TEST_QUESTIONS, 1):
    print(f"\n\n\t'Regular expression {index}: {regex}'")
    all_matches = generate_all_matches(regex)
    print(f"\tAll possible expressions: {len(all_matches)}")
    for match in all_matches:
        print(match)
        expressions_set.add(match)
        expressions_counter += 1

print(f"\n\t\tMatches: {expressions_counter}")
print(f"\t\tUnique Matches: {len(expressions_set)}")
print(f"\t\tNon-Unique Matches Deleted: {len(expressions_set) - expressions_counter}")
