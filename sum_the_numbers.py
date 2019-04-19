numbers = [5, 4, 9, 7, 8, 9]

def sum_the_numbers(num):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum_the_numbers(numbers))