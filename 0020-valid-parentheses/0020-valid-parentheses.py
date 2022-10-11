class Solution:
    def isValid(self, s: str) -> bool:
        opening = {'(': 1, '{': 2, '[': 3}
        closing = {')': 1, '}': 2, ']': 3}
        stack = []

        for i in s:
            if opening.get(i):
                stack.append(i)
            elif closing.get(i):
                if stack and opening.get(stack[-1]) == closing.get(i):
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True