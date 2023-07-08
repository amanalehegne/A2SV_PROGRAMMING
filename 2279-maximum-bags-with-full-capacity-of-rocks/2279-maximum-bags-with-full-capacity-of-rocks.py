class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        bags = len(capacity)
        openSpace = sorted([capacity[i] - rocks[i] for i in range(bags)])

        for i in range(bags):
            if additionalRocks - openSpace[i] < 0:
                return i
            additionalRocks -= openSpace[i]

        return i + 1
