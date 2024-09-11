# Objective: Write a Python function that takes a list of numbers 
# and returns the largest number in the list.

def find_largest_number(numbers):
    largest_number = numbers[0]
    for number in numbers:
        if(number > largest_number):
            largest_number = number
    return largest_number

def find_smallest_number(numbers):
    smallest_number = numbers[0]
    for number in numbers[1:]:
        if(number < smallest_number):
            smallest_number = number
    return smallest_number

test_list = [10, 3, 67, 2, 45]
print(find_largest_number(test_list))
print(find_smallest_number(test_list))