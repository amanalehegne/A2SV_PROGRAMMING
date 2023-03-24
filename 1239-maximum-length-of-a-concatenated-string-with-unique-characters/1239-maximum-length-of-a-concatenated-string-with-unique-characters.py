class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = [0]
        def check(state, check):
            tmp = state[:]
            tmp.append(check)
            tmp = "".join(tmp)
            set_ = set()
            for i in tmp:
                if i in set_:
                    return False
                set_.add(i)

            return True
        
        
        def backtrack(idx, state):
            
            tmp = "".join(state.copy())
            res[0] = max(res[0], len(tmp))
            
            length = len(arr)
            if idx == length:
                return
            
            for i in range(idx, length):
                if check(state, arr[i]):
                    state.append(arr[i])
                    backtrack(i + 1, state)
                    state.pop()
        
        backtrack(0, [])
        return res[0]
            
        