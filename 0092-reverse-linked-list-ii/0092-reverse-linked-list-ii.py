# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # Get the left and its previous
        leftPrev, current = dummy, head
        for i in range(left - 1):
            leftPrev = current
            current = current.next

        # Reverse Elements from left to the right
        prevNode = None
        for i in range(right - left + 1):
            nextNode = current.next
            current.next = prevNode
            prevNode = current
            current = nextNode

        # Connect Endpoints
        leftNode = leftPrev.next
        leftPrev.next = prevNode
        leftNode.next = current

        return dummy.next