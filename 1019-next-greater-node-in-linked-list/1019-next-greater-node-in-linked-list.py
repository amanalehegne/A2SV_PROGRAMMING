# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        lst = []

        while head:
            lst.append(head.val)
            head = head.next
        for i in range(len(lst)):
            while len(stack) > 0 and lst[stack[-1]] < lst[i]:
                lst[stack.pop()] = lst[i]
            stack.append(i)
        while len(stack) > 0:
            lst[stack.pop()] = 0
        return lst