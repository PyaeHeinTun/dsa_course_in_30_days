class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    
    def size(self):
        return len(self.stack)

def is_balanced(s: str) -> bool:
    stack = Stack()
    for char in s:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

def reverse_str(s:str) -> str:
    stack = Stack()
    reverse_str = ""
    for char in s:
        stack.push(char)
    
    for _ in range(0,stack.size()):
        reverse_str += stack.peek()
        stack.pop()

    return reverse_str

def calculate_postfix(s:str) -> float:
    simplified_str = s.split(" ")
    stack = Stack()
    for char in simplified_str:
        stack.push(char)
        if char in "+-*/":
            stack.pop()
            current_operator = char
            val_1 = stack.peek()
            stack.pop()
            val_2 = stack.peek()
            stack.pop()

            calculate_result = str(eval(val_2 + current_operator + val_1))
            stack.push(calculate_result)
    
    return stack.peek()