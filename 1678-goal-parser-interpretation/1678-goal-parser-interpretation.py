class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        for char in command:
            if char == ")":
                temp = []
                while stack and stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                if temp:
                    stack.append("al")
                else:
                    stack.append("o")
            else:
                stack.append(char)
        
        return "".join(stack)
        