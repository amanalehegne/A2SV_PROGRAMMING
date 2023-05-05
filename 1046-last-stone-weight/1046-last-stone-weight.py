class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        size = len(stones)
        
        for i in range(size):
            stones[i] *= -1
        heapq.heapify(stones)


        while stones:
            size = len(stones)
            if size == 1:
                return -stones[-1]
            first, second = -heapq.heappop(stones), -heapq.heappop(stones)
            val = first - second
            if val:
                heapq.heappush(stones, -val)
        
        return 0

        