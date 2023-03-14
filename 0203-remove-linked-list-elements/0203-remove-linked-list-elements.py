# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        def rec(dummy, cur, k):
            if not cur:
                return
            nxt = cur.next
            if cur.val != k:
                dummy.next = cur
                dummy = dummy.next
                cur.next = None
            rec(dummy, nxt, k)
        
        dummy = ListNode(-1)
        rec(dummy, head, val)
        return dummy.next
        