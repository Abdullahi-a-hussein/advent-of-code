

# --- Day 7: Bridge Repair ---
from itertools import product
# processing input to a workable format
provided_operation = ["*", "+"]


def process_input(path):
    with open(path) as file:
        content = [entry.strip("\n") for entry in file.readlines()]
    cal_equetions = []
    for entry in content:
        result = entry.split(":")
        test_value = int(result[0].strip())
        operation = [int(val.strip()) for val in result[1].strip().split(" ")]
        cal_equetions.append((test_value, operation))
    return cal_equetions


# Proceed input file
calibration_equations = process_input("input.txt")


# Part 1


# find and return all possible operation combinations
def perform_operation(operations, size):
    return list(product(operations, repeat=size))


def check_operation(test_value, expression):
    operations = perform_operation(provided_operation, len(expression) - 1)
    valid_operations = []
    for operation in operations:
        total = expression[0]
        for index, val in enumerate(operation):
            total = eval(f"{total}{val}{expression[index + 1]}")

        if total == test_value:
            valid_operations.append(operation)
    return len(valid_operations) > 0, valid_operations


def total_calibration(calibration_equations):
    total = 0
    for equation in calibration_equations:
        test_value, expression = equation
        correct, operation = check_operation(test_value, expression)
        if correct:
            total += test_value
    return total


print(total_calibration(calibration_equations))
