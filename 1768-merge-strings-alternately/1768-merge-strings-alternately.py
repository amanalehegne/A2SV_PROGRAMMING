class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []
        charsIndex = 0
        word1Length = len(word1)
        word2Length = len(word2)
        while charsIndex < word1Length and charsIndex < word2Length:
            answer.append(word1[charsIndex])
            answer.append(word2[charsIndex])
            charsIndex += 1
        
        while charsIndex < word1Length:
            answer.append(word1[charsIndex])
            charsIndex += 1
        
        while charsIndex < word2Length:
            answer.append(word2[charsIndex])
            charsIndex += 1
        
        return "".join(answer)
        