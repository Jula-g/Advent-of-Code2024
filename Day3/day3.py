import re

def part1(text_lines):
    sum = 0 
    for line in text_lines:
        matches = re.findall(r'mul\(\d+,\s*\d+\)', line)

        for match in matches:
            numbers = re.findall(r'\d+', match)
            sum += int(numbers[0]) * int(numbers[1])
    return sum 

    
def part2(text):
    matches = re.findall("mul\(\d+,\d+\)|don't\(\)|do\(\)", text)
    total_sum = 0
    for match in matches:
        global skip
        if match == "don't()":
            skip = True  
                
        elif match == "do()":
            skip = False  
            continue      
        if skip: 
            continue
        
        numbers = re.findall(r'\d+', match)
        total_sum += (int(numbers[0]) * int(numbers[1]))       
    return total_sum

    
if __name__ == "__main__":
    f = open("C:\\Users\\Jula\\Documents\\Advent-of-code2024\\Day3\\puzzle.txt", "r")
    lines = f.readlines()
   
    print(part1(lines))
    
    skip = False 
    result2 = 0
    for line in lines:
        result2 += part2(line)
    print(result2) # 88802350