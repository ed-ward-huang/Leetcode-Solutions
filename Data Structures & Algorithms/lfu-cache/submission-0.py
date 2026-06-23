class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        
        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0
    
    def add_most_recent(self, node: Node):
        most_recent = self.tail.prev

        most_recent.next = node
        node.prev = most_recent

        self.tail.prev = node
        node.next = self.tail

        self.size += 1

    def remove(self, node: Node):
        before = node.prev
        after = node.next

        before.next = after
        after.prev = before

        node.prev = None
        node.next = None

        self.size -= 1
    
    def remove_lru(self):
        ## if size permits, remove node right after dummy head node
        if self.size > 0:
            lru = self.head.next
            self.remove(self.head.next)
            return lru
        
        return None
    
    def is_empty(self):
        return self.size == 0

class LFUCache:
    def __init__(self, capacity: int):
        ## track: how often each key is used, recency order among keys with same frequency
        self.store = {} ## key -> Node

        self.freq_to_list = {} ## frequency -> doubly linked list
        ## for recency most recent is at front, least recent is at back

        ## keeps track of least frequent key, to remove, so we can remove like freq_to_list(min_freq)
        self.min_freq = 0

        self.capacity = capacity


    ## must be O(1) time because get and put call it
    def updateLFU(self, node: int):
        old_freq = node.freq
        old_list = self.freq_to_list[old_freq]

        ## remove node from old freq doubly linked list
        old_list.remove(node)
        if old_list.is_empty():
            del self.freq_to_list[old_freq]

            ## Cleanup + make sure if the smallest frequency and only instance of that frequency 
            ## is updated, we increase min_freq by one
            if self.min_freq == old_freq:
                self.min_freq += 1

        ## update frequency (+1)
        node.freq += 1
        new_freq = node.freq

        if new_freq not in self.freq_to_list:
            self.freq_to_list[new_freq] = DoublyLinkedList()
        
        ## add ndoe to new freq doubly linked list
        self.freq_to_list[new_freq].add_most_recent(node)
        
    ## O(1) time
    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        
        self.updateLFU(self.store[key])

        return self.store[key].value

    ## O(1) time
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        ## key exists: update value and frequency
        if key in self.store:
            self.store[key].value = value
            self.updateLFU(self.store[key])
            return

        ## key does not exist, make new key
        if len(self.store) == self.capacity:
            min_freq_list = self.freq_to_list[self.min_freq]
            node_removed = min_freq_list.remove_lru()
            del self.store[node_removed.key]

            if min_freq_list.is_empty():
                del self.freq_to_list[self.min_freq]
                ## no need to worrry about min_freq because we create a key, so min freq will be 1

        new_node = Node(key, value)
        if 1 not in self.freq_to_list:
            self.freq_to_list[1] = DoublyLinkedList()
            
        self.freq_to_list[1].add_most_recent(new_node)
        self.store[new_node.key] = new_node

            ## new keys always start at min_freq of 1, so min_freq whenever new key is added will be 1
        self.min_freq = 1
        
        return



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)