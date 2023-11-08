from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dp(idx, word):
            size = len(digits)
            if idx == size:
                res.append(word)
                return
            
            for val in graph[digits[idx]]:
                dp(idx + 1, word + val)
        
        res = []
        graph = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        if digits:
            dp(0, "")
        
        return res
