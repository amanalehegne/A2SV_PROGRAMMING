class Solution:
    def candy(self, ratings: List[int]) -> int:
        size = len(ratings)
        arr = sorted([(val, i) for i, val in enumerate(ratings)])
        ans = [0] * size
        res = 0
        
        for i in range(size):
            idx = arr[i][1]
            left = right = 0
            
            if idx - 1 >= 0 and ratings[idx - 1] < ratings[idx]:
                left = ans[idx - 1]
            if idx + 1 < size and ratings[idx + 1] < ratings[idx]:
                right = ans[idx + 1]
            
            ans[idx] += max(left, right) + 1
            res += ans[idx]
        
        return res