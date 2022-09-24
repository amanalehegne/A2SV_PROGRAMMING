class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i, j = 0, 0
        while j < len(popped) - 1:
            if stack:
                # Stack is Not Empty
                if stack[-1] == popped[j]:
                    stack.pop()
                    j += 1
                else:
                    stack.append(pushed[i])
                    i += 1
            else:
                # Stack is Empty
                stack.append(pushed[i])
                i += 1
            # print(stack)
            if i >= len(pushed) and stack[-1] != popped[j]:
                return False
        return True