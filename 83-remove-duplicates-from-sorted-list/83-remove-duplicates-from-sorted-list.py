# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if (head is not None) and (head.next is not None):
            next_elemt = head.next
        else:
            return head
        while next_elemt is not None:
            if current.val == next_elemt.val:
                current.next = next_elemt.next
            else:
                current = current.next
            next_elemt = next_elemt.next
        return head