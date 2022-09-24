class Solution:
    def reverseParentheses(self, s: str) -> str:
        word = ""
        stack = []
        for i in s:
            if i != ')':
                # print(i + "- Not Closing")
                stack.append(i)
            else:
                while stack and stack[-1] != '(':
                    word += stack.pop()
                if stack:
                    stack.pop()
                for j in word:
                    stack.append(j)
                    word = word[1:]
        return "".join(stack)