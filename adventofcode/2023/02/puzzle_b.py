from functools import reduce

sum = 0

with open("input.txt", "r") as fd:
    for line in fd.readlines():
        min_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        subsets = line.split(":")[1].strip()
        for subset in subsets.split(";"):
            subset = subset.strip()
            for draw in subset.split(","):
                draw = draw.strip()
                amount, color = draw.split(" ", maxsplit=1)
                min_cubes[color] = max(min_cubes[color], int(amount))

        sum += reduce(lambda acc, x: acc * x, min_cubes.values(), 1)

print(sum)


