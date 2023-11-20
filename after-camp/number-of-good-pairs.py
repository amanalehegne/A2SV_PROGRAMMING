class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numberOccurance = dict()
        answer = 0
        for num in nums:
            if numberOccurance.get(num):
                answer += numberOccurance.get(num)
            numberOccurance[num] = 1 + numberOccurance.get(num, 0)
        
        return answer