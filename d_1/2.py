import re
from os.path import dirname, join

def main():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")

    file1 = open(file_path, "r")
    lines = file1.readlines()
    sum = 0

    for line in lines:
        line = line.replace("zero","z1o")
        line = line.replace("one","o1e")
        line = line.replace("two","t2o")
        line = line.replace("three","t3e")
        line = line.replace("four","f4r")
        line = line.replace("five","f5e")
        line = line.replace("six","s6x")
        line = line.replace("seven","s7n")
        line = line.replace("eight","e8h")
        line = line.replace("nine","n9e")
        x = re.findall(r"\d",line)
        if len(x) == 1:
            sum = sum + int(x[0])*10 + int(x[0])
        elif len(x) > 1:
            sum = sum + int(x[0])*10 + int(x[-1])
            
    print(sum)

    file1.close()

if __name__ == "__main__":
    main()