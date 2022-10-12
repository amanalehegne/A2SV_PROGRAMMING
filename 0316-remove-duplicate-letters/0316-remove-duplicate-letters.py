class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = dict()
        for i in s:
            if dic.get(i):
                dic[i] += 1
            else:
                dic[i] = 1
        stack = []
        inc = dict()
        for i in s:
            if not inc.get(i):
                while stack and stack[-1] > i and dic.get(stack[-1]):
                    inc[stack.pop()] = False
                stack.append(i)
            inc[i] = True
            dic[i] -= 1
        return "".join(stack[:len(dic)])