import re
import numpy as np

def look_for_parts(x,y,numbers_enumeration):
    # function returns all unique digits from x,y neighbourhood in numbers_enumeration
    digit = re.compile(r'[0-9]')

    x_0 = max(x-1,0)
    x_k = min(x+1,numbers_enumeration.shape[1]) 
    y_0 = max(y-1,0)
    y_k = min(y+1,numbers_enumeration.shape[0])  
    
    return np.unique(numbers_enumeration[x_0:x_k+1,y_0:y_k+1])


def main():
    file1 = open("input.txt", "r")
    lines = file1.readlines()
    file1.close()
    
    # each part number have part_no_index assigned which is written in numbers_enumeration array
    numbers_enumeration = np.zeros((len(lines),len(lines[0])-1), dtype=np.int16)
    
    # part_nos contains part numbers which are assigned to numbers_enumeration.
    # It is large just to make sure that it's not smaller than the maximal possible account of part numbers
    part_nos = np.zeros((len(lines)*(len(lines[0])-1))+1)
    part_no_index = 1
    
    # numbers_enumeration and part_nos assignment
    for i,line in enumerate(lines):
        for numbers_in_line in re.finditer(r'\d+',line):
            x_0 = numbers_in_line.start()
            x_k = numbers_in_line.end()
            part_no = int(numbers_in_line.group())
            part_nos[part_no_index] = part_no
            numbers_enumeration[i][x_0:x_k]=numbers_enumeration[i][x_0:x_k]*0+part_no_index
            part_no_index = part_no_index + 1
    
    
    star = re.compile(r'[*]')
    
    # The sum of gear ratios - gear ratio is calculated only if there are exactly 2 parts adjacent to '*',
    # i.e. there are exactly 3 unique numbers in the neighbourhood
    sum = 0
    for i,line in enumerate(lines):
        for j in range(0,len(line)-2):
            if star.match(line[j]):
                part_to_multiply = look_for_parts(i,j,numbers_enumeration)
                if part_to_multiply.shape[0] == 3:
                    sum = sum + part_nos[part_to_multiply[1]]*part_nos[part_to_multiply[2]]
    
    
    print(sum)
    
    

if __name__ == "__main__":
    main()