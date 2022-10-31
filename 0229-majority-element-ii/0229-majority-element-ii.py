class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans, dic = [], dict()
        for i in nums:
            dic[i] = 1 + dic.get(i, 0)
        for key in dic:
            if dic.get(key) > len(nums) // 3:
                ans.append(key)
        return ans