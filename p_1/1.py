import re


file1 = open("input.txt", "r")

Lines = file1.readlines()
sum = 0


for line in Lines:
    x = re.findall("\d",line)
    if len(x) == 1:
        sum = sum + int(x[0])*10 + int(x[0])
    elif len(x) > 1:
        sum = sum + int(x[0])*10+ int(x[-1])
        
print(sum)



file1.close()