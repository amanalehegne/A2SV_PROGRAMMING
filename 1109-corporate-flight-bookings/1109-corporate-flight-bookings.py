class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * (n + 1)
        for start, end, val in bookings:
            ans[start - 1] += val
            ans[end] += -val
        prefix = 0
        for i, val in enumerate(ans):
            prefix += val
            ans[i] = prefix
        return ans[:-1]