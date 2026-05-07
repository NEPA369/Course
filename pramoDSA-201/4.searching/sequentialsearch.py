# 1. Write a program for sequential Search.

def find_first(data, target):
    for index in range(len(data)):
        if data[index] == target:
            return index
    return -1


def find_last(data, target):
    for index in range(len(data) - 1, -1, -1):
        if data[index] == target:
            return index
    return -1


def find_all(data, target):
    return [i for i, value in enumerate(data) if value == target]


if __name__ == "__main__":
    elements = [20, 33, 8, 45, 8, 19, 8, 25]

    print("Data:", elements)
    print("First 8 index:", find_first(elements, 8))
    print("Last 8 index:", find_last(elements, 8))
    print("All 8 indices:", find_all(elements, 8))
