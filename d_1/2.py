import re

def main():
    file1 = open("input.txt", "r")

    lines = file1.readlines()
    sum = 0

    count = 0
    for line in lines:
        count = count + 1
        if count<20:
            print(line)
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
        if count<20:
            print(line)
            print(x)
        if len(x) == 1:
            sum = sum + int(x[0])*10 + int(x[0])
        elif len(x) > 1:
            sum = sum + int(x[0])*10 + int(x[-1])
            
    print(sum)

    file1.close()

if __name__ == "__main__":
    main()

