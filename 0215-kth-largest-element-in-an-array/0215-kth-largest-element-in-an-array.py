class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        The time complexity would be on avergae case O(n) -> because we are only concerned with only onw half of the each list which means n + n/2 + n/4 + n/8 ... = 2n
        In the worst case it is O(n^2) because we are using quick sort
        """
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
            largest = length - k

            if largest > idx:
                return quickSelect(arr, idx + 1, right)
            elif largest < idx:
                return quickSelect(arr, left, idx - 1)
            else:
                return arr[largest]
        
        return quickSelect(nums)
        