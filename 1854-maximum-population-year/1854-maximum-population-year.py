class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:        
        startDate = float("inf")
        endDate = -float("inf")
        for x, y in logs:
            startDate = min(startDate, x)
            endDate = max(endDate, y)
            
        print(startDate, endDate)
        
        arr = [0] * (endDate - startDate + 1)
        for start, end in logs:
            arr[start - startDate] += 1
            arr[end - startDate] -= 1
        
        
        prefix = 0
        length = len(arr)
        maxVal = 0
        for i in range(length):
            temp = arr[i]
            arr[i] += prefix
            if arr[maxVal] < arr[i]:
                maxVal = i
            prefix += temp
            
        return startDate + maxVal
        
        