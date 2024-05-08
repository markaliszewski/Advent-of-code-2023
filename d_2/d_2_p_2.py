"""Solution of d_2_p_2_task.txt."""
import re
from os.path import dirname, join

def power_of_sets(line):
    """Returns the power of the minimum set of cubes that must have been present
    in game specified in line"""
    max_green = 0
    max_red = 0
    max_blue = 0
    entries = re.split(':|;|,',line)
    for entry in entries:
        key = re.findall(r'[a-zA-Z]+',entry) 
        value = re.findall(r'\d+',entry)
        match key[0]:
            case 'red':
                if int(value[0])>max_red:
                    max_red = int(value[0])
            case 'blue':
                if int(value[0])>max_blue:
                    max_blue = int(value[0])
            case 'green':
                if int(value[0])>max_green:
                    max_green = int(value[0])
    return max_green*max_red*max_blue

def main():
    """Prints the sum of the power of the minimum set of cubes that must have been present
    in each game included in input.txt according to d_2_p_2_task.txt"""
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")

    with open(file_path, "r", encoding="UTF-8") as file1:
        lines = file1.readlines()

    sum_of_power_of_sets = 0
    for line in lines:
        sum_of_power_of_sets += power_of_sets(line)

    print(sum_of_power_of_sets)

if __name__ == "__main__":
    main()
