class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        size1 = len(nums1)
        size2 = len(nums2)
        
        if size1 == 0 or size2 == 0 or k == 0:
            return []
        
        for i in range(min(size1, k)):
            heapq.heappush(heap, [nums1[i] + nums2[0], nums1[i], nums2[0], 0])
        
        res = []
        while heap and k > 0:
            _, num1, num2, idx2 = heapq.heappop(heap)
            res.append([num1, num2])
            if idx2 < size2 - 1:
                new_sum = num1 + nums2[idx2 + 1]
                heapq.heappush(heap, [new_sum, num1, nums2[idx2 + 1], idx2 + 1])
            k -= 1
        
        return res
