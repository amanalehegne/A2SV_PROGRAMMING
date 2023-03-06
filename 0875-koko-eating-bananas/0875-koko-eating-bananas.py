class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        while start <= end:
            perHour = start + (end - start) // 2
            totalTime = sum([ceil(i / perHour) for i in piles])

            if totalTime <= h:
                end = perHour - 1
            else:
                start = perHour + 1
            
        return start
        