class Solution:
    def nextGreaterElement(self, num1: List[int], num2: List[int]) -> List[int]:
        stack, dic = [], {}
        for i, val in enumerate(num2):
            print(stack)
            # To get the next greater element, we need to store each element in a stack, and if we encounter a 
            # larger element tah the top, that means we found the next larger element for the top. Thus we pop it and repeat the process
            # Store the next greater value of each element in a hash table
            while stack and num2[stack[-1]] < val:
                dic[num2[stack.pop()]] = val
            stack.append(i)
        while stack:
            dic[num2[stack.pop()]] = -1
        for i in range(len(num1)):
            num1[i] = dic.get(num1[i])

        return num1