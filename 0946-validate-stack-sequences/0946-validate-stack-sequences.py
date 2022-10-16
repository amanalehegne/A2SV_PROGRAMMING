class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        l = r = 0
        while l < len(pushed):
            stack.append(pushed[l])
            l += 1
            while stack and stack[-1] == popped[r]:
                stack.pop()
                r += 1
        if not stack:
            return True
        else:
            return False