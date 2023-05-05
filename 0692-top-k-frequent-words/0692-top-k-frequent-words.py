class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        dic = dict()
        size = len(words)
        for i in range(size):
            idx = min(dic.get(words[i], [float("inf")])[-1], i)
            freq = dic.get(words[i], [0])[0] + 1
            dic[words[i]] = [freq, idx]
    
        arr = []
        for key in dic:
            heapq.heappush(arr, [-dic[key][0], dic[key][1], key])
        res = []
        while k:
            res.append(heapq.heappop(arr)[-1])
            k -= 1
            
        return res
        
        
        
        