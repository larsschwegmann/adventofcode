import re

with open("input.txt", "r") as fd:
    res = sum(
        int(d[0] + d[-1])
        for d in (
            re.sub(r"[^\d]", "", line)
            for line in fd.readlines()
        )
    )

print(res)