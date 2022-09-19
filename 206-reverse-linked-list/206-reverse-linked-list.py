# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        temp = head
        if temp is None:
            return head
        while temp is not None:
            current = temp
            next = temp.next
            current.next = prev
            prev = temp
            temp = next

        return current