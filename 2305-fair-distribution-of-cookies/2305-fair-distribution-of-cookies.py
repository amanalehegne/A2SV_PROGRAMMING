class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        res = [float("inf")]
        def backtrack(idx, people):
            if idx >= len(cookies):
                res[0] = min(res[0], max(people))
                return
            
            length = len(people)
            for i in range(length):
                people[i] += cookies[idx]
                if people[i] < res[0]:
                    backtrack(idx + 1, people)
                people[i] -= cookies[idx]
        
        backtrack(0, [0] * k)
        return res[0]