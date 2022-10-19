class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"
        stack, count = [], 0
        for i in num:
            while count < k and stack and stack[-1] > i:
                stack.pop()
                count += 1
            stack.append(i)
        while count < k:
            stack.pop()
            count += 1
        return str(int("".join(stack)))