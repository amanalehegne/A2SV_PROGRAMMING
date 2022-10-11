class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        if self.min_stack:
            if self.min_stack[-1] >= val:
                self.min_stack.append(val)
        else:
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]