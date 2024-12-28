from pprint import pprint
path = "day9/input.txt"


def process_input(path):
    with open(path) as file:
        content = file.read().strip("\n")
    disk_map = []
    block_id = 0
    for i in range(len(content)):
        is_file = i % 2 == 0
        x = int(content[i])
        if is_file:
            disk_map += [block_id] * x
            block_id += 1
        else:
            disk_map += [-1] * x

    return disk_map


disk_map = process_input(path)


# Part 1

def check_sum(disk_map):

    new_disk = disk_map[:]
    i, j = 0, len(disk_map) - 1
    while i < j:
        if disk_map[i] != -1:
            i += 1
        if disk_map[j] == -1:
            j -= 1
        if disk_map[i] == -1 and disk_map[j] != -1 and i < len(disk_map) - 1 and j >= 0:
            new_disk[i], new_disk[j] = new_disk[j], new_disk[i]
            i += 1
            j -= 1
    total = 0
    for i, item in enumerate(new_disk):
        if item != -1:
            total += i * item
        else:
            break
    return total


# print(disk_map)
print(check_sum(disk_map))


# Part 2

def check_sum_2(disk_map):
    answer = 0
    marker = []
    new_disk = disk_map[:]
    ln = len(disk_map)
    i = 0
    curr = disk_map[0]
    while i < ln:
        j = i
        while j < ln and disk_map[i] == disk_map[j]:
            curr = disk_map[j]
            j += 1

        marker.append([curr, [i, j - i]])
        i = j
    end = len(marker) - 1
    moved = False
    while end > 0:
        start = 0
        changes = []
        moved = False
        while start < end:
            if marker[end][0] == -1:
                break
            else:
                if marker[start][0] == -1:
                    l2 = marker[end][1][1]
                    s1, l1 = marker[start][1][0], marker[start][1][1]
                    if l2 < l1:
                        part = [-1, [s1 + l2, l1 - l2]]
                        # Collect changes instead of modifying in-place
                        changes.append((start, end, part))
                        moved = True
                        break
                    elif l2 == l1:
                        # Collect swap as a change
                        changes.append((start, end, None))
                        moved = True
                        break
                start += 1
        for change in changes:
            s, e, part = change

            s1, s2 = marker[s][1][0], marker[e][1][0]
            marker[s], marker[e] = marker[e], marker[s]
            marker[s][1][0] = s1
            marker[e][1][0] = s2
            if part:
                marker.insert(s + 1, part)
                marker[e+1][1][1] = marker[e + 1][1][1] - part[1][1]

        if moved:
            end = len(marker) - 1
        else:

            end -= 1
    for item in marker:
        if item[0] != -1:
            for i in range(item[1][0], item[1][0] + item[1][1]):
                answer += item[0] * i
    return answer


print(check_sum_2(disk_map))
