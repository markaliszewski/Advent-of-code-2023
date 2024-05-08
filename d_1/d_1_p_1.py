"""Solution of d_1_p_1_task.txt."""
import re
from os.path import dirname, join

def main():
    """Print sum of all calibration values according to d_1_p_1_task.txt."""
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")

    with open(file_path, "r", encoding="utf-8") as file1:
        lines = file1.readlines()

    sum_of_calibration_values = 0
    for line in lines:
        x = re.findall(r"\d",line)
        if len(x) == 1:
            sum_of_calibration_values += int(x[0])*10 + int(x[0])
        elif len(x) > 1:
            sum_of_calibration_values += int(x[0])*10+ int(x[-1])
    print(sum_of_calibration_values)


if __name__ == "__main__":
    main()
