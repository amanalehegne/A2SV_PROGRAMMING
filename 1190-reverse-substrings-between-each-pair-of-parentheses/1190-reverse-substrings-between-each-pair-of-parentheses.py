class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ')':
                stack.append(i)
            else:
                word = ""
                while stack and stack[-1] != '(':
                    word += stack.pop()
                if stack[-1] == '(':
                    stack.pop()
                i = 0
                while i < len(word):
                    stack.append(word[i])
                    i += 1
        return "".join(stack)