class Solution:
    def dayCount(self, arr, k):
        length = len(arr)
        runningSum = 0
        count = 1
        for i in range(length):
            runningSum += arr[i]
            if runningSum > k:
                count += 1
                runningSum = arr[i]
        return count
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)
        
        while start <= end:
            mid = start + (end - start) // 2
            getDay = self.dayCount(weights, mid)
            if getDay > days:
                start = mid + 1
            else:
                end = mid - 1

        return start
        
        