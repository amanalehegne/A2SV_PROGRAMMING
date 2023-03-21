class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue = []
        ans = 0
        small = len(nums) + 1
        temp = []
        # Create a monotonically increasing dataset
        for i, val in enumerate(nums):
            ans += val
            if ans >= k:
                small = min(small, i + 1)
            while queue and ans - queue[0][0] >= k:
                temp = queue.pop(0)
            if temp:
                small = min(small, i - temp[1])

            while queue and queue[-1][0] >= ans:
                queue.pop()
            queue.append([ans, i])
        if small > len(nums):
            return -1
        return small