class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n
        for i, j, k in bookings:
            ans[i - 1] += k
            # Limit the seat to the start of the booking to the end, 
            # by giving the flight next to the end a -ve value of the seat
            # so that when we use predix sum, the prefix sum value of the seat dies (not get accounted) 
            if j < n:
                ans[j] -= k
        # Calculate the prefix Sum
        prefix_sum = 0
        for i, val in enumerate(ans):
            prefix_sum += val
            ans[i] = prefix_sum
        return ans