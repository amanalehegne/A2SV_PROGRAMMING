class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        res = [float("inf")]
        people = [0] * k
        
        def backtrack(idx, current_max):
            if res[0] <= current_max:
                return
            if idx >= len(cookies):
                res[0] = min(res[0], current_max)
                return
            
            length = len(people)
            for i in range(length):
                people[i] += cookies[idx]
                runningMax = max(current_max, people[i])
                backtrack(idx + 1, runningMax)
                people[i] -= cookies[idx]
        
        backtrack(0, 0)
        return res[0]