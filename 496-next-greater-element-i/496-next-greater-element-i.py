class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i = 0
        stack = []
        dic = {}
        for i in range(len(nums1)):
            dic[nums1[i]] = i
        for i in nums2:
            if not stack:
                if dic.get(i) is not None:
                    stack.append(i)
            else:
                if stack[-1] > i:
                    if dic.get(i) is not None:
                        stack.append(i)
                else:
                    while stack and stack[-1] < i:
                        val = stack.pop()
                        if dic.get(val) is not None:
                            nums1[dic.get(val)] = i
                    if dic.get(i) is not None:
                        stack.append(i)
        while stack:
            nums1[dic.get(stack.pop())] = -1
        return nums1