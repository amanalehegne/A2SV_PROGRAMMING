class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        size = n * n
        arr = []
        for i in range(size):
            row = i // n
            col = i % n
            val = matrix[row][col]
            if len(arr) >= (size - k + 1):
                heapq.heappop(arr)
            heapq.heappush(arr, val)
        
        
        return arr[0]
        