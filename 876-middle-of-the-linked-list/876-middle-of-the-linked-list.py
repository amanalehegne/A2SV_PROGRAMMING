# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        obj = ListNode()
        ans = obj
        count = 0
        temp = head
        while temp is not None:
            temp = temp.next
            count += 1
        index = 0
        while head is not None:
            if index >= count // 2:
                ans.next = ListNode(head.val)
                ans = ans.next
            head = head.next
            index += 1
        return obj.next
        