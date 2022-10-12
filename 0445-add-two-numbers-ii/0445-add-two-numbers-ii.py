# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
           s2.append(l2.val)
           l2 = l2.next
        print(s1, s2)
        # Sum - Adding the stacks
        add, carry = [], 0
        while s1 and s2:
            get_sum = s1.pop() + s2.pop() + carry
            carry = get_sum // 10
            get_sum = get_sum % 10
            add.append(get_sum)
        while s1:
            get_sum = s1.pop() + carry
            carry = get_sum // 10
            get_sum = get_sum % 10
            add.append(get_sum)
        while s2:
            get_sum = s2.pop() + carry
            carry = get_sum // 10
            get_sum = get_sum % 10
            add.append(get_sum)
        if carry:
            add.append(carry)

        list = []
        for i in range(1, len(add) + 1):
            list.append(ListNode(add[-i]))
        for i in range(len(list) - 1):
            list[i].next = list[i + 1]

        return list[0]