class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.person = persons
        self.time = times
        
        self.winner = []
        zero = one = 0
        dic = defaultdict(int)
        currentMax = [0, -float("inf")]
        for i in persons:
            dic[i] += 1
            if currentMax[-1] <= dic[i]:
                currentMax = [i, dic[i]]
            self.winner.append(currentMax[0])
            
        
    def bisect_left(self, arr, target):
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            midPoint = left + (right - left) // 2
            
            if arr[midPoint] < target:
                left = midPoint + 1
            else:
                right = midPoint - 1
        if left >= len(arr) or arr[left] != target:
            left -= 1
        return left
        
    def q(self, t: int) -> int:
        idx = self.bisect_left(self.time, t)
        return self.winner[idx]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)