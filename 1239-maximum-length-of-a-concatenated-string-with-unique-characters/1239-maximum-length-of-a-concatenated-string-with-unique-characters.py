class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = [0]
        def check(state, check):
            
            set_ = set()
            for i in check:
                if i in set_:
                    return False
                set_.add(i)
            
            temp = "".join(state)
            for i in check:
                if i in temp:
                    return False
            
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
            
        