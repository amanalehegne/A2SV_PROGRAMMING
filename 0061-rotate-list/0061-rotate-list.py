# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        if count == 0:
            return
        slow = fast = head
        for i in range(k % count):
            fast = fast.next
        if k % count == 0:
            return head
        while fast.next:
            fast = fast.next
            slow = slow.next
        temp = slow.next
        slow.next = None
        fast.next = head
        return temp