from math import ceil
class MyQueue:
    def __init__(self):
        self.first = []
        self.second = []


    def push(self, x: int) -> None:
        if not(self.first) and not(self.second):
            self.first.append(x)
        else:
            if self.first:
                while self.first:
                    self.second.append((self.first.pop()))
                self.second.append(x)
            else:
                while self.second:
                    self.first.append((self.second.pop()))
                self.first.append(x)


    def pop(self) -> int:
        if not (self.first) and not (self.second):
            return -1
        else:
            if self.first:
                siz = len(self.first)
                index = ceil(siz / 2) - 1
                val = self.first.pop(index)
            else:
                siz = len(self.second)
                index = ceil(siz / 2) - 1
                val = self.second.pop(index)
        return val


    def peek(self) -> int:
        if not (self.first) and not (self.second):
            return -1
        else:
            if self.first:
                siz = len(self.first)
                index = ceil(siz / 2) - 1
                val = self.first[index]
            else:
                siz = len(self.second)
                index = ceil(siz / 2) - 1
                val = self.second[index]
        return val


    def empty(self) -> bool:
        if not (self.first) and not (self.second):
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()