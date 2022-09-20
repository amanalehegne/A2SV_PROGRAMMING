# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        dummy = start = ListNode(0, head)
        first = True
        while temp and temp.next:
            next_block = temp.next.next
            prev, current = temp, temp.next

            dummy.next = current
            if first:
                start.next = current
                first = False
            prev.next = current.next
            current.next = prev

            dummy = prev

            temp = next_block
        return start.next