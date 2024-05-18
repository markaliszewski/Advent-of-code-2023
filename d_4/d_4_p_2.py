"""Solution of d_4_p_1_task.txt."""
import re
from os.path import dirname, join

import numpy as np


def points_of_game(line: str) -> int:
    """
    Returns the number of new cards gained
    
    :param line: line to scan
    :return: number of new cards gained from game included in line
    """
    both_sets_as_strings = re.split(r'[:|]', line)
    left_set = list(map(int, re.findall(r'\d+', both_sets_as_strings[1])))
    right_set = list(map(int, re.findall(r'\d+', both_sets_as_strings[2])))
    number_of_hits = len(set(left_set) & set(right_set))
    return int(number_of_hits)

def main() -> None:
    """
    Prints the sum of all cards obtained and won from input.txt according to d_4_p_2_task.txt
    """
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")

    with open(file_path, "r", encoding="UTF-8") as file1:
        lines = file1.readlines()

    list_of_card_scores = np.zeros(len(lines), dtype=int)
    number_of_cards = np.ones(len(lines), dtype=int)

    for i, line in enumerate(lines):
        list_of_card_scores[i] = points_of_game(line)


    for i, card_score in enumerate(list_of_card_scores):
        for j in range(1,card_score+1):
            try:
                number_of_cards[i+j] += 1*number_of_cards[i]
            except IndexError:
                pass

    print(sum(number_of_cards))

if __name__ == "__main__":
    main()
