numbers = [4, 2, 9, 45, 12, 30, 75, 8, 23]

def largest_number(numbers):
    largest_num = numbers[0]
    for number in numbers:
        if number > largest_num:
            largest_num = number
    return largest_num

print(largest_number(numbers))