list_a = [1, 2, 3, 4, 5, 6]
list_b = [2, 4, 6, 8, 10, 12]

def multiply_vectors(numbers1, numbers2):
    new_list = []
    count = 0
    for number in numbers1:
        new_list.append(number * numbers2[count])
        count += 1
    return new_list

print(multiply_vectors(list_a, list_b))