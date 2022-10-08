class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic, ans = {}, []
        maxim, count = 0, 0
        
        for i in range(len(s)):
            dic[s[i]] = i
    
        for i in range(len(s)):
            maxim = max(maxim, dic[s[i]])
            count += 1
            if i == maxim:
                ans.append(count)
                count = 0
        return ans