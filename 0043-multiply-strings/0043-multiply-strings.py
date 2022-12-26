class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        length1 = len(num1)
        length2 = len(num2)
        answer = [0] * (length1 + length2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        for index1 in range(length1):
            for index2 in range(length2):
                answerIndex = index1 + index2
                product = answer[answerIndex] + (ord(num1[index1]) - ord("0"))*(ord(num2[index2]) - ord("0"))
                
                answer[answerIndex] = product % 10
                answer[answerIndex + 1] += product // 10

        emptySpace = 0
        answer = answer[::-1]
        for i in range(length1 + length2):
            if answer[i]:
                break
            emptySpace += 1
        answer = answer[emptySpace:]
        return "".join(str(i) for i in answer)
        