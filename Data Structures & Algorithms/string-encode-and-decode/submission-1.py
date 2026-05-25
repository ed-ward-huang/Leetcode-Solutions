class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        rvalue = ''
        for s in range(len(strs)):
            if s == 0:
                rvalue = strs[s]
            else:
                rvalue = rvalue + "`" + strs[s]
        
        return rvalue + "`"

    def decode(self, s: str) -> List[str]:
        if s == '':
            return []
        rvalue = []
        curword = 0
        for c in range(len(s)):
            if s[c] == '`':
                rvalue.append(s[curword:c])
                curword = c + 1
        
        return rvalue
            