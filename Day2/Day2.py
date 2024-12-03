def part1():
    safe = len(lines)
    for line in lines:
        numbers = list(map(int, line.strip().split()))
        for i in range(len(numbers)-1):
            difference = abs(numbers[i] - numbers[i+1])
            if difference > 3:
                safe -= 1
                break

            if numbers[0] < numbers[len(numbers)-1] and numbers[i] >= numbers[i+1]:
                safe -= 1
                break

            if numbers[0] > numbers[len(numbers)-1] and numbers[i] <= numbers[i+1]:
                safe -= 1
                break
        
            if numbers[i] == numbers[i+1]:
                safe -= 1
                break

    return safe


def is_safe(numbers):
    for i in range(len(numbers)-1):
            difference = abs(numbers[i] - numbers[i+1])
            if difference > 3:
                return False
            if numbers[0] < numbers[len(numbers)-1] and numbers[i] >= numbers[i+1]:
                return False
            if numbers[0] > numbers[len(numbers)-1] and numbers[i] <= numbers[i+1]:
                return False
            if numbers[i] == numbers[i+1]:
                return False

    return True

    
def part2():
    safe = len(lines)
    for line in lines:
        count = 0
        numbers = list(map(int, line.strip().split()))
        for i in range(len(numbers)-1):
            difference = abs(numbers[i] - numbers[i+1])
            if difference > 3:
                count+=1
        
            if numbers[0] < numbers[len(numbers)-1] and numbers[i] > numbers[i+1]:
                count+=1
             
            if numbers[0] > numbers[len(numbers)-1] and numbers[i] < numbers[i+1]:
                count+=1
        
            if numbers[i] == numbers[i+1]:
                count+=1
                
            if count == 1:
                if not is_safe(numbers[:i] + numbers[i+1:]):
                    safe -= 1
                    break
                else: 
                    count = 0
                    continue
                    
            if count > 1:
                safe -= 1
                break      

    return safe

if __name__ == "__main__":
    f = open("C:\\Users\\Jula\\Documents\\Advent-of-code2024\\Day2\\puzzle.txt", "r")
    lines = f.readlines()

    print(part1())  
    print(part2())