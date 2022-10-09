# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        # We have two pointers, fast and slow, fast goes twice as fast as the slow pointer, thus when it reach the end,
        # the slow one will be at the middle - the slow will be at half of what the fast is, 
        # if the fast is at the end, the slow will be at the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow