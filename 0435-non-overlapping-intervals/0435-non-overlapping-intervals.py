class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x:x[0])
        prevEnd, count = intervals[0][1], 0
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                count += 1
                # The shorter the interval, the more likely it has no overlap
                prevEnd = min(prevEnd, end)
        return count