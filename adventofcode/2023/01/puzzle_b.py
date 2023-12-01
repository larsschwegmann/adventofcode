import re


def word_to_digit(match: re.Match):
    match match.group(1):
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"


with open("input.txt", "r") as fd:
    sum = 0
    for line in fd.readlines():
        words_to_digits = re.sub(
            r"(?=(one|two|three|four|five|six|seven|eight|nine))",
            word_to_digit,
            line
        )
        digits_only = re.sub(
            r"[^\d]",
            "",
            words_to_digits
        )
        sum += int(digits_only[0] + digits_only[-1])

    print(sum)
