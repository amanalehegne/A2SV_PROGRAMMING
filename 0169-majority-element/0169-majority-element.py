class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = [0, 0]
        dic = dict()
        for i in nums:
            dic[i] = 1 + dic.get(i, 0)
            if count[1] < dic.get(i):
                count = [i, dic.get(i)]
        return count[0]