class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def bisect_left(arr, target):
            left = 0
            right = len(arr) - 1
            
            while left <= right:
                midPoint = left + (right - left) // 2
                
                if arr[midPoint][0] < target:
                    left = midPoint + 1
                else:
                    right = midPoint - 1
            if left >= len(arr):
                left = -1
            return left
        
        dic = dict()
        length = len(intervals)
        for i in range(length):
            temp = tuple(intervals[i])
            dic[temp] = i
        
        intervals.sort()
        
        res = [0] * length
        for arr in intervals:
            start, end = arr
            x = bisect_left(intervals, end)
            if x > -1:
                x = dic[tuple(intervals[x])]
            idx = dic[tuple(arr)]
            res[idx] = x
        
        return res

        