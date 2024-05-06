import re

def main():
    file1 = open("input.txt", "r")

    lines = file1.readlines()

    
    valid_symbols = re.compile(r'[^0-9\.]')
    
    i = 0
    for numbers_in_line in re.finditer(r'\d+',lines[i]):
        str_start = numbers_in_line.start()
        str_end = numbers_in_line.start()
        str_val = int(numbers_in_line.group())
        
        print(valid_symbols.match(lines[i+1][str_start])==None)
        print(str_end)
        print(str_val)

    file1.close()

if __name__ == "__main__":
    main()

