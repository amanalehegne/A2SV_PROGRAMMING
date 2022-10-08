class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count, max_count = 0, 0
        dic = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}
        l = 0
        for i in range(len(s)):
            if i - l >= k:
                max_count = max(max_count, count)
                if dic.get(s[l]):
                    count -= 1
                l += 1
            if dic.get(s[i]):
                count += 1
        return max(max_count, count)