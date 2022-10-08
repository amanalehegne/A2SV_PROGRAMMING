class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count, max_count = 0, 0
        dic = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}
        for i in range(k):
            if dic.get(s[i]):
                count += 1
        l, r = 0, i + 1
        while r < len(s):
            max_count = max(max_count, count)
            if dic.get(s[l]):
                count -= 1
            if dic.get((s[r])):
                count += 1
            l += 1
            r += 1
        return max(max_count, count)