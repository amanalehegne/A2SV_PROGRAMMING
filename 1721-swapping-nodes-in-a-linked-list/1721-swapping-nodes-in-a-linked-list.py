# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = head
        first = ListNode(0, head)
        for i in range(k):
            fast = fast.next
            first = first.next
        slow = head
        while fast:
            slow = slow.next
            fast = fast.next
        
        temp = first.val
        first.val = slow.val
        slow.val = temp
        return head
        