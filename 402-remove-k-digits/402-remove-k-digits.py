class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        stack = []
        count = 0
        for i in num:
            while stack and stack[-1] > i and count < k:
                stack.pop()
                count += 1
            stack.append(i)
        while stack and count < k:
            stack.pop()
            count += 1
        return str(int("".join(stack)))