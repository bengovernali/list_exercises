numbers = [4, 2, 9, 45, 12, 30, 75, 8, 23]

def smallest_number(numbers):
    smallest_num = numbers[0]
    for number in numbers:
        if number < smallest_num:
            smallest_num = number
    return smallest_num

print(smallest_number(numbers))