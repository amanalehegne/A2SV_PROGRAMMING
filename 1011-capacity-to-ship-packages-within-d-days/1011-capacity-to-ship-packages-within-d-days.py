class Solution:
    def dayCount(self, arr, k):
        length = len(arr)
        runningSum = count = 0
        left = 0
        for i in range(length):
            if runningSum + arr[i] > k:
                left = i
                count += 1
                runningSum = 0
            runningSum += arr[i]
        return count
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)
        
        while start <= end:
            mid = start + (end - start) // 2
            getDay = self.dayCount(weights, mid)
            if getDay < days:
                end = mid - 1
            else:
                start = mid + 1

        return start
        
        