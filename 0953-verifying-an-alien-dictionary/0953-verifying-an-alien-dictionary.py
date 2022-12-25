class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        wordOrder = dict()
        for i, char in enumerate(order):
            wordOrder[char] = chr(97 + i)

        converted = []
        for word in words:
            temp = []
            for char in word:
                temp.append(wordOrder.get(char))
            converted.append("".join(temp))

        prevWord = converted[0]
        length = len(converted)
        for i in range(1, length):
            if prevWord > converted[i]:
                return False
            prevWord = converted[i]

        return True
        