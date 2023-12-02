import re

expected = {
    "red": 12,
    "green": 13,
    "blue": 14
}

sum = 0

with open("input.txt", "r") as fd:
    for line in fd.readlines():
        game_id = int(re.match(r"^Game (\d+):", line).group(1))

        subsets = line.split(":")[1].strip()
        for subset in subsets.split(";"):
            subset = subset.strip()
            for draw in subset.split(","):
                draw = draw.strip()
                amount, color = draw.split(" ", maxsplit=1)
                if int(amount) > expected[color]:
                    break
            else:
                continue

            break
        else:
            sum += game_id

print(sum)


