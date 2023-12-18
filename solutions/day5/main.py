from pathlib import Path
import math

input_file = Path(__file__).parent.resolve() / "input.txt"


def in_range(start: int, rng: int, num: int) -> bool:
    if num >= start and num < start + rng:
        return True
    return False


def part_1(data):
    seeds = data[0].split("seeds:")[1].strip().split(" ")
    s = None
    result = []
    for seed in seeds:
        if s is not None:
            result.append(s)
        s = int(seed)
        found = False
        for line in data[1:]:
            list_map = line.strip().split(" ")
            if not list_map[0].isdigit():
                found = False
                continue
            if found:
                continue
            dest = int(list_map[0])
            src = int(list_map[1])
            rng = int(list_map[2])
            if in_range(src, rng, s):
                s = s - src + dest
                found = True
                continue
    result.append(s)
    return min(result)


def process_input(data):
    seeds = []
    maps = []
    map_index = 0 
    for line in data:
        if line == '': continue

        token = line.split()

        if token[1] == 'map:':
            maps.append([])
            map_index = len(maps) - 1
            continue

        if token[0] == 'seeds:':
            st = 1
            while st < len(token):
                seed_start = int(token[st])
                seed_end = seed_start +int(token[st+1]) - 1
                seeds.append((seed_start, seed_end))
                st += 2
            continue

        dest = int(token[0])
        source = int(token[1])
        range_len = int(token[2])
        source_end = source + range_len - 1
        adjustment = dest - source
        maps[map_index].append((source, source_end, adjustment))
    return seeds, maps


def part_2(data):
    seeds, maps = process_input(data)
    lowest = math.inf
    for seed in seeds:
        result = []
        result.append(seed)
        for map in maps:
            queue = result
            result = []
            while len(queue) > 0:
                source = queue.pop()
                start, end = source
                for m in map:
                    map_start, map_end, adjust = m
                    if start >= map_start and end <= map_end:
                        result.append((start + adjust, end + adjust))
                        break
                    if end < map_start or start > map_end:
                        continue
                    # Start splitting ranges left and right since the full range is not within the map
                    if start < map_start:
                        queue.append((start, map_start-1))
                        queue.append((map_start, end))
                        break
                    if end > map_end:
                        queue.append((start, map_end))
                        queue.append((map_end+1, end))
                        break
                else:
                    result.append(source)
        lowest = min(lowest, min([item[0] for item in result]))
    return lowest


if __name__ == "__main__":
    result = part_1(input_file.read_text().splitlines())
    print(f"Part1: {result}")

    result = part_2(input_file.read_text().splitlines())
    print(f"Part2: {result}")

