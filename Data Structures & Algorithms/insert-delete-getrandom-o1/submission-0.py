class RandomizedSet:

    def __init__(self):
        ## set() O(1) insert remove, no O(1) random, since have to get all elements
        ## {} key = val, value = index where value stored in array, []
        self.hashMap = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.hashMap.keys():
            return False
        
        self.hashMap[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashMap.keys():
            return False
        
        lastIndex = len(self.values) - 1
        index = self.hashMap[val]

        self.hashMap[self.values[lastIndex]] = index
        self.values[index] = self.values[lastIndex]
        self.values.pop()
        del self.hashMap[val]

        return True


    def getRandom(self) -> int:
        return random.choice(self.values)
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()