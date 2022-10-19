class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, dic = [], {}
        for i, val in enumerate(nums2):
            while stack and nums2[stack[-1]] < val:
                dic[nums2[stack.pop()]] = val
            stack.append(i)
        for i, val in enumerate(nums1):
            nums1[i] = dic.get(val, -1)
        return nums1