class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        length = len(s)
        stack = []
        for i in range(length):
            if s[i] == ")":
                count = 0
                while stack[-1] != "(":
                    count = stack.pop()
                stack.pop()
                
                prev = 0
                if stack and stack[-1] != "(":
                    prev = stack.pop()
                if count:
                    stack.append(prev + (count * 2))
                else:
                    stack.append(prev + 1)
            else:
                stack.append(s[i])
        
        return sum(stack)