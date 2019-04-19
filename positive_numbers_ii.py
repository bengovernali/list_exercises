numbers = [-1, 5, 6, -10, 20, -13, 40, -55]

def positive_numbers(numbers):
    positives = []
    for number in numbers:
        if number > 0:
            positives.append(number)
    return positives

print(positive_numbers(numbers))