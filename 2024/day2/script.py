
def savety_check(input_list) -> bool:
    increasing = True
    decreasing = True

    for index in range(len(input_list) - 1):
        diff = input_list[index] - input_list[index + 1]
        if abs(diff) == 0 or abs(diff) > 3:
            return False
        if diff > 0:
            decreasing = False
        if diff < 0:
            increasing = False
    return increasing or decreasing

# print(savety_check("7 6 4 2 1"))
# print(savety_check("1 2 7 8 9"))
# print(savety_check("9 7 6 2 1"))
# print(savety_check("1 3 2 4 5"))
# print(savety_check("8 6 4 4 1"))
# print(savety_check("1 3 6 7 9"))


def process_input(path, savety):
    with open(path) as file:
        content = file.readlines()
    count = 0
    for report in content:
        input_list = [int(item.strip())
                      for item in report.strip(" ").split(" ")]
        if savety(input_list):
            count += 1
    return count


def savety_check_2(input_list) -> bool:

    recheck = False
    check = savety_check(input_list)
    if check:
        return True
    if savety_check(input_list[1:]):
        return True
    ln = len(input_list)
    if savety_check(input_list[: ln-1]):
        return True
    for i in range(1, ln - 1):
        new_input = input_list[:i] + input_list[i+1:]
        if savety_check(new_input):
            return True
    return False


# print(savety_check_2("7 6 4 2 1"))
# print(savety_check_2("1 2 7 8 9"))
# print(savety_check_2("9 7 6 2 1"))
# print(savety_check_2("1 3 2 4 5"))
# print(savety_check_2("8 6 4 4 1"))
# print(savety_check_2("1 3 6 7 9"))


print(process_input("input.txt", savety_check_2))
