class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

if __name__ == "__main__":
    minStack =  MinStack()
    print("Pushing: 1")
    minStack.push(1)
    print("Pushing: 2")
    minStack.push(2)
    print("Pushing: 0")
    minStack.push(0)
    
    print("Get Min:", minStack.getMin())  # returns 0
    
    print("Pop:", minStack.pop()) # returns 2
    print("Top:", minStack.top()) # returns 1
    print("Get Min:", minStack.getMin()) # returns 1