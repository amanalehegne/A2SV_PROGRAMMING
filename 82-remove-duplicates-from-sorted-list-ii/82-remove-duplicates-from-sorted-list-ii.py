# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        current = head

        while current and current.next:
            if current.next and current.val == current.next.val:
                # Get the last element of the duplicate
                while current.next and current.val == current.next.val:
                    current = current.next
                # Once we get that move it to the unique element
                current = current.next
                # connect that to our previous node
                prev.next = current
            else:
                # If the element is unique, move to the next node
                # For prev it's the current node, and or the current it's its next node
                prev = current
                current = current.next
        return dummy.next