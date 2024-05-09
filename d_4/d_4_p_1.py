"""Solution of d_4_p_1_task.txt."""
import re
from os.path import dirname, join

def points_of_game(line: str) -> int:
    """
    Returns the number of points gained
    
    :param line: line to scan
    :return: points gained from game included in line
    """
    tmp = re.split(r'[*:*|]', line)
    left_set = list(map(int, re.findall(r'\d+', tmp[1])))
    right_set = list(map(int, re.findall(r'\d+', tmp[2])))
    number_of_hits = len(set(left_set) & set(right_set))
    a = 2 ** (number_of_hits-1)
    if a < 1:
        return 0
    return int(a)

def main() -> None:
    """
    Prints the sum of the power of the minimum set of cubes that must have been present
    in each game included in input.txt according to d_2_p_2_task.txt
    """
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")

    with open(file_path, "r", encoding="UTF-8") as file1:
        lines = file1.readlines()

    sum_of_points = sum(points_of_game(line) for line in lines)

    print(sum_of_points)

if __name__ == "__main__":
    main()
