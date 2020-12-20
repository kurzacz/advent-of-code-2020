from pathlib import Path


class FoundAnswer(Exception):
    pass


SUM_GOAL = 2020


numbers_list = list()
numbers_set = set()

file_path = Path("input.txt")
with open(file_path, "r") as input_file:
    for line in input_file:
        number = int(line.rstrip("\n"))
        numbers_list.append(number)
        numbers_set.add(number)

try:
    for number1 in numbers_list:
        complement1 = SUM_GOAL - number1
        for number2 in numbers_list:
            complement2 = complement1 - number2

            if complement2 in numbers_set:
                print(f"Found matching numbers: {number1} & {number2} & {complement2}")
                print(f"Product equals to {number1 * number2 * complement2}")
                raise FoundAnswer
except FoundAnswer:
    pass
