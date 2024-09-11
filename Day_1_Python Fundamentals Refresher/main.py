# Variables and Data Types
name = "NgaPyi"
age = 26
is_hacker = True
hacker_rating = 9.5

# Conditionals
if is_hacker:
    print(f"{name} is a true hacker!")
else:
    print(f"{name} needs to level up.")

# Loops
# For loop example
for i in range(1, 6):
    print(f"Hacking level {i}")

# While loop example
count = 1
while count <= 5:
    print(f"Executing hack #{count}")
    count += 1

# Functions
def greet_hacker(name):
    return f"Hello, {name}! Ready to hack?"

print(greet_hacker(name))

# List Comprehensions
hacker_levels = [i for i in range(1, 11)]
squared_levels = [x**2 for x in hacker_levels]  # Squares of levels 1 to 10
print(f"Squared hacker levels: {squared_levels}")

# Input/Output
user_input = input("Enter your hacking nickname: ")
print(f"Welcome, {user_input}!")
