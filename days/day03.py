from curses.ascii import isdigit

from lib import load_input


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    grid = []
    for line in data:
        grid.append([x for x in line])
    result = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if not isdigit(grid[x][y]) or isdigit(grid[x][y]) and y > 0 and isdigit(grid[x][y-1]):
                continue
            z = y
            while z < len(grid[x]) and isdigit(grid[x][z]):
                z += 1
            if check_if_symbol_around(grid, x, y - 1, min(z + 1, len(grid[x]))):
                result += int("".join(grid[x][y:z]))
    return result


def check_if_symbol_around(grid, x, y_1, y_2):
    for y in range(y_1, y_2):
        if x > 0:
            if not isdigit(grid[x-1][y]) and grid[x-1][y] != '.':
                return True
        if x < len(grid) - 1:
            if not isdigit(grid[x+1][y]) and grid[x+1][y] != ".":
                return True
    if y_1 >= 0 and not grid[x][y_1] == '.':
        return True
    return grid[x][y_2 - 1] != '.' and not isdigit(grid[x][y_2 - 1])



def part_two(data):
    grid = []
    for line in data:
        grid.append([x for x in line])
    result = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == "*":
                # print(gear(grid, x, y))
                result += gear(grid, x, y)
    return result

def gear(grid, x_1, y_1):
    number_1 = 0
    number_2 = 0
    added = set()
    for x in range(max(0, x_1-1), min(x_1 + 2,len(grid))):
        for y in range(max(0, y_1-1), min(y_1 + 2, len(grid[x]))):
            if (x,y) in added:
                continue
            if isdigit(grid[x][y]):
                y_min = y_max = y
                while y_min >= 0 and isdigit(grid[x][y_min - 1]):
                    y_min -= 1
                while y_max < len(grid[x]) and isdigit(grid[x][y_max]):
                    y_max += 1
                for z in range(y_min, y_max):
                    added.add((x, z))
                if number_1 == 0:
                    number_1 = int("".join(grid[x][y_min: y_max]))
                else:
                    number_2 = int("".join(grid[x][y_min: y_max]))
    print(number_1, number_2)
    return number_1 * number_2

if __name__ == "__main__":
    # print(solve(load_input("small")))
    # print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
