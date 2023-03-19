class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1

        target = chr(ord(target) + 1)

        while left <= right:
            midPoint = left + (right - left) // 2

            if letters[midPoint] < target:
                left = midPoint + 1
            else:
                right = midPoint - 1

        if left > len(letters) - 1:
            return letters[0]
        return letters[left]
        