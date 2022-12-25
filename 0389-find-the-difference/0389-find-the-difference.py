class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        elementsOnS = Counter(list(s))
        for char in t:
            if not elementsOnS.get(char):
                return char
            elementsOnS[char] -= 1
                
        