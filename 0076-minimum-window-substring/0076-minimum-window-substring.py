class Solution:
    def minWindow(self, s: str, t: str) -> str:
        base = Counter(t)
        baseLength = len(base)
        length = len(s)
        dic = defaultdict(int)
        left = 0
        check = 0
        res = [float("inf"), 0, 0]
        
        for i in range(length):
            dic[s[i]] += 1
            if s[i] in base and dic[s[i]] == base[s[i]]:
                check += 1
            while check == baseLength:
                if res[0] > (i - left + 1):
                    res = [(i - left + 1), left, i+1]
                dic[s[left]] -= 1
                if s[i] in base and dic[s[left]] < base[s[left]]:
                        check -= 1
                left += 1
                
        return s[res[1]:res[-1]]
        