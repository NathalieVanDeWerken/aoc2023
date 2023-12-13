import numpy as np

from lib import load_input


def solve(data, part=1):
    lines = data.split("\n\n")
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)

def score(grid):
    for i in range(0, len(grid) - 1):
        flag = True
        for j in range(0, min(i + 1, len(grid) - 1 - i)):
            if grid[i - j] != grid[i + 1 + j]:
                flag = False
        if flag:
            return (i + 1) * 100
    grid_T = np.transpose(np.array(grid)).tolist()
    for i in range(0, len(grid_T) - 1):
        flag = True
        for j in range(0, min(i + 1, len(grid_T) - 1 - i)):
            if grid_T[i - j] != grid_T[i + 1 + j]:
                flag = False
        if flag:
            return i + 1
    return 0

def part_one(data):
    ans = 0
    for x in data:
        grid = []
        for y in x.splitlines():
            grid.append(list(y))
        ans += score(grid)
    return ans

def part_two(data):
    ans = 0
    for x in data:
        grid = []
        for y in x.splitlines():
            grid.append(list(y))
        ans += score2(grid)
    return ans


def score2(grid):
    for i in range(0, len(grid) - 1):
        diff = 0
        for j in range(0, min(i + 1, len(grid) - 1 - i)):
            diff += sum(1 for x, y in zip(grid[i - j], grid[i + 1 + j]) if x != y)
        if diff == 1:
            return (i + 1) * 100
    grid_T = np.transpose(np.array(grid)).tolist()
    for i in range(0, len(grid_T) - 1):
        diff = 0
        for j in range(0, min(i + 1, len(grid_T) - 1 - i)):
            diff += sum(1 for x, y in zip(grid_T[i - j], grid_T[i + 1 + j]) if x != y)
        if diff == 1:
            return i + 1
    return 0

if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
