class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = []
        
    def push(self, x):
        self.stack.append(x)
        minimum = self.minimum
        minimum.append(x if not minimum else min(x, minimum[-1]) )
        
    def pop(self):
        self.stack.pop()
        self.minimum.pop()
        
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minimum[-1]
