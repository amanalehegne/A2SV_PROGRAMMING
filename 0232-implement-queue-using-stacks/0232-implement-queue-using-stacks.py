class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.top = None

    def push(self, x: int) -> None:
        if not self.s1:
            self.top = x
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]
        return self.top

    def empty(self) -> bool:
        if self.s1 or self.s2:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()