class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = dict()
        for i in nums:
            if dic.get(i):
                return True
            dic[i] = True
        return False