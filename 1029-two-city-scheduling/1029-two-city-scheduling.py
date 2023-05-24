class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[0] - x[1])
        size = len(costs)
        res = 0
        for i in range(size):
            if i < size // 2:
                res += (costs[i][0])
            else:
                res += (costs[i][1])
        
        return res
    
        