class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Get the maximum distance
        n = trips[-1][-1]
        for i in trips:
            n = max(n, i[-1])
        ans = [0] * (n + 1)
        # Get number of people in the car at the start of their trip and mark their ending (using negative)
        for number, start, end in trips:
            ans[start] += number
            ans[end] -= number
        # Prefix Sum
        # Get the number of people in the car at that point, if it exceeds the capacity, return False
        prefix_sum = 0
        for i in range(len(ans)):
            prefix_sum += ans[i]
            if prefix_sum > capacity:
                return False
            ans[i] = prefix_sum
        return True