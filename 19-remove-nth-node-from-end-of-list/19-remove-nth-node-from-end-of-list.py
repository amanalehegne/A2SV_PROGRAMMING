# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp1 = temp = head
        count = 0
        while temp1 is not None:
            temp1 = temp1.next
            count += 1
        if count - n == 0:
            head = head.next
        for i in range(count - n - 1):
            if temp is None:
                return head
            temp = temp.next
        if temp.next is not None:
            temp.next = temp.next.next
        else:
            temp.next = None
        return head