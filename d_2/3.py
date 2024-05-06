import re

def main():
    file1 = open("input.txt", "r")

    lines = file1.readlines()
    sum = 0
    count = 0
    
    for line in lines:
        fail = False
        entries = re.split(':|;|,',line)
        for entry in entries:
            key = ''.join(re.findall(r'[a-zA-Z]*',entry)) 
            value = re.findall(r'\d+',entry)
            match key:
                case 'Game':
                    id = int(value[0])
                case 'red':
                    if int(value[0])>12:
                        fail = True
                case 'blue':
                    if int(value[0])>14:
                        fail = True
                case 'green':
                    if int(value[0])>13:
                        fail = True
        if not fail:
             sum = sum + id
            
    print(sum)

    file1.close()

if __name__ == "__main__":
    main()
