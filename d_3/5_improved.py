import re
import numpy as np

def look_for_symbols(x_0,x_k,y,symbols_locations):
    
    if x_0-1<0:
        x_0 = 0
    else:
        x_0 = x_0-1
        
    if x_k > symbols_locations.shape[1]:
        x_k = symbols_locations.shape[1]
    else:
        x_k = x_k

    if y-1<0:
        y_0 = 0
    else:
        y_0 = y-1
        
    if y+1 > symbols_locations.shape[0]:
        y_k = symbols_locations.shape[0]
    else:
        y_k = y+1
        
    
    if np.sum(symbols_locations[y_0:y_k+1,x_0:x_k+1]) > 0:
        is_valid = True
    else:
        is_valid = False
    return is_valid




def main():
    file1 = open("input.txt", "r")
    lines = file1.readlines()
    file1.close()
    
    valid_symbols = re.compile(r'[^0-9a-zA-Z\.]')
    
    symbols_locations = np.zeros((len(lines),len(lines[0])-1), dtype=np.int8)
    
    for i in range(0,len(lines)-1):
        for j in range(0,len(lines[0])-2):
            if valid_symbols.match(lines[i][j]):
                symbols_locations[i][j] = 1
    
    
    sum = 0
    for i in range(0,(len(lines))):
        for numbers_in_line in re.finditer(r'\d+',lines[i]):
            is_part_number = False
            x_0 = numbers_in_line.start()
            x_k = numbers_in_line.end()
            part_no = int(numbers_in_line.group())
            if look_for_symbols(x_0,x_k,i,symbols_locations):
                sum = sum + part_no
    print(sum)        
 

if __name__ == "__main__":
    main()