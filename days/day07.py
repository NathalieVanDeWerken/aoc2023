import functools
from collections import Counter

from lib import load_input


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def rank(item):
    scores = {
        (5,): 7,
        (1, 4): 6,
        (2, 3): 5,
        (1, 1, 3): 4,
        (1, 2, 2): 3,
        (1, 1, 1, 2): 2,
        (1, 1, 1, 1, 1): 1
    }
    x = Counter(item)
    return scores[tuple(sorted(x.values()))]


def compare(item1, item2):
    points = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12,
              'A': 13}
    rank_1 = rank(item1[0])
    rank_2 = rank(item2[0])
    if rank_1 > rank_2:
        return 1
    elif rank_1 < rank_2:
        return -1
    else:
        for x, y in zip(item1[0], item2[0]):
            if points[x] != points[y]:
                return -1 if points[x] < points[y] else 1


def part_one(data):
    data = [line.strip().split(" ") for line in data]
    data = sorted(data, key=functools.cmp_to_key(compare))
    result = 0
    for ind, x in enumerate(data):
        result += (ind + 1) * int(x[1])
    return result


def compare2(item1, item2):
    points = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 11, 'K': 12,
              'A': 13}
    rank_1 = rank2(item1[0])
    rank_2 = rank2(item2[0])
    if rank_1 > rank_2:
        return 1
    elif rank_1 < rank_2:
        return -1
    else:
        for x, y in zip(item1[0], item2[0]):
            if points[x] != points[y]:
                return -1 if points[x] < points[y] else 1


def rank2(item):
    scores = {
        (5,): 7,
        (1, 4): 6,
        (2, 3): 5,
        (1, 1, 3): 4,
        (1, 2, 2): 3,
        (1, 1, 1, 2): 2,
        (1, 1, 1, 1, 1): 1
    }
    x = Counter(item)
    to_add = x['J']
    del x['J']
    if len(x) == 0:
        return 7
    highest = max([(value, key) for key, value in x.items()])
    x.update({highest[1]: to_add})
    return scores[tuple(sorted(x.values()))]


def part_two(data):
    data = [line.strip().split(" ") for line in data]
    data = sorted(data, key=functools.cmp_to_key(compare2))
    result = 0
    for ind, x in enumerate(data):
        result += (ind + 1) * int(x[1])
    return result


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
