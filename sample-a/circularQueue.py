class MyCircularQueue(object):

    def __init__(self, k):
        self.queue = [None] * k
        self.head = -1
        self.tail = -1
        self.capacity = k
        self.count = 0

    def enQueue(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = value
        self.count += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.queue[self.head] = None  # Or keep the value if needed for other purposes
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        if self.count == 0:
            self.head = -1
            self.tail = -1
        return True

    def Front(self):
        if self.isEmpty():
            return -1  # Or None, depending on your design
        return self.queue[self.head]

    def Rear(self):
        if self.isEmpty():
            return -1  # Or None
        return self.queue[self.tail]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity
    
    def getQueue(self):
        return self.queue


# Your MyCircularQueue object will be instantiated and called as such:
if __name__ == "__main__":
    k = 5
    obj = MyCircularQueue(k)
    obj.enQueue(1) # [1]
    obj.enQueue(2) # [1, 2]
    obj.enQueue(3) # [1, 2, 3]
    print(obj.getQueue())
    
    print(obj.isFull()) # False
    print(obj.Front()) # 1
    print(obj.Rear()) # 3
    print(obj.deQueue()) # True 
    print(obj.getQueue()) # [None, 2, 3, n, n]
    
    print(obj.enQueue(6)) # True 
    print(obj.getQueue()) # [2, 3, 6, n, n]
    
    print(obj.Rear()) # 6
    print(obj.Front()) # 2
    print(obj.enQueue(7)) # True [2, 3, 6, 7]
    print(obj.enQueue(8)) # True [2, 3, 6, 7, 8]
    print(obj.getQueue())
    
    print(obj.isFull()) # True
    print(obj.enQueue(10)) # True [3, 6, 7, 8]    
    print(obj.getQueue())
    
    print(obj.deQueue()) # True [8, None, 3, 6, 7]
    print(obj.getQueue())
    print(obj.Front()) # 3
    print(obj.Rear()) # 8