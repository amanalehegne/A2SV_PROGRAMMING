class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        nums = ""
        for i in s:
            if i != ']':
                if i.isdigit():
                    nums += i
                else:
                    if nums:
                        stack.append(nums)
                        nums = ""
                    stack.append(i)
            else:
                temp = []
                while stack[-1] != '[':
                    temp.insert(0, stack.pop())
                stack.pop()
                stack.append(("".join(temp)) * int(stack.pop()))
        return "".join(stack)
                