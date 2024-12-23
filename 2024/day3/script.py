import re
# Day 3: Mull It Over


def solver(mul_str: str) -> int:
    return int(mul_str.split(",")[0]) * int(mul_str.split(",")[1])


def process_input(path):
    with open(path) as file:
        content = file.read()
    return content


def problem_1(problem_str, solver):
    content = problem_str
    i = 0
    ln = len(content) - 4
    required = []
    while i < ln:
        collected = ""
        j = i
        if content[i] == "m" and content[i:i+4] == "mul(":
            j = i + 4
            while content[j] != ")" and (content[j] == "," or content[j].isnumeric()):
                collected += content[j]
                j += 1
            if content[j] == ")":
                required.append(collected)
            i = j
        i += 1
    print(required)
    total = sum([solver(entry) for entry in required])
    return total


problem_str = process_input("input.txt")
p = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
# print(problem_1(problem_str, solver))

p = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def part_2(problem_str, solver):
    mul_pattern = r"mul\(\d+,\d+\)"
    dont_pattern = r"don't\(\)"
    do_pattern = r"do\(\)"

    # tokenize the input problem t find the position of each multiplication operation
    tokens = [(m.group(), m.start()) for m in re.finditer(
        rf"{mul_pattern}|{dont_pattern}|{do_pattern}", problem_str)]
    result, skip = [], False
    for i, (token, pos) in enumerate(tokens):
        if token == "don't()":
            skip = True
        elif token == "do()":
            skip = False
        elif re.match(mul_pattern, token):
            if not skip:
                pattern = r"\(([\d,]+)\)"
                matches = re.search(pattern, token).group(1)
                result.append(matches)
    total = sum([solver(op) for op in result])
    return total


print(part_2(problem_str, solver))
