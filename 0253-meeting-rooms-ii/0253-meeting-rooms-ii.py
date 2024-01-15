class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        arr = []
        for start, end in intervals:
            arr.append([start, True])
            arr.append([end, False])
        
        arr.sort()
        
        count = 0
        res = 0
        for val, check in arr:
            if check:
                count += 1
            else:
                count -= 1
            res = max(res, count)    
        
        return res
        