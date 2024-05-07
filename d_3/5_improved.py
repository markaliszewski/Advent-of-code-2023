import re
import numpy as np

def look_for_symbols(x_0,x_k,y,symbols_locations):
    

    x_0 = max(x_0-1,0)
    x_k = min(x_k,symbols_locations.shape[1])
    y_0 = max(y-1,0)        
    y_k = min(y+1,symbols_locations.shape[0])
        

    return np.sum(symbols_locations[y_0:y_k+1,x_0:x_k+1]) > 0


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
    for i, line in enumerate(lines):
        for numbers_in_line in re.finditer(r'\d+',line):
            x_0 = numbers_in_line.start()
            x_k = numbers_in_line.end()
            part_no = int(numbers_in_line.group())
            if look_for_symbols(x_0,x_k,i,symbols_locations):
                sum = sum + part_no
    print(sum)        
 

if __name__ == "__main__":
    main()