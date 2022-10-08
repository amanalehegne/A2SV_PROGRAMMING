class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        if len(arr) <= 1:
            return
        i = 0
        peek = 0
        while i < len(arr) - 1:
            if arr[i] < arr[i + 1]:
                while i < len(arr) - 1 and arr[i] < arr[i + 1]:
                    i += 1
                peek = i
            else:
                i += 1
        if peek == 0:
            return arr.sort()

        index = peek
        for i in range(peek - 1, len(arr)):
            if arr[peek - 1] < arr[i] < arr[peek]:
                index = i
        self.swap(arr, peek-1, index)
        temp = arr[peek:]
        temp.sort()
        arr[peek:] = temp
        
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        