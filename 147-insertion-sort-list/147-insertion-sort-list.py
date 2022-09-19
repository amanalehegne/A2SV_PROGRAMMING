# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        while head:
            temp = dummy
            while temp.next and temp.next.val < head.val:
                temp = temp.next
            next = head.next
            temp.next, head.next = head, temp.next
            head = next
        return dummy.next