class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        stack = [-1]
        length = len(arr)
        for i in range(length):
            idx = length - 1 - i
            val = arr[idx]
            arr[idx] = stack[-1]
            if stack[-1] < val:
                stack.append(val)
        return arr