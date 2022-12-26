class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # sample size = max(100)
        # O(N ^ 2)
        characterWord = dict()
        answer = 0
        for word in words:
            charactersMap = Counter(word)
            temp = list(charactersMap.keys())
            temp.sort()
            characters = "".join(temp)
            if characterWord.get(characters):
                answer += characterWord.get(characters)
            characterWord[characters] = 1 + characterWord.get(characters, 0)
        return answer
            