class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        i, ans = 0, []
        while i < len(l) and i < len(r):
            temp = nums[l[i]:r[i] + 1]
            temp.sort(reverse=True)
            check = True
            dif = temp[0] - temp[1]
            for j in range(1, r[i] - l[i]):
                if temp[j] - temp[j + 1] != dif:
                    check = False
                    break
            ans.append(check)
            i += 1
        return ans