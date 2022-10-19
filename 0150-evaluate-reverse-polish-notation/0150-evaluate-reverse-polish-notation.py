class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(i)
            else:
                stack.append(self.oprand(int(stack.pop()), int(stack.pop()), i))
        return int(stack[-1])
    
    def oprand(self, num1, num2, op):
        if op == "+":
            return num2 + num1
        elif op == "-":
            return num2 - num1
        elif op == "*":
            return num2 * num1
        elif op == "/":
            return num2 / num1
        