class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        indices = []
        length = len(boxes)
        for i in range(length):
            bit = boxes[i]
            if bit == "1":
                indices.append(i)
        answer = []
        for i in range(length):
            count = 0
            for j in indices:
                count += abs(i - j)
            answer.append(count)
        return answer