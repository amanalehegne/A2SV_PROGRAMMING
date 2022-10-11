class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(i)
            else:
                if stack:
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    stack.append(self.evaluateExpression(num2, i, num1))
        return int(stack[-1])

    def evaluateExpression(self, num1, op, num2):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            return num1 / num2