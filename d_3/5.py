import re
from os.path import dirname, join

def main():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")

    file1 = open(file_path, "r")
    lines = file1.readlines()

    
    valid_symbols = re.compile(r'[^0-9a-zA-Z\.]')
    sum = 0
    
    i = 0
    for numbers_in_line in re.finditer(r'\d+',lines[i]):
        is_part_number = False
        str_start = numbers_in_line.start()
        str_end = numbers_in_line.end()
        str_val = int(numbers_in_line.group())
        
        for j in range(str_start,str_end):
            if not valid_symbols.match(lines[i+1][j])==None:
                is_part_number = True
        if str_start > 0:
            if not (valid_symbols.match(lines[i+1][str_start-1])==None and valid_symbols.match(lines[i][str_start-1])==None):
                is_part_number = True
        if str_end < len(lines[i])-1:
            if not (valid_symbols.match(lines[i+1][str_end])==None and valid_symbols.match(lines[i][str_end])==None):
                is_part_number = True
            
        if is_part_number:
            sum = sum + str_val
    
    for i in range(1,(len(lines)-1)):
        for numbers_in_line in re.finditer(r'\d+',lines[i]):
            is_part_number = False
            str_start = numbers_in_line.start()
            str_end = numbers_in_line.end()
            str_val = int(numbers_in_line.group())
            
            for j in range(str_start,str_end):
                if not (valid_symbols.match(lines[i+1][j])==None and valid_symbols.match(lines[i-1][j])==None):
                    is_part_number = True
            if str_start > 0:
                if not (valid_symbols.match(lines[i+1][str_start-1])==None and valid_symbols.match(lines[i][str_start-1])==None and valid_symbols.match(lines[i-1][str_start-1])==None):
                    is_part_number = True
            if str_end < len(lines[i])-1:
                if not (valid_symbols.match(lines[i+1][str_end])==None and valid_symbols.match(lines[i][str_end])==None and valid_symbols.match(lines[i-1][str_end])==None):
                    is_part_number = True
            if is_part_number:
                sum = sum + str_val

    
    i = (len(lines)-1)
    for numbers_in_line in re.finditer(r'\d+',lines[i]):
        is_part_number = False
        str_start = numbers_in_line.start()
        str_end = numbers_in_line.end()
        str_val = int(numbers_in_line.group())
        
        for j in range(str_start,str_end):
            if not (valid_symbols.match(lines[i-1][j])==None):
                is_part_number = True
        if str_start > 0:
            if not (valid_symbols.match(lines[i][str_start-1])==None and valid_symbols.match(lines[i-1][str_start-1])==None):
                is_part_number = True
        if str_end < len(lines[i])-1:
            if not (valid_symbols.match(lines[i][str_end])==None and valid_symbols.match(lines[i-1][str_end])==None):
                is_part_number = True
        if is_part_number:
            sum = sum + str_val
    
    print(sum)
    file1.close()

if __name__ == "__main__":
    main()