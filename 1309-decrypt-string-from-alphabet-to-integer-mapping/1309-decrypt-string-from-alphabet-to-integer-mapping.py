class Solution:
    def freqAlphabets(self, s: str) -> str:
        length = len(s)
        countHash = 0
        for char in s:
            if char == "#":
                countHash += 1

        answer = [0] * (length - countHash*2)
        answerIndex = 1
        index = 0
        while index < length:
            if s[(length - 1 - index)] == "#":
                index += 1
                second = s[(length - 1 - index)]
                index += 1
                first = s[(length - 1 - index)]
                answer[-answerIndex] = chr(96 + int(first + second))
            else:
                answer[-answerIndex] = chr(96 + int(s[(length - 1 - index)]))
            index += 1
            answerIndex += 1

        return "".join(answer)
        
        