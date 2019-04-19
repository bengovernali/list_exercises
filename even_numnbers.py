numbers = [3, 6, 7, 20, 30, 15, 19, 37, 12, 5]

def even_numbers(numbers):
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

print(even_numbers(numbers))