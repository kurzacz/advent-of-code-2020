import re
from pathlib import Path

regex = re.compile(r"(\d+)\-(\d+) (\w)\: (\w+)")

file_path = Path("input.txt")

def check_password_match_rules(char: str, first: int, second: int, password: str) -> bool:
    first_match = password[first-1] == char
    second_match = password[second-1] == char
    return first_match ^ second_match


passwords_valid = 0

with open(file_path, "r") as input_file:
    for line in input_file:
        decompose = regex.match(line)
        if not decompose:
            continue

        first_occurence = int(decompose.group(1))
        second_occurence = int(decompose.group(2))
        char = decompose.group(3)
        password = decompose.group(4)

        if check_password_match_rules(char, first_occurence, second_occurence, password):
            passwords_valid += 1

print(passwords_valid)

