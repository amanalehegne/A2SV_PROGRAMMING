class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans, dic = [], dict()
        for i in nums:
            dic[i] = 1 + dic.get(i, 0)
            if dic.get(i) == len(nums) // 3 + 1:
                ans.append(i)
        return ans