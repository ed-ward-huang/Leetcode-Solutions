class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s 
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        index = 0
        while index < len(s):
            ## we want to read chars until '#' key
            length = ""
            while s[index] != "#":
                length = length + s[index]
                index += 1
            
            ## increment again to get past the # key
            index += 1
            length = int(length)
            res.append(s[index:(index+length)])
            index += length
        
        return res

