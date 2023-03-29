class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """
        For any j point nums[i] > 2 * nums[j], all points less than j the equation is True
        If we found the insert position for 2 * nums[j], we know the numbers of elements smaller than j also, thus the nuber of pairs
        """
        def divideConquer(arr, left, right):
            if left >= right:
                return [arr[right]]
            
            midPoint = left + (right - left) // 2
            leftArr = divideConquer(arr, left, midPoint)
            rightArr = divideConquer(arr, midPoint + 1, right)
            
            return solve(leftArr, rightArr)
        
        ans = [0]
        def solve(arr1, arr2):
            # print(arr1, arr2)
            for i in arr2:
                ans[0] += (len(arr1) - bisect_left(arr1, i*2 + 1))
            
            res = []
            i1 = i2 = 0
            l1, l2 = len(arr1), len(arr2)
            
            while i1 < l1 and i2 < l2:
                if arr1[i1] < arr2[i2]:
                    res.append(arr1[i1])
                    i1 += 1
                else:
                    res.append(arr2[i2])
                    i2 += 1
            
            if i1 < l1:
                res = res + arr1[i1:]
            else:
                res = res + arr2[i2:]
        
            return res
        
        def bisect_left(arr, target):
            left = 0
            right = len(arr) - 1

            while left <= right:
                midPoint = left + (right - left) // 2
                if target > arr[midPoint]:
                    left = midPoint + 1
                elif target <= arr[midPoint]:
                    right = midPoint - 1

            return left
        
        divideConquer(nums, 0, len(nums) - 1)
        return ans[0]
            
        