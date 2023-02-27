class Solution:
    def maxSumRangeQuery(self, arr: List[int], query: List[List[int]]) -> int:
        length = len(arr)
        res = [0] * (length + 1)
        for start, end in query:
            res[start] += 1
            res[end + 1] -= 1
        res = res[:length]
        prefix = 0
        for i in range(length):
            temp = res[i]
            res[i] += prefix
            prefix += temp
        res.sort()
        arr.sort()
        ans = 0
        for i in range(length):
            ans += (res[i] * arr[i])

        return ans % (10**9 + 7)
        