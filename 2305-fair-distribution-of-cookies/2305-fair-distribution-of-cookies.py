class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        res = [float("inf")]
        people = [0] * k
        
        def backtrack(idx, current_max):
            if idx >= len(cookies):
                res[0] = min(res[0], current_max)
                return
            
            length = len(people)
            for i in range(length):
                people[i] += cookies[idx]
                if people[i] < res[0]:
                    backtrack(idx + 1, max(current_max, people[i]))
                people[i] -= cookies[idx]
        
        backtrack(0, 0)
        return res[0]