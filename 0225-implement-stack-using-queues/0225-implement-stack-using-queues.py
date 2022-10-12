class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        if not self.q1 and not self.q2:
            self.q1.append(x)
        else:
            if self.q1:
                self.q2.append(x)
                while self.q1:
                    self.q2.append(self.q1.pop(0))
            elif self.q2:
                self.q1.append(x)
                while self.q2:
                    self.q1.append(self.q2.pop(0))

    def pop(self) -> int:
        if not self.q1 and not self.q2:
            return -1
        else:
            if self.q1:
                return self.q1.pop(0)
            elif self.q2:
                return self.q2.pop(0)

    def top(self) -> int:
        if not self.q1 and not self.q2:
            return -1
        else:
            if self.q1:
                return self.q1[0]
            elif self.q2:
                return self.q2[0]

    def empty(self) -> bool:
        if not self.q1 and not self.q2:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()