# --- Day 5: Print Queue ---

def process_input(path):
    with open(path) as file:
        content = file.read().split("\n\n")
    rules = [(int(page.strip("\n").split("|")[0]), int(
        page.strip("\n").split("|")[1])) for page in content[0].split("\n")]
    updates = [[int(page) for page in update.split(",")]
               for update in content[1].split("\n")]

    return rules, updates


def part_1(content, update_checker):
    total = 0
    rules, updates = content

    for update in updates:
        check = update_checker(rules, update)
        if check:
            total += update[len(update) // 2]
    return total


def correct_update(rules, update) -> bool:
    cache = {}
    for i, page in enumerate(update):
        cache[page] = i
    for rule in rules:
        x, y = rule
        if x in cache and y in cache and not cache[x] < cache[y]:
            return False
    return True

    # print(process_input("input.txt"))
rules = [
    (47, 53),
    (97, 13),
    (97, 61),
    (97, 47),
    (75, 29),
    (61, 13),
    (75, 53),
    (29, 13),
    (97, 29),
    (53, 29),
    (61, 53),
    (97, 53),
    (61, 29),
    (47, 13),
    (75, 47),
    (97, 75),
    (47, 61),
    (75, 61),
    (47, 29),
    (75, 13),
    (53, 13)
]

updates = [[75, 47, 61, 53, 29],
           [97, 61, 53, 29, 13],
           [75, 29, 13],
           [75, 97, 47, 61, 53],
           [61, 13, 29],
           [97, 13, 75, 29, 47]
           ]

content = process_input("input.txt")
print(part_1(content, correct_update))
