class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            elif i in ")}]":
                if stack:
                    if (stack[-1] == "(" and i == ")") or (stack[-1] == "{" and i == "}") or (stack[-1] == "[" and i == "]"):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
        return True
        