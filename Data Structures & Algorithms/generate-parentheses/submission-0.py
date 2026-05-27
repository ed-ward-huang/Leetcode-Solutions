class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        ## ()
        def backtracking(openBrackets: int, closeBrackets: int, substring: List[str]):
            
            ## Base Case
            if openBrackets == closeBrackets and openBrackets == n:
                substringStr = "".join(substring)
                res.append(substringStr)
                return

            validOpenBracket = openBrackets < n

            validCloseBracket = (openBrackets > closeBrackets and closeBrackets < n)
            
            if validOpenBracket:
                substring.append("(")
                backtracking(openBrackets + 1, closeBrackets, substring)
                substring.pop()
            
            if validCloseBracket:
                substring.append(")")
                backtracking(openBrackets, closeBrackets + 1, substring)
                substring.pop()
        
        backtracking(0, 0, [])
        return res


