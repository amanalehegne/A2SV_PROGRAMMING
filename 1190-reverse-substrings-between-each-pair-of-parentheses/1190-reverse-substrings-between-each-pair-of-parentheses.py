class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ')':
                stack.append(i)
            else:
                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()
                while temp:
                    stack.append(temp.pop(0))
        return "".join(stack)