from collections import defaultdict
# Day 1: Historian Hyseria

# Part
ex1 = [1, 2, 3, 3, 3, 4]
ex2 = [3, 3, 3, 4, 5, 9]


def sum_difference(lst1, lst2):
    return sum([abs(int(id1) - int(id2)) for id1, id2 in zip(lst1, lst2)])


def problem_input(path):
    with open(path) as file:
        content = file.readlines()
    items = []
    for entry in content:
        items.append(entry.strip("\n").split("   "))
    input1, input2 = [], []
    for item in items:
        input1.append(int(item[0]))
        input2.append(int(item[1]))
    input1.sort()
    input2.sort()
    return input1, input2


# part 1
lists = problem_input("input1.txt")
print(sum_difference(lists[0], lists[1])),

# part 2


def similarity_score(lst1, lst2):
    count = defaultdict(lambda: 0)
    for item1 in lst1:
        count[item1] = 0
        for item2 in lst2:
            if item1 == item2:
                count[item1] += 1

    score = sum([key * value for key, value in count.items()])
    return score


print(similarity_score(lists[0], lists[1]))
