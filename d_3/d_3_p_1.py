"""Solution of d_3_p_1_task.txt."""
import re
from os.path import dirname, join

import numpy as np


def look_for_symbols(x_0: int, x_k: int, y: int, symbols_locations: np.ndarray) -> bool:
    """
    Returns number if valid symbols (according to d_3_p_1_task.txt)
    in neighbourhood of x_0, x_k and y (part number location).
    
    :param x_0: starting index of part number
    :param x_k: ending index of part number
    :param y: line number
    :symbols_locations: 0 - there is no symbol, 1 - there is a symbol 
    :return: are there any symbols in neighbourhood of x_0, x_k and y?
    """
    x_0 = max(x_0-1,0)
    x_k = min(x_k,symbols_locations.shape[1])
    y_0 = max(y-1,0)
    y_k = min(y+1,symbols_locations.shape[0])

    return np.sum(symbols_locations[y_0:y_k+1,x_0:x_k+1]) > 0

def assign_symbols_location(lines: str,symbols_locations: np.ndarray) -> None:
    """
    Assign 1 to any location where is valid symbol

    :param line: line to search
    :param symbols_locations: 0 - there is no symbol, 1 - there is a symbol
    """
    valid_symbols = re.compile(r'[^0-9a-zA-Z\.]')
    for i in range(0, len(lines)-1):
        for j in range(0, len(lines[0])-2):
            if valid_symbols.match(lines[i][j]):
                symbols_locations[i][j] = 1

def sum_of_part_nos(lines: list, symbols_locations: np.ndarray) -> int:
    """
    Returns sum of part numbers
    
    :param lines: list of lines to search
    :param symbols_locations: 0 - there is no symbol, 1 - there is a symbol
    :return: sum of part numbers in lines
    """
    local_sum = 0
    for i, line in enumerate(lines):
        for numbers_in_line in re.finditer(r'\d+', line):
            x_0 = numbers_in_line.start()
            x_k = numbers_in_line.end()
            part_no = int(numbers_in_line.group())
            if look_for_symbols(x_0, x_k, i, symbols_locations):
                local_sum += part_no
    return local_sum

def main() -> None:
    """
    Returns the sum of part numbers of input.txt according to d_3_p_1_task.txt
    """
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")

    with open(file_path, "r", encoding="UTF-8") as file1:
        lines = file1.readlines()


    symbols_locations = np.zeros((len(lines),len(lines[0])-1), dtype=np.int8)
    assign_symbols_location(lines,symbols_locations)

    print(sum_of_part_nos(lines,symbols_locations))

if __name__ == "__main__":
    main()
