f = open("C:\\Users\\Jula\\Documents\\Advent-of-code2024\\puzzle.txt", "r")
lines = f.readlines()

list1 = []
list2 = []

for line in lines:
    number1, number2 = line.split()
    list1.append(int(number1))
    list2.append(int(number2))

def part1():
    distance = 0
    for i in range(len(list1)):
        min1 = min(list1)
        min2 = min(list2)
        distance += abs(min2 - min1)
        list1.remove(min1)
        list2.remove(min2)

    return distance

def part2():
    similarity = 0
    for i in range(len(list1)):
        number = list1[i]
        amount = 0
        for j in range(len(list2)):
            if number == list2[j]:
                amount += 1

        similarity += number * amount

    return similarity

if __name__ == "__main__":
    print(part1())
    print(part2())        



