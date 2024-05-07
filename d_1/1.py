import re
from os.path import dirname, join

def main():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")

    file1 = open(file_path, "r")
    lines = file1.readlines()
    sum = 0


    for line in lines:
        x = re.findall(r"\d",line)
        if len(x) == 1:
            sum = sum + int(x[0])*10 + int(x[0])
        elif len(x) > 1:
            sum = sum + int(x[0])*10+ int(x[-1])
            
    print(sum)

    file1.close()

if __name__ == "__main__":
    main()