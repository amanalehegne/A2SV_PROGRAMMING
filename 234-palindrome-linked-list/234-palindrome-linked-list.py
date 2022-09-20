# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []

        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next

        for i in range(1, len(stack) // 2 + 1):
            indx = -1 * i
            if stack[indx] != head.val:
                return False
            head = head.next
        return True