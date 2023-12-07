import math
from pathlib import Path

input_file = Path(__file__).resolve().parent / "input.txt"


def create_matrix(data: list[str]):
    rows = len(data)
    cols = len(data[0])
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for ridx, line in enumerate(data):
        for cidx, char in enumerate(line):
            matrix[ridx][cidx] = char
    return matrix


def find_largest_number(matrix, row, col, tracked):
    chars = ""
    while col > 0 and matrix[row][col-1].isdigit():
        col -= 1
    while col < len(matrix[0]) and matrix[row][col].isdigit():
        chars += matrix[row][col]
        tracked.add((row, col))
        col += 1
    return int(chars) if chars else chars


def part_1(data: list[str]):
    matrix = create_matrix(data)
    numbers = []
    tracked = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col].isdigit() or matrix[row][col] == '.':
                continue
            inputs = [(row, col + 1), (row, col -1), (row -1, col), (row-1,col-1),(row-1,col+1), (row + 1, col - 1), (row + 1, col + 1)]
            for inp in inputs:
                if matrix[inp[0]][inp[1]].isdigit() and (inp[0], inp[1]) not in tracked:
                    num = find_largest_number(matrix, inp[0], inp[1], tracked)
                    if num:
                        numbers.append(num)
    return sum(numbers)


def part_2(data: list[str]):
    matrix = create_matrix(data)
    gear_ratios = []
    tracked = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] != '*':
                continue
            adj_nums = []
            inputs = [(row, col + 1), (row, col -1), (row -1, col), (row-1,col-1),(row-1,col+1), (row + 1, col - 1), (row + 1, col + 1)]
            for inp in inputs:
                if matrix[inp[0]][inp[1]].isdigit() and (inp[0], inp[1]) not in tracked:
                    num = find_largest_number(matrix, inp[0], inp[1], tracked)
                    if num:
                        adj_nums.append(num)
            if len(adj_nums) > 1:
                gear_ratios.append(math.prod(adj_nums))
    return sum(gear_ratios)


if __name__ == "__main__":
    data = input_file.read_text().splitlines()
    result = part_1(data)
    print(f"Part1: {result}")

    result = part_2(data)
    print(f"Part2: {result}")

