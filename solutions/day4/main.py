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


TEST_INPUT = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

if __name__ == "__main__":
    #result = part_1(input_file.read_text().splitlines())
    #print(result)
    
    result = part_1(TEST_INPUT)
    print(result)

