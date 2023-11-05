class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        start = float('inf')
        end = float('-inf')
        for birth, death in logs:
            start = min(start, birth)
            end = max(end, death)
        
        size = (end - start) + 1
        arr = [0] * (size + 1)
        for birth, death in logs:
            arr[birth - start] += 1
            arr[death - start] -= 1
        
        for i in range(1, size + 1):
            arr[i] += arr[i - 1]
        
        res = 0
        for i in range(size + 1):
            if arr[res] < arr[i]:
                res = i

        return res + start