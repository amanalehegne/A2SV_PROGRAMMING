class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(left, right):
            if left == right:
                return [nums[left]]
            
            midPoint = left + (right - left) // 2
            
            left = mergeSort(left, midPoint)
            right = mergeSort(midPoint + 1, right)
            
            return sortList(left, right)
        
        def sortList(arr1, arr2):
            l1, l2 = len(arr1), len(arr2)
            i1 = i2 = idx = 0
            res = [0]*(l1 + l2)
            
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
        
        return mergeSort(0, len(nums) - 1)
                
        