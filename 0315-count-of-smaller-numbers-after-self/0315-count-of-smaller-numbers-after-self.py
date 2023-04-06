class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        size = len(nums)
        nums = [(nums[i], i) for i in range(size)]
        
        def divide(arr, left, right):
            if left >= right:
                return arr[left:right+1]
            
            midPoint = left + (right - left) // 2
            
            leftArr = divide(arr, left, midPoint)
            rightArr = divide(arr, midPoint + 1, right)
            
            return solve(leftArr, rightArr)
        
        dic = defaultdict(int)
        
        def solve(arr1, arr2):
            for i in arr1:
                x = binarySearch(arr2, i[0] - 1)
                dic[i] += x
            
            l1, l2 = len(arr1), len(arr2)
            i1 = i2 = 0
            res = []
            while i1 < l1 and i2 < l2:
                if arr1[i1][0] < arr2[i2][0]:
                    res.append(arr1[i1])
                    i1 += 1
                else:
                    res.append(arr2[i2])
                    i2 += 1
            if i1 < l1:
                res += arr1[i1:]
            else:
                res += arr2[i2:]
            return res
        
        
        def binarySearch(arr, target):
            left = 0
            right = len(arr) - 1

            while left <= right:
                midPoint = left + (right - left) // 2
                if target < arr[midPoint][0]:
                    right = midPoint - 1
                else:
                    left = midPoint + 1

            return left
        
        
        
        nums = divide(nums, 0, size - 1)
        
        res = [0] * size
        for key in dic:
            res[key[1]] = dic[key]
        
        return res
                    