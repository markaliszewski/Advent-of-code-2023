"""Solution of d_1_p_2_task.txt."""
import re
from os.path import dirname, join


def replace_words_with_digits(line):
    """Replaces word with digit. Be carefull - works spesifically to solve d_1_p_2_task.txt
    and is pretty much useless for other applications."""
    line = line.replace("zero", "z1o")
    line = line.replace("one", "o1e")
    line = line.replace("two", "t2o")
    line = line.replace("three", "t3e")
    line = line.replace("four", "f4r")
    line = line.replace("five", "f5e")
    line = line.replace("six", "s6x")
    line = line.replace("seven", "s7n")
    line = line.replace("eight", "e8h")
    line = line.replace("nine", "n9e")


def main():
    """Print improved sum of all calibration values according to d_1_p_2_task.txt."""
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")

    with open(file_path, "r", encoding="UTF-8") as file1:
        lines = file1.readlines()

    sum_of_calibration_values = 0
    for line in lines:
        replace_words_with_digits(line)
        x = re.findall(r"\d", line)
        if len(x) == 1:
            sum_of_calibration_values += int(x[0])*10 + int(x[0])
        elif len(x) > 1:
            sum_of_calibration_values += int(x[0])*10 + int(x[-1])
    print(sum_of_calibration_values)


if __name__ == "__main__":
    main()
