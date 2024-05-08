str_to_int = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def starts_with_number(text: str):
    for key, value in str_to_int.items():
        if text.startswith(key):
            return value
    return None

def get_number_from_line(line: str) -> int:
    first_number = None
    last_number = None

    for character_no in range(len(line)):
        number1 = int(line[character_no]) if line[character_no].isnumeric() else None
        number2 = starts_with_number(line[character_no:])
        if number1 is not None or number2 is not None:
            number = number1 if number1 is not None else number2
            if first_number is None:
                first_number = number
            last_number = number
    return int(first_number) * 10 + int(last_number)


if __name__ == "__main__":
    with open("./input.txt", "r") as f:
        print(sum([get_number_from_line(line) for line in f.readlines()]))