class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        cur = ""
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                stack.append((cur, num))
                cur = ""
                num = 0

            elif c == "]":
                storedCur, storedNum = stack.pop()
                cur = storedCur + cur * storedNum
            else:
                cur = cur + c
        
        return cur