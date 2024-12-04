import re

def find_horizontal(lines):
    matches = []
    for line in lines:
        horizontal_matches = re.findall(r"XMAS", line)
        horizontal_backwards_matches = re.findall(r"SAMX", line)
        matches += horizontal_matches + horizontal_backwards_matches
    return matches


def find_vertical(lines):
    matches = []
    for col in range(len(lines[0])):
        for row in range(len(lines)):
            if lines[row][col] == "X":
                if row + 3 < len(lines):
                    vertical_match = lines[row][col] + lines[row+1][col] + lines[row+2][col] + lines[row+3][col]
                    if vertical_match == "XMAS":
                        matches.append(vertical_match)
                if row - 3 >= 0:
                    vertical_match = lines[row][col] + lines[row-1][col] + lines[row-2][col] + lines[row-3][col]
                    if vertical_match == "XMAS":
                        matches.append(vertical_match)   
            else:
                continue
    return matches


def find_diagonal(lines):
    matches = []
    for col in range(len(lines[0])):
        for row in range(len(lines)):
            if lines[row][col] == "X":
                if row + 3 < len(lines) and col + 3 < len(lines[0]):
                    diagonal_match = lines[row][col] + lines[row+1][col+1] + lines[row+2][col+2] + lines[row+3][col+3]
                    if diagonal_match == "XMAS":
                        matches.append(diagonal_match)
                        
                if row - 3 >= 0 and col - 3 >= 0:
                    diagonal_match = lines[row][col] + lines[row-1][col-1] + lines[row-2][col-2] + lines[row-3][col-3]
                    if diagonal_match == "XMAS":
                        matches.append(diagonal_match)

                if row + 3 < len(lines) and col - 3 >= 0:
                    diagonal_match = lines[row][col] + lines[row+1][col-1] + lines[row+2][col-2] + lines[row+3][col-3]
                    if diagonal_match == "XMAS":
                        matches.append(diagonal_match)
                if row - 3 >= 0 and col + 3 < len(lines[0]):
                    diagonal_match = lines[row][col] + lines[row-1][col+1] + lines[row-2][col+2] + lines[row-3][col+3]
                    if diagonal_match == "XMAS":
                        matches.append(diagonal_match)
            else:
                continue
    return matches


def part1(lines):
    return len(find_horizontal(lines)) + len(find_vertical(lines)) + len(find_diagonal(lines))


def part2(lines):
    count = 0
    for col in range(len(lines[0])):
        for row in range(len(lines)):
            if lines[row][col] == "A":
                if row + 1 < len(lines) and col + 1 < len(lines[0]) and row - 1 >= 0 and col - 1 >= 0:
                    diagonal_match1 = lines[row-1][col-1] + lines[row][col] + lines[row+1][col+1]
                    diagonal_match2 = lines[row-1][col+1] + lines[row][col] + lines[row+1][col-1]
                    if (diagonal_match1 == "SAM" or diagonal_match1 == "MAS") and (diagonal_match2 == "SAM" or diagonal_match2 == "MAS"):
                        count += 1
            else:
                continue

    return count
                    

if __name__ == "__main__":
    f = open("C:\\Users\\Jula\\Documents\\Advent-of-code2024\\Day4\\puzzle.txt", "r")
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    print(part1(lines))
    print(part2(lines))
            

        