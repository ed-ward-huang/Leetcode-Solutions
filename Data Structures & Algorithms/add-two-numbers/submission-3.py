# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        ## Do we need to create a new Linked List

        if not l1:
            return l2
        if not l2:
            return l1

        dummy = ListNode()
        head = dummy

        carry = 0

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            value = v1 + v2 + carry
            carry = value // 10
            value = value % 10

            head.next = ListNode(value, None)
            head = head.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry > 0:
            head.next = ListNode(carry, None)
        
        return dummy.next
            





