from pathlib import Path

SUM_GOAL = 2020

numbers_list = list()
numbers_set = set()

file_path = Path("input.txt")
with open(file_path, "r") as input_file:
    for line in input_file:
        number = int(line.rstrip("\n"))
        numbers_list.append(number)
        numbers_set.add(number)

for number in numbers_list:
    complement = SUM_GOAL - number
    if complement in numbers_set:
        print(f"Found matching numbers: {number} & {complement}")
        print(f"Product equals to {number * complement}")
        break

