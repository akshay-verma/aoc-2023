from pathlib import Path
from typing import List


def _get_digits(line):
    nums = [char for char in line if char.isdigit()]
    return int("".join([nums[0], nums[-1]]))


def part_1(data: List[str]):
    result = 0
    for line in data:
        result += _get_digits(line)
    return result


digit_map = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3ree",
    "four": "f4ur",
    "five": "f5ve",
    "six": "s6x",
    "seven": "s7ven",
    "eight": "e8ght",
    "nine": "n9ne"
}

def part_2(data: List[str]) -> int:
    result = 0
    for line in data:
        for key, value in digit_map.items():
            line = line.replace(key, value)
        result += _get_digits(line)
    return result


if __name__ == "__main__": 
    data = (Path(__file__).resolve().parent / "input.txt").read_text()
    result = part_1(data.splitlines())
    print(f"Part1: {result}")

    result = part_2(data.splitlines())
    print(f"Part2: {result}")

