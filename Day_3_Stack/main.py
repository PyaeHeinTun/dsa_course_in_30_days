class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None
    
    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        return None
    

        
    