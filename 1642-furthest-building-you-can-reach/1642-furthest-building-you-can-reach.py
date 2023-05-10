class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minheap = []
        size = len(heights)
        laddersUsed = 0
        for i in range(size - 1):
            val = heights[i + 1] - heights[i]
            
            if val > 0:
                heapq.heappush(minheap, val)
                laddersUsed += 1
                
            if laddersUsed > ladders:
                temp = heapq.heappop(minheap)
                if temp > bricks:
                    return i
                bricks -= temp
                laddersUsed -= 1

        return size - 1
