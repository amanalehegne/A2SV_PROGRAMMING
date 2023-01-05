class Solution:
    def printVertically(self, s: str) -> List[str]:
        length = 0
        words = s.split()
        for word in words:
            length = max(length, len(word))

        answer = []
        for index in range(length):
            temp = []
            for word in words:
                lenWord = len(word)
                if index < lenWord:
                    temp.append(word[index])
                else:
                    temp.append(" ")
            newWord = "".join(temp).rstrip()
            answer.append(newWord)
        return answer
                
                
            
        