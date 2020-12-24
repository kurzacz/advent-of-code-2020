import re
from pathlib import Path

regex = re.compile(r"(\d+)\-(\d+) (\w)\: (\w+)")

file_path = Path("input.txt")

def check_password_match_rules(char: str, min_occurences: int, max_occurences: int, password: str) -> bool:
    num_occurences = password.count(char)
    return min_occurences <= num_occurences <= max_occurences


passwords_valid = 0

with open(file_path, "r") as input_file:
    for line in input_file:
        decompose = regex.match(line)
        if not decompose:
            continue

        min_occurences = int(decompose.group(1))
        max_occurences = int(decompose.group(2))
        char = decompose.group(3)
        password = decompose.group(4)

        if check_password_match_rules(char, min_occurences, max_occurences, password):
            passwords_valid += 1

print(passwords_valid)

