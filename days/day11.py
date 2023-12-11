import numpy as np

from lib import load_input


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    grid = []
    for x in data:
        grid.append([y for y in x])
    galaxies = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y]== "#":
                galaxies.append((x, y))
    empty_rows = [z[0] for z in list(filter(lambda x1: all(y == "." for y in x1[1]), enumerate(grid)))]
    grid_T = np.transpose(np.array(grid)).tolist()
    empty_columns = [z[0] for z in list(filter(lambda x1: all(y == "." for y in x1[1]), enumerate(grid_T)))]
    result = 0
    for x in galaxies:
        for y in galaxies:
            result += abs(x[0] - y[0]) + abs(x[1] - y[1])
            result += len(list(filter(lambda z: z in range(min(x[0], y[0]), max(x[0], y[0])), empty_rows)))
            result += len(list(filter(lambda z: z in range(min(x[1], y[1]), max(x[1], y[1])), empty_columns)))
    return int(result / 2)


def part_two(data):
    grid = []
    for x in data:
        grid.append([y for y in x])
    galaxies = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == "#":
                galaxies.append((x, y))
    empty_rows = [z[0] for z in list(filter(lambda x1: all(y == "." for y in x1[1]), enumerate(grid)))]
    grid_T = np.transpose(np.array(grid)).tolist()
    empty_columns = [z[0] for z in list(filter(lambda x1: all(y == "." for y in x1[1]), enumerate(grid_T)))]
    result = 0
    for x in galaxies:
        for y in galaxies:
            result += abs(x[0] - y[0]) + abs(x[1] - y[1])
            result += len(list(filter(lambda z: z in range(min(x[0], y[0]), max(x[0], y[0])), empty_rows))) * 999999
            result += len(list(filter(lambda z: z in range(min(x[1], y[1]), max(x[1], y[1])), empty_columns))) * 999999
    return int(result / 2)


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
