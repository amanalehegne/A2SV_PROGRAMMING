# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        
        if count == 0:
            return None
        if count == n:
            return head.next
        
        temp = head
        for i in range(count - n - 1):
            temp = temp.next
        if temp.next and temp.next.next:
            temp.next = temp.next.next
        else:
            temp.next = None
        return head