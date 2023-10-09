class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        def dfs(idx, swapped, memo={}):
            if idx == len(nums1):
                return 0

            if (idx, swapped) in memo:
                return memo[(idx, swapped)]

            check1 = idx == 0

            # NoSwap
            swap = noSwap = float('inf')
            check = nums1[idx] > nums1[idx - 1] and nums2[idx] > nums2[idx - 1]
            if check1 or check:
                noSwap = dfs(idx + 1, False, memo)

            # Swap
            check2 = nums1[idx] > nums2[idx - 1] and nums2[idx] > nums1[idx - 1]

            if check1 or check2:
                nums1[idx], nums2[idx] = nums2[idx], nums1[idx]
                swap = dfs(idx + 1, True, memo) + 1
                nums1[idx], nums2[idx] = nums2[idx], nums1[idx]

            memo[(idx, swapped)] = min(noSwap, swap)
            return memo[(idx, swapped)]
        
        return dfs(0, False)
        