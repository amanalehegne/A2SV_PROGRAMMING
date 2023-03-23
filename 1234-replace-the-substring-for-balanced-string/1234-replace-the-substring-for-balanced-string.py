class Solution:
    def balancedString(self, s: str) -> int:
        dic = {"Q": 0, "W": 0, "E": 0, "R": 0}
        for i in s:
            dic[i] += 1
        
        length = len(s)
        count = length // 4
        left = 0
        res = length
        
        for i in range(length):
            # Get the count of of each characters outside the window
            dic[s[i]] -= 1
            
            # Which substring if removed will give us no more than n / 4
            # Then once we find the substring, we know that substring have to be replaced
            # If the characters outside the window are valid (they are either equal to n / 4 in which case they are valid by them self or they are less than n/4 and the chracters in the window will be replaced to make the valid), we find the substring to replace
            while (dic["Q"] <= count) and (dic["W"] <= count) and (dic["E"] <= count) and (dic["R"] <= count) and left < length:
                # Get the length of the minimum substring
                res = min(res, i - left + 1)
                dic[s[left]] += 1
                left += 1
                
        
        return res