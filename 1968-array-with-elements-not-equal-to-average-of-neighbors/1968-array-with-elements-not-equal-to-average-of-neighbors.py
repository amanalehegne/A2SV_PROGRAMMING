class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        l, r = 0, len(nums) - 1
        # To guarentee the number is larger than the avergae of its neibour, the number have to be greater than both its neightbers. 
        # To do that we put the largest element (nums[-1]) between the the two smallest (nums[0] and nums[1]). Then repeat the process
        # To get the largest number and the smallest number easily we sorted the list
        while l <= r:
            ans.append(nums[l])
            if l != r:
                ans.append(nums[r])
            l += 1
            r -= 1
        return ans