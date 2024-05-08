"""Solution of d_1_p_2_task.txt."""
import re
from os.path import dirname, join


def replace_words_with_digits(line: str) -> str:
    """
    Replaces word with digit. Be carefull - works spesifically to solve d_1_p_2_task.txt
    and is pretty much useless for other applications.

    :param line: line to be changed
    :return: changed line  
    """
    line = line.replace("zero", "z1o").replace("one", "o1e").replace("two", "t2o")\
    .replace("three", "t3e").replace("four", "f4r").replace("five", "f5e").\
    replace("six", "s6x").replace("seven", "s7n").replace("eight", "e8h").replace("nine", "n9e")
    return line


def main() -> None:
    """
    Print improved sum of all calibration values according to d_1_p_2_task.txt.
    """
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")

    with open(file_path, "r", encoding = "UTF-8") as file1:
        lines = file1.readlines()

    sum_of_calibration_values = 0
    for line in lines:
        line = replace_words_with_digits(line)
        x = re.findall(r"\d", line)
        if len(x) == 1:
            sum_of_calibration_values += int(x[0])*10 + int(x[0])
        elif len(x) > 1:
            sum_of_calibration_values += int(x[0])*10 + int(x[-1])
    print(sum_of_calibration_values)


if __name__ == "__main__":
    main()
