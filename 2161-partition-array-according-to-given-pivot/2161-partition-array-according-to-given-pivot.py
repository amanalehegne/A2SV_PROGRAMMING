class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small = greater = equal = 0
        for i in nums:
            if i > pivot:
                greater += 1
            elif i < pivot:
                small += 1
            else:
                equal += 1
        ans = [0] * len(nums)

        greater = small + equal
        equal = small
        small = 0

        for i in nums:
            if i > pivot:
                ans[greater] = i
                greater += 1
            elif i < pivot:
                ans[small] = i
                small += 1
            else:
                ans[equal] = i
                equal += 1
        return ans