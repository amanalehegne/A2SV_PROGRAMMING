class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(arr, left, right):
            start = left
            pivot = arr[start]
            while True:
                while left <= right and pivot >= arr[left]:
                    left += 1
                while left <= right and pivot < arr[right]:
                    right -= 1

                if left <= right:
                    arr[left], arr[right] = arr[right], arr[left]
                else:
                    break

            arr[start], arr[right] = arr[right], arr[start]
            return right


        def quickSelect(arr, left = 0, right = len(nums) - 1):
            if left > right:
                return -1

            idx = partition(arr, left, right)

            length = len(arr)
            res = length - k

            if res > idx:
                return quickSelect(arr, idx + 1, right)
            elif res < idx:
                return quickSelect(arr, left, idx - 1)
            else:
                return arr[res]
        
        return quickSelect(nums)
        