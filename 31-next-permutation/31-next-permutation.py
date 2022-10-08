class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        if len(arr) <= 1:
            return
        i, peek = 0, 0
        while i < len(arr) - 1:
            if arr[i] < arr[i + 1]:
                while i < len(arr) - 1 and arr[i] < arr[i + 1]:
                    i += 1
                peek = i
            else:
                i += 1
        # If we dont have any peek, which means the numbers are sorted in ascending order
        if peek == 0:
            return arr.sort()
        # Speacial case when our peek isn't the best value, thus we find a smaller element than the peek, but higher than the element next to the peek.
        index = peek
        for i in range(peek - 1, len(arr)):
            if arr[peek - 1] < arr[i] < arr[peek]:
                index = i
        self.swap(arr, peek-1, index)
        
        # Sorting in ascending order guraentie we have smallest number possible, thus once we swap the values, we have to make sure the elements next to it are the smallest possible values
        temp = arr[peek:]
        temp.sort()
        arr[peek:] = temp
        
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        