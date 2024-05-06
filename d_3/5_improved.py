import re
import numpy as np

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
    
    np.savetxt('out.txt', symbols_locations, fmt='%d')           
    

#     i = 0
#     for numbers_in_line in re.finditer(r'\d+',lines[i]):
#         is_part_number = False
#         str_start = numbers_in_line.start()
#         str_end = numbers_in_line.end()
#         str_val = int(numbers_in_line.group())
#         
#         for j in range(str_start,str_end):
#             if not valid_symbols.match(lines[i+1][j])==None:
#                 is_part_number = True
#         if str_start > 0:
#             if not (valid_symbols.match(lines[i+1][str_start-1])==None and valid_symbols.match(lines[i][str_start-1])==None):
#                 is_part_number = True
#         if str_end < len(lines[i])-1:
#             if not (valid_symbols.match(lines[i+1][str_end])==None and valid_symbols.match(lines[i][str_end])==None):
#                 is_part_number = True
#             
#         if is_part_number:
#             sum = sum + str_val
#     
#     for i in range(1,(len(lines)-1)):
#         for numbers_in_line in re.finditer(r'\d+',lines[i]):
#             is_part_number = False
#             str_start = numbers_in_line.start()
#             str_end = numbers_in_line.end()
#             str_val = int(numbers_in_line.group())
#             
#             for j in range(str_start,str_end):
#                 if not (valid_symbols.match(lines[i+1][j])==None and valid_symbols.match(lines[i-1][j])==None):
#                     is_part_number = True
#             if str_start > 0:
#                 if not (valid_symbols.match(lines[i+1][str_start-1])==None and valid_symbols.match(lines[i][str_start-1])==None and valid_symbols.match(lines[i-1][str_start-1])==None):
#                     is_part_number = True
#             if str_end < len(lines[i])-1:
#                 if not (valid_symbols.match(lines[i+1][str_end])==None and valid_symbols.match(lines[i][str_end])==None and valid_symbols.match(lines[i-1][str_end])==None):
#                     is_part_number = True
#             if is_part_number:
#                 sum = sum + str_val
# 
#     
#     i = (len(lines)-1)
#     for numbers_in_line in re.finditer(r'\d+',lines[i]):
#         is_part_number = False
#         str_start = numbers_in_line.start()
#         str_end = numbers_in_line.end()
#         str_val = int(numbers_in_line.group())
#         
#         for j in range(str_start,str_end):
#             if not (valid_symbols.match(lines[i-1][j])==None):
#                 is_part_number = True
#         if str_start > 0:
#             if not (valid_symbols.match(lines[i][str_start-1])==None and valid_symbols.match(lines[i-1][str_start-1])==None):
#                 is_part_number = True
#         if str_end < len(lines[i])-1:
#             if not (valid_symbols.match(lines[i][str_end])==None and valid_symbols.match(lines[i-1][str_end])==None):
#                 is_part_number = True
#         if is_part_number:
#             sum = sum + str_val
#     
#     print(sum)

if __name__ == "__main__":
    main()

