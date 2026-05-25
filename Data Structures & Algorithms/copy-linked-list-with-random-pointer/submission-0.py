"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        store = {} ##key = original Node, value = copied Node

        dummy = Node(0)
        headCopy = dummy

        headOriginal = head

        while headOriginal:
            headCopy.next = Node(headOriginal.val, headOriginal.next)
            store[headOriginal] = headCopy.next

            headCopy = headCopy.next
            headOriginal = headOriginal.next
        
        headOriginal = head
        headCopy = dummy.next

        while headOriginal:
            if headOriginal.random and headOriginal.random in store.keys():
                headCopy.random = store[headOriginal.random]

            headOriginal = headOriginal.next
            headCopy = headCopy.next
        
        return dummy.next

        



