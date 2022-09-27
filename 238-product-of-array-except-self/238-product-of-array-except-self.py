class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        dic = {}
        zero = 0
        for i in nums:
            if i == 0:
                zero += 1
                dic[zero] = True
            else:
                total_product *= i
        ans = []
        for i in nums:
            if i == 0:
                if len(dic) == 1:
                    ans.append(total_product)
                else:
                    ans.append(0)
            else:
                if dic:
                    ans.append(0)
                else:
                    ans.append(total_product // i)
        return ans