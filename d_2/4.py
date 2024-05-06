import re

def main():
    file1 = open("input.txt", "r")

    lines = file1.readlines()
    result = 0
    
    for line in lines:
        fail = False
        max_green = 0
        max_red = 0
        max_blue = 0
        entries = re.split(':|;|,',line)
        for entry in entries:
            key = re.findall(r'[a-zA-Z]+',entry) 
            value = re.findall(r'\d+',entry)
            match key[0]:
                case 'red':
                    if int(value[0])>max_red:
                        max_red = int(value[0])
                case 'blue':
                    if int(value[0])>max_blue:
                        max_blue = int(value[0])
                case 'green':
                    if int(value[0])>max_green:
                        max_green = int(value[0])
                        
        result = result + max_green*max_red*max_blue
            
    print(result)

    file1.close()

if __name__ == "__main__":
    main()

