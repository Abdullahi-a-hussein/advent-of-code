from functools import cache
path = "day11/input.txt"


def process_input(path):
    with open(path) as file:
        content = file.readlines()[0].strip("\n")
    return [entry.strip(" ") for entry in content.split(" ")]


stones = tuple(process_input(path))
seconds = 75


# def transform(stones, seconds):
#     for _ in range(seconds):
#         new_stones = []
#         for stone in stones:
#             if stone == "0":
#                 new_stones.append("1")
#             elif len(stone) % 2 == 0:
#                 ln = len(stone)
#                 left, right = stone[: ln//2], str(int(stone[ln//2:]))
#                 new_stones.append(left)

#                 new_stones.append(right)
#             else:
#                 sn = str(int(stone) * 2024)
#                 new_stones.append(sn)
#         stones = new_stones[:]
#     return len(stones)


def split(stone):
    new_stones = []
    if stone == "0":
        new_stones.append("1")
    elif len(stone) % 2 == 0:
        ln = len(stone)
        left, right = stone[: ln//2], str(int(stone[ln//2:]))
        new_stones.append(left)
        new_stones.append(right)
    else:
        sn = str(int(stone) * 2024)
        new_stones.append(sn)
    return tuple(new_stones)


@cache
def transform2(stones, seconds):
    if seconds == 0:
        return len(stones)
    total = 0
    for stone in stones:

        new_stones = split(stone)
        total += transform2(new_stones, seconds-1)
    return total


print(transform2(stones, seconds))
