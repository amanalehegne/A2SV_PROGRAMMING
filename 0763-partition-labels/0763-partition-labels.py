class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = dict()
        for i, val in enumerate(s):
            dic[val] = i
        group_size = l = 0
        ans = []
        for i, val in enumerate(s):
            group_size = max(group_size, dic[val])
            if group_size == i:
                ans.append(i - l + 1)
                l = i + 1
        return ans
                
            
        