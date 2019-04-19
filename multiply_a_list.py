numbers = [2, 4, 6, 8, 10, 12, 14, 16]

def multiply_a_list(numbers, factor):
    new_list = []
    for number in numbers:
        new_list.append(number * factor)
    return new_list

print(multiply_a_list(numbers, 2))