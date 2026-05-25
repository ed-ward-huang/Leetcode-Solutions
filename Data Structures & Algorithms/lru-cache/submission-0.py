class Node:
    def __init__(self, key: int, val: int, next: 'Node', prev: 'Node'):
        ## we can update recency with O(1), LRU on the left MRU on the right, if remove LRU then remove leftmost Node, if put/get a node, add it to rightmost also O(1)
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        ## hashmap is O(1) to add, update and get
        self.capacity = capacity
        self.capacityInUse = 0

        ## store pointers to each node, so key = "key", value = Node()
        self.store = {}

        ## dummy, 1, 2, 3, 4, dummy
        ## We assign rightmost node as most recent
        ## We assign leftmost node as least recent
        self.dummyLeft = Node(0, 0, None, None)
        self.dummyRight = Node(0, 0, None, None)

        self.dummyLeft.next = self.dummyRight
        self.dummyRight.prev = self.dummyLeft
    
    def insertMostRecent(self, node):
        mostRecent = self.dummyRight.prev
        mostRecent.next = node
        node.prev = mostRecent

        self.dummyRight.prev = node
        node.next = self.dummyRight
    
    def removeNode(self, node):
        left = node.prev
        right = node.next
        left.next = right
        right.prev = left
        

    ## get constant O(1)
    def get(self, key: int) -> int:
        if key in self.store:
            cur = self.store[key]

            ## update recency
            self.removeNode(cur)
            self.insertMostRecent(cur)
            return cur.val
        else:
            return -1

    ## put constant O(1)
    def put(self, key: int, value: int) -> None:
        
        ## update:
        if key in self.store:
            self.store[key].val = value

            # most recent
            cur = self.store[key]
            self.removeNode(cur)
            self.insertMostRecent(cur)
        
        ## new key
        else:
            ## is capacity already at max?
            if self.capacityInUse == self.capacity:
                
                ## remove LRU
                LRU = self.dummyLeft.next
                self.removeNode(LRU)
                del self.store[LRU.key]

                self.capacityInUse -= 1
            
            newNode = Node(key, value, None, None)
            self.insertMostRecent(newNode)

            self.store[key] = newNode
            self.capacityInUse += 1




        
