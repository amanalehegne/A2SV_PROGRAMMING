class Solution:
    def freqAlphabets(self, s: str) -> str:
        stack = []
        for nums in s:
            if nums == "#":
                s, f = stack.pop(), stack.pop()
                stack.append(f + s)
            else:
                stack.append(nums)
        answer = []
        for i in stack:
            answer.append(chr(96 + int(i)))
        return "".join(answer)
        