class TimeMap:

    def __init__(self):
        self.store = {} ## key : [(time, value)...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        keyValue = self.store.get(key, [])
        l, r = 0, len(keyValue) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2 

            if keyValue[m][1] > timestamp:
                r = m - 1
            elif keyValue[m][1] <= timestamp:
                res = str(keyValue[m][0])
                l = m + 1
        
        return res

        
        
