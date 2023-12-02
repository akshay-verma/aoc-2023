import math
from pathlib import Path
from collections import defaultdict

"""
Input Format:
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
"""
 
input_file = Path(__file__).resolve().parent / "input.txt"


cubes_map = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def get_cubes(game: str):
    cubes = game.split(",")
    result = defaultdict(int)
    for cube in cubes:
        parts = cube.strip().split(" ")
        num = int(parts[0].strip())
        color = parts[1].strip()
        result[color] += num
    return result


def part_1(data: list[str]) -> int:
    result = 0
    for idx, line in enumerate(data):
        parts = line.split(";")
        games = [parts[0].split(":")[1].strip()]
        games.extend(parts[1:])
        for game in games:
            cube_data = get_cubes(game.strip())
            if any([num > cubes_map[color] for color, num in cube_data.items()]):
                break
        else:
            result += idx + 1
    return result



def part_2(data: list[str]) -> int:
    result = 0
    for idx, line in enumerate(data):
        parts = line.split(";")
        games = [parts[0].split(":")[1].strip()]
        games.extend(parts[1:])
        min_cube_data = {"red": 0, "green": 0, "blue": 0}
        for game in games:
            cube_data = get_cubes(game.strip())
            min_cube_data = {color: max(num, cube_data.get(color, 0)) for color, num in min_cube_data.items()}
        result += math.prod(min_cube_data.values())
    return result


if __name__ == "__main__":
    data = input_file.read_text()
    result = part_1(data.splitlines())
    print(f"Part1: {result}")
    
    result = part_2(data.splitlines())
    print(f"Part2: {result}")

