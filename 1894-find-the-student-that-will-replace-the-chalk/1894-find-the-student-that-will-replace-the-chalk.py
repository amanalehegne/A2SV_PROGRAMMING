class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_sum = 0
        # Get the total number of calks needed, for a full cycle
        for i, val in enumerate(chalk):
            total_sum += val
            # However sometimes the total number of calks isn't enough to cover a whole round
            if total_sum > k:
                return i

        # The number of calks remaining after certain round is found
        # by getting the remainder of total chalk remaining to the number of calks needed for a cycle
        total_sum = k % total_sum

        prefix_sum = 0
        for i, val in enumerate(chalk):
            prefix_sum += val
            # Check how many chalks we have left for the partial cycle, and get the index when it's not enough
            if prefix_sum > total_sum:
                return i