def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range (n):
        for j in range(n - i - 1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]    
    return numbers

def sort_list_declarative(numbers):
    return sorted(numbers)

array = [3, 5, 1, 2, 6, 4]
print(sort_list_imperative(array))
print(sort_list_declarative(array))