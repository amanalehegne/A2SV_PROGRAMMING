class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix, distance = 0, max(z for x, y, z in trips)
        ans = [0] * (distance + 1)
        for people, start, end in trips:
            ans[start] += people
            ans[end] -= people
        for i in ans:
            prefix += i
            if prefix > capacity:
                return False
        return True