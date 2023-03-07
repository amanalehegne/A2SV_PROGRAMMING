class MyCircularDeque:
    def __init__(self, k: int):
        self.arr = [0] * k
        self.size = k
        self.count = 0
        self.front = -1
        self.rear = 0
    
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.front == -1:
            self.front = 0
            self.rear = 0
        elif self.front == 0:
            self.front = self.size - 1
        else:
            self.front -= 1
        
        self.arr[self.front] = value
        self.count += 1
        return True
    
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.front == -1:
            self.front = 0
            self.rear = 0
        elif self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear += 1
        
        self.arr[self.rear] = value
        self.count += 1
        return True
   
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        elif self.front == self.size - 1:
            self.front = 0
        else:
            self.front += 1
        
        self.count -= 1
        return True
    
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        elif self.rear == 0:
            self.rear = self.size - 1
        else:
            self.rear -= 1
        
        self.count -= 1
        return True
    
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.front]
    
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.rear]
    
    def isEmpty(self) -> bool:
        return self.count == 0
    
    def isFull(self) -> bool:
        return self.count == self.size
