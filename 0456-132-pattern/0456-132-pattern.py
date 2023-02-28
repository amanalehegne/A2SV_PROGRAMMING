class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        length = len(nums)
        jValue = -float("inf")
        for i in range(length):
            idx = length - 1 - i
            if nums[idx] < jValue:
                # the top of our stack is the K value
                # Since we are going backward, the nums[idx] if the I value
                # jVal is the J value
                # Becuse it's a monotonically decreasing stack, we can be sure that jVal < top of stack (stack[-1])
                # if I value (nums[idx]) < J value (jVal), we get the patter nums[idx] (I) < jVal (J) < stack[-1] (K) or 132 => IKJ
                return True
            while stack and stack[-1] < nums[idx]:
                # Since nums[j] > nums[i], we have to maximize the jValue
                # Because we have a monotonic stack (decreasing), the first element is the smallest and the last is the greatest
                # We want to maiximize the jVal as high as possible
                jValue = stack.pop()
                
            stack.append(nums[idx])
        return False