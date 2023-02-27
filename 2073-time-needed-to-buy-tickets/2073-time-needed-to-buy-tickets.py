class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        length = len(tickets)
        for i in range(length):
            if i <= k:
                res += min(tickets[k], tickets[i])
            else:
                res += min(tickets[k] - 1, tickets[i])
        
        return res
        