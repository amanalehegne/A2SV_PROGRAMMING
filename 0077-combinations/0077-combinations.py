class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def is_valid_state(state):
            if len(state) == k:
                return True
            return False
        
        def get_candidate(start):
            return [i for i in range(start, n+1)]
        
        def backtrack(idx, state):
            check = is_valid_state(state)
            if check:
                res.append(state.copy())
                return
            
            candidate = get_candidate(idx)
            for i in candidate:
                state.append(i)
                backtrack(i + 1, state )
                state.pop()
        
        backtrack(1, [])
        return res
            
        