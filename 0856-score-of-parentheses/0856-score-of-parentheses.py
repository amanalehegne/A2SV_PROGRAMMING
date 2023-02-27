class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        length = len(s)
        stack = []
        count = 0
        for i in range(length):
            if s[i] == ")":
                count += (stack.pop() + max(count, 1))
            else:
                stack.append(count)
                count = 0
        
        return count