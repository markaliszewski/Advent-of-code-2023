
"""Solution of d_1_p_2_task.txt."""
import re
from os.path import dirname, join

MAX_RED = 12
MAX_BLUE = 14
MAX_GREEN = 13

def is_game_valid(line: str) -> tuple[bool, int]:
    """
    reads game_id from line and checks validity according to d_2_p_1_task.txt

    :param line: line to scan
    :return: [is string valid?, game ID]
    """

    entries = re.split(r'[:;,]',line)
    validity = True
    for entry in entries:
        key = re.findall(r'[a-zA-Z]+',entry)
        value = re.findall(r'\d+',entry)
        match key[0]:
            case 'Game':
                game_id = int(value[0])
            case 'red':
                if int(value[0]) > MAX_RED:
                    validity = False
            case 'blue':
                if int(value[0]) > MAX_BLUE:
                    validity = False
            case 'green':
                if int(value[0]) > MAX_GREEN:
                    validity = False
    return validity, game_id

def main():
    """
    Prints the sum of IDs of the valid games in input.txt according to d_2_p_1_task.txt.
    """
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")

    with open(file_path, "r", encoding="UTF-8") as file1:
        lines = file1.readlines()

    sum_of_game_ids = 0

    for line in lines:
        validity, game_id = is_game_valid(line)
        if validity:
            sum_of_game_ids += game_id

    print(sum_of_game_ids)

    file1.close()

if __name__ == "__main__":
    main()
