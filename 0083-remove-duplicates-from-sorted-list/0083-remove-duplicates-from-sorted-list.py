# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        dummy = ListNode(0, head)
        temp2 = dummy
        while temp:
            if prev != temp.val:
                dummy.next = temp
                dummy = dummy.next
            prev = temp.val
            temp = temp.next
        dummy.next = None

        return temp2.next
        