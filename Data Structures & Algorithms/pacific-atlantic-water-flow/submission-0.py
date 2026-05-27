class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ## loop through heights

        ## each one, do a graph traversal (dfs), and check if it can hit the 
        ## bounds of top/left and bottom/right

        ## visited array

        ## {} key = (r,c), value = (p, a)


        ## new thoughts, REVERSE FLOW

        ## check square on top and left border, find in hashmap all that are connected to pacific via a dfs
        ## If we have a stored value for that, we can ignore doing repeated work
        

        ## set() (r,c) that are connected to the pacific
        ###
        

        def dfs(r, c, check):
            dir = [(0,1), (0,-1), (1,0), (-1,0)]
            for dr, dc in dir:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and heights[nr][nc] >= heights[r][c] and (nr, nc) not in check:
                    check.add((nr, nc))
                    dfs(nr, nc, check)

                
            return
                    

        connectedPacific = set() ## store all (r,c) connected to the pacific
        connectedAtlantic = set() ## store all (r,c) connected to the pacific

        ## iterate through top bound
        for c in range(len(heights[0])):
            connectedPacific.add((0, c))
            dfs(0,c,connectedPacific)
        
        ## iterate through left bound
        for r in range(len(heights)):
            connectedPacific.add((r, 0))
            dfs(r,0,connectedPacific)

        ## iterate through bottom
        for c in range(len(heights[0])):
            connectedAtlantic.add((len(heights) - 1, c))
            dfs(len(heights) - 1,c,connectedAtlantic)
        
        ## iterate through left bound
        for r in range(len(heights)):
            connectedAtlantic.add((r, len(heights[0]) - 1))
            dfs(r,len(heights[0]) - 1,connectedAtlantic)

        res = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r,c) in connectedAtlantic and (r,c) in connectedPacific:
                    res.append([r,c])
        
        return res

            




