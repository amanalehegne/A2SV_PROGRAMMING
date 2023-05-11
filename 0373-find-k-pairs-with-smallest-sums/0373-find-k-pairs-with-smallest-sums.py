class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        size1, size2 = len(nums1), len(nums2)
        for i in range(size1):
            if len(heap) >= k:
                if nums1[i] + nums2[0] >= -heap[0][0]:
                    break
            for j in range(size2):
                val = [-(nums1[i] + nums2[j]), nums1[i], nums2[j]]
                if len(heap) >= k:
                    if -val[0] >= -heap[0][0]:
                        break
                    else:
                        heapq.heappop(heap)
                        heapq.heappush(heap, val)
                else:
                    heapq.heappush(heap, val)
        
        return [[x, y] for z, x, y in heap]
                
                
                