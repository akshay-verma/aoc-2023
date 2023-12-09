from pathlib import Path
from collections import defaultdict

input_file = Path(__file__).parent.resolve() / "input.txt"


def create_map(data):
    result = defaultdict(int)
    for num in data.split(" "):
        if num:
            num = num.strip()
            result[int(num)] += 1
    return result


def part_1(data):
    result = 0
    for line in data:
        x, y = line.split("|")
        x = x.split(":")[1]
        win = create_map(x)
        mine = create_map(y)
        points = 0
        for num in mine:
            if num in win:
                points = 1 if points == 0 else points * 2
        result += points
    return result


def part_2(data):
    count = defaultdict(lambda: 1)
    for idx, line in enumerate(data):
        x, y = line.split("|")
        x = x.split(":")[1]
        win = create_map(x)
        mine = create_map(y)
        card_num = idx + 1
        i = 0
        for num in mine:
            if num in win:
                cur_count = count[card_num]
                new_index = card_num + i + 1
                count[new_index] += 1 * cur_count
                i += 1
    return sum(count.values())


if __name__ == "__main__":
    result = part_1(input_file.read_text().splitlines())
    print(f"Part1: {result}")

    result = part_2(input_file.read_text().splitlines())
    print(f"Part2: {result}")
