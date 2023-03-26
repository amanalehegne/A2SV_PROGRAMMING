class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def check(arr):
            for i in arr:
                if i != 0:
                    return False
            return True
        
        arr = [0] * n
        res = [0]
        
        def backtrack(idx, count):
            length = len(requests)
            if idx == length:
                return
            
            for i in range(idx, length):
                from_, to_ = requests[i]
                arr[from_] -= 1
                arr[to_] += 1
                
                if check(arr):
                    res[0] = max(res[0], count + 1)
                
                backtrack(i + 1, count + 1)
                
                arr[from_] += 1
                arr[to_] -= 1
        
        backtrack(0, 0)
        return res[0]
        
        