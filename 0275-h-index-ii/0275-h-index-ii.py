class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        
        left = 0
        right = length - 1
        
        while left <= right:
            midPoint = left + (right-left) // 2
            
            if length - midPoint > citations[midPoint]:
                left = midPoint + 1
            else:
                right = midPoint - 1

        return length - left
        