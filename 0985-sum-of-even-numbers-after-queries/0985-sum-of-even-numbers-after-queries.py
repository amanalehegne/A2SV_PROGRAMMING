class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = list()
        sumValue = sum(i for i in nums if not i % 2)
        for num, index in queries:
            if not nums[index] % 2:
                sumValue -= nums[index]
            nums[index] += num
            if not nums[index] % 2:
                sumValue += nums[index]
            answer.append(sumValue)
        return answer
        