class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ans = []
        for i in intervals:
            if not ans:
                ans.append(i)
            else:
                if ans[-1][-1] >= i[0]:
                    x = min(ans[-1][0], i[0])
                    y = max(ans[-1][-1], i[-1])
                    ans[-1] = [x, y]
                else:
                    ans.append(i)
        return ans