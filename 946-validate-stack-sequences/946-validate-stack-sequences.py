class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, l = [], 0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[l]:
                stack.pop()
                l += 1
        if stack:
            return False
        return True