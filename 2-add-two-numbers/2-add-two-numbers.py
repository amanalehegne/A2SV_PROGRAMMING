# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        obj = ListNode()
        ans = obj
        carry = 0
        while (l1 is not None) and (l2 is not None):
            sum = l1.val + l2.val + carry
            carry = sum // 10
            sum = sum % 10
            l1 = l1.next
            l2 = l2.next
            ans.next = ListNode(sum)
            ans = ans.next

        while l1 is not None:
            sum = l1.val + carry
            carry = sum // 10
            sum = sum % 10
            l1 = l1.next
            ans.next = ListNode(sum)
            ans = ans.next

        while l2 is not None:
            sum = l2.val + carry
            carry = sum // 10
            sum = sum % 10
            l2 = l2.next
            ans.next = ListNode(sum)
            ans = ans.next

        if carry > 0:
            ans.next = ListNode(carry)
            ans = ans.next

        return obj.next