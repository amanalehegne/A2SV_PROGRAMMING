# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        res = l1
        carry = 0
        temp = None
        
        while l1 and l2:
            sumVal = l1.val + l2.val + carry
            carry = sumVal // 10
            sumVal %= 10
            l1.val = sumVal
            
            if l1.next is None: 
                if l2.next is None and carry:
                    l1.next = ListNode(carry)
                    l1 = l1.next
                temp = l1
            
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            sumVal = l1.val + carry
            carry = sumVal // 10
            sumVal %= 10
            l1.val = sumVal
            if l1.next is None and carry:
                l1.next = ListNode(carry)
                l1 = l1.next
            
            l1 = l1.next
        
        while l2:
            sumVal = l2.val + carry
            carry = sumVal // 10
            sumVal %= 10
            temp.next = ListNode(sumVal)
            temp = temp.next
            
            if l2.next is None and carry:
                temp.next = ListNode(carry)
                temp = temp.next
            
            l2 = l2.next
            
        return res
        