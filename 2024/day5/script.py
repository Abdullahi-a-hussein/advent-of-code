# --- Day 5: Print Queue ---

def process_input(path):
    with open(path) as file:
        content = file.read().split("\n\n")
    rules = [(int(page.strip("\n").split("|")[0]), int(
        page.strip("\n").split("|")[1])) for page in content[0].split("\n")]
    updates = [[int(page) for page in update.split(",")]
               for update in content[1].split("\n")]

    return rules, updates


rules, updates = process_input("input.txt")


def part_1(rules, updates, update_checker):
    total = 0
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


print(part_1(rules, updates, correct_update))

# part 2


def order(rules, update):
    new_update = [0] * len(update)
    cache = {}
    for i, page in enumerate(update):
        cache[page] = i
    for _ in update:
        for x, y in rules:
            if x in cache and y in cache and not cache[x] < cache[y]:
                cache[y], cache[x] = cache[x], cache[y]

    for page, i in cache.items():
        new_update[i] = page
    return new_update


def part_2(rules, updates, update_checker):
    total = 0
    for update in updates:
        check = update_checker(rules, update)
        if not check:
            new_update = order(rules, update)
            total += new_update[len(update) // 2]
    return total


rules, updates = process_input("input.txt")
print(part_2(rules, updates, correct_update))
