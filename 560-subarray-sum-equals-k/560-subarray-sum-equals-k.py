class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, current_sum, dic = 0, 0, {}
        for i in range(len(nums)):
            current_sum += nums[i]
            val = current_sum - k
            if current_sum == k:
                count += 1
            if dic.get(val):
                count += dic.get(val)

            if dic.get(current_sum):
                dic[current_sum] += 1
            else:
                dic[current_sum] = 1
        return count