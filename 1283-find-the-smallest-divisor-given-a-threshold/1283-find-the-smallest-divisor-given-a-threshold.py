class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start, end = 1, max(nums)
        while start <= end:
            perHour = start + (end - start) // 2
            totalTime = sum([ceil(i / perHour) for i in nums])

            if totalTime <= threshold:
                end = perHour - 1
            else:
                start = perHour + 1
            
        return start
        