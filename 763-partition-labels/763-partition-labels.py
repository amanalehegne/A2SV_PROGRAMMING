class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic, ans = {}, []
        for i, val in enumerate(s):
            dic[val] = i
        end, count = 0, 0
        for i, val in enumerate(s):
            end = max(end, dic[val])
            if i == end:
                ans.append(count + 1)
                count, end = 0, 0
            else:
                count += 1
        return ans