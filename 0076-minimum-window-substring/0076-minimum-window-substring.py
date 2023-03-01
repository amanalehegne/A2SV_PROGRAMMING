class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length = len(s)
        base = Counter(t)
        baseSize = len(base)
        dic = defaultdict(int)
        completeChars = 0
        res = [float("inf"), 0, 0]
        left = 0
        
        for i in range(length):
            dic[s[i]] += 1
            if s[i] in base and dic[s[i]] == base[s[i]]:
                completeChars += 1
            
            while completeChars == baseSize:
                if res[0] > (i - left + 1):
                    res = [(i - left + 1), left, i]
                dic[s[left]] -= 1
                if s[left] in base and dic[s[left]] < base[s[left]]:
                    completeChars -= 1
                left += 1
                
        if res[0] == float("inf"):
            return ""
        return s[res[1] : res[-1] + 1]
                
                
            