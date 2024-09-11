# Basic List Creation and Indexing
fruits = ['apple', 'banana', 'cherry', 'date']

print(fruits[0])  # Output: 'apple'
print(fruits[-1])  # Output: 'date' (Negative indexing)

# Slicing
print(fruits[1:3])  # Output: ['banana', 'cherry'] (From index 1 to 2)

# Modifying Lists
fruits.append('elderberry')  # Adds 'elderberry' to the end
print(fruits)

fruits.insert(1, 'blueberry')  # Inserts 'blueberry' at index 1
print(fruits)

fruits.pop()  # Removes the last item (default)
print(fruits)

fruits.remove('banana')  # Removes 'banana'
print(fruits)

# Sorting Lists
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # Sorts in ascending order
print(numbers)

# List Comprehensions
squares = [x**2 for x in range(1, 6)]  # List of squares [1, 4, 9, 16, 25]
print(squares)
