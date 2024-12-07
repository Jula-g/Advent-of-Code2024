def sort_orders(rules):
    orders = {}
    for rule in rules:
        before, after = map(int, rule.split("|"))
        if before not in orders:
            orders[before] = []
        orders[before].append(after)
    return orders
    
def sort_updates(orders, updates):
    correct_updates = []
    incorrect_updates = []
    for update in updates:
        numbers = list(map(int, update.split(",")))
        is_correct = True

        for key, values in orders.items():
            if key in numbers:
                key_index = numbers.index(key)
                for value in values:
                    if value in numbers:
                        value_index = numbers.index(value)
                        if key_index > value_index: 
                            is_correct = False
                            
                            break
            if not is_correct:
                break

        if is_correct:
            correct_updates.append(update)
        else:
            incorrect_updates.append(update)
    
    return correct_updates, incorrect_updates


def add_middle_numbers(correct_updates):
    result = 0
    for update in correct_updates:
        numbers = list(map(int, update.split(",")))

        middle_index = int(len(numbers) / 2)
        result += numbers[middle_index] 

    return result

def correct_orders(orders, incorrect_updates):
    corrected_updates= []
    for update in incorrect_updates:
        numbers = list(map(int, update.split(",")))
        changed = True
        while changed: 
            changed = False
            for key, values in orders.items():
                if key in numbers:
                    key_index = numbers.index(key)
                    for value in values:
                        if value in numbers:
                            value_index = numbers.index(value)
                            if key_index > value_index: 
                                numbers[key_index], numbers[value_index] = numbers[value_index], numbers[key_index]
                                changed = True
        corrected_updates.append(",".join(map(str, numbers)))
    return corrected_updates    



if __name__ == "__main__":
    f = open("C:\\Users\\Jula\\Documents\\Advent-of-code2024\\Day5\\puzzle.txt", "r")   
    lines = f.readlines()
    
    rules = []
    updates = []
    for line in lines:
        if line.strip() == "":
            break
        rules.append(line.strip())
    
    updates = [line.strip() for line in lines[len(rules) + 1:]]
    orders = sort_orders(rules)

    # Part 1
    correct_updates, incorrect_updates = sort_updates(orders, updates)
    result = add_middle_numbers(correct_updates)
    print(result)

    # Part 2
    corrected_updates = correct_orders(orders, incorrect_updates)
    result2 = add_middle_numbers(corrected_updates)
    print(result2)
    

           