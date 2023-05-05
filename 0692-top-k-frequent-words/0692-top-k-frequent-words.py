class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        dic = defaultdict(list)
        for key in freq:
            dic[freq[key]].append(key)
        
        heap = []
        for key in dic:
            heapq.heappush(heap, -key)
        
        res = []
        while heap:
            idx = -heapq.heappop(heap)
            words = sorted(dic[idx])
            for word in words:
                res.append(word)
                if len(res) >= k:
                    return res
        
        return res