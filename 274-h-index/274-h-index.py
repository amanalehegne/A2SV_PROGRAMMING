class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        for i, val in enumerate(citations):
            if len(citations) - i <= val:
                return len(citations) - i
        return 0
        