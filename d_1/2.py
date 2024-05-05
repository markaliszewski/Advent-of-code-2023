import re

def main():
    file1 = open("input.txt", "r")

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

