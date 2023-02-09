# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode(0, head)
        even = ListNode(0, head)
        oddPrev, evenPrev = odd, even
        idx = 0
        while head:
            if idx % 2:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            idx += 1
        odd.next = None
        even.next = oddPrev.next
        return evenPrev.next
        