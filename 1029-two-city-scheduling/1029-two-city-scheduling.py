class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr = []
        for cost1, cost2 in costs:
            val = cost1 - cost2
            arr.append([val, cost1, cost2])
        
        arr.sort()
        size = len(costs)
        res = 0
        for i in range(size):
            if i < size // 2:
                res += (arr[i][1])
            else:
                res += (arr[i][2])
        
        return res
    
        