class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(idx, prev):
            length = len(s)
            if idx == length:
                return True 
            
            # Get the candidates
            for i in range(idx, len(s)):
                num = int(s[idx:i + 1])
                if num + 1 == prev:
                    check = backtrack(i + 1, num)
                    if check:
                        return check
            return False
            
        
        length = len(s)
        for i in range(length - 1):
            num = int(s[:i+1])
            check = backtrack(i + 1, num)
            if check:
                return True
        
        return False
            
        