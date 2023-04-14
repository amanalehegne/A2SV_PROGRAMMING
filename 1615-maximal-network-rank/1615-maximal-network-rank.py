class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        dic = defaultdict(list)
        for x, y in roads:
            dic[x].append(y)
            dic[y].append(x)
        
        res = -float("inf")
        for city1 in range(n):
            for city2 in range(city1 + 1, n):
                count = len(dic[city1]) + len(dic[city2])
                if city2 in dic[city1]:
                    count -= 1
                res = max(res, count)
        
        return res
        