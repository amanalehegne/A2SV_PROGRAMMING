class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l1 = l2 = 0
        if n == 0:
            return
        while l1 < m:
            if nums1[l1] > nums2[l2]:
                temp = nums1[l1]
                nums1[l1] = nums2[l2]
                nums2[l2] = temp
            for i in range(len(nums2) - 1):
                if nums2[i] > nums2[i + 1]:
                    temp = nums2[i]
                    nums2[i] = nums2[i + 1]
                    nums2[i + 1] = temp
            l1 += 1
        for i in range(n):
            nums1[m + i] = nums2[i]
                
        