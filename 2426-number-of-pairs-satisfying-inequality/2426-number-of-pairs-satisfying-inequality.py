class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        """
        [3, 2, 5] and [2, 2, 1]
        nums1[i] - nums1[j] <= nums2[i] - nums2[j] + k
        nums1[i] - nums1[j] - nums2[i] - nums2[j] <= k
        nums1[i] - nums2[i] - nums1[j] - nums2[j] <= k
        i - j <= k
        i <= k + j
        
        if we have an array that has the difference between nums1[k] and nums2[k], we can easily get the values at i and j
        numsDiff = nums1 - nums2
        numsDiff = [1, 0, 4]
        
        Once we got the difference arary we can do a divide and conquer approch on it
        How?
        * Like any divide and conquer approch we have to split the array into two - in this case from the middle
        * Then our left would be for i and the right would be for j because i < j
        * For every j find its i in the array using binary search
        * Merge sort the array as we go up!
        
        """
        def zipArr(arr1, arr2):
            res = []
            length = len(arr1)
            for i in range(length):
                res.append(arr1[i] - arr2[i])
            
            return res
        
        ans = [0]
        def mergeSort(arr, left, right):
            if left == right:
                return arr[left:right+1]

            midPoint = left + (right - left) // 2

            left = mergeSort(arr, left, midPoint)
            right = mergeSort(arr, midPoint + 1, right)

            return solve(left, right, diff)
        
        def solve(arr1, arr2, diff):
            for i in arr2:
                ans[0] += bisect_right(arr1, i + diff)

            l1 = len(arr1)
            l2 = len(arr2)

            i1 = i2 = idx = 0
            res = [0] * (l1 + l2)

            while i1 < l1 and i2 < l2:
                if arr1[i1] < arr2[i2]:
                    res[idx] = arr1[i1]
                    i1 += 1
                else:
                    res[idx] = arr2[i2]
                    i2 += 1
                idx += 1

            while i1 < l1:
                res[idx] = arr1[i1]
                i1 += 1
                idx += 1

            while i2 < l2:
                res[idx] = arr2[i2]
                i2 += 1
                idx += 1

            return res
        
        
        def bisect_right(arr, target):
            left = 0
            right = len(arr) - 1

            while left <= right:
                midPoint = left + (right - left) // 2
                if target < arr[midPoint]:
                    right = midPoint - 1
                elif target >= arr[midPoint]:
                    left = midPoint + 1

            return left
    
        arr = zipArr(nums1, nums2)
        print(arr)
        
        mergeSort(arr, 0, len(arr) - 1)

        return ans[0]
    
        
        