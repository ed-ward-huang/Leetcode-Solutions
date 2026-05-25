# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        length = 0
        tmp = dummy.next
        while tmp:
            length += 1
            tmp = tmp.next
        
        deleteNode = length - n + 1

        tmp = dummy.next
        prev = dummy
        while tmp:
            deleteNode -= 1

            if deleteNode == 0:
                nxt = tmp.next
                prev.next = nxt
                break
            
            tmp = tmp.next
            prev = prev.next

        return dummy.next
            




