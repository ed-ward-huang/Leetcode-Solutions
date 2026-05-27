class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def dfs(r, c):
            if not 0 <= r < len(board) or not 0 <= c < len(board[0]) or board[r][c] != 'O':
                return
            
            board[r][c] = 'C'
            dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dr, dc in dir:
                dfs(r + dr, c + dc)

        if not board or not board[0]:
            return board
        
        ## top
        for c in range(len(board[0])):
            if board[0][c] == 'O':
                dfs(0, c)
        
        ## left
        for r in range(len(board)):
            if board[r][0] == 'O':
                dfs(r, 0)
        ## bottom
        for c in range(len(board[0])):
            if board[len(board) - 1][c] == 'O':
                dfs(len(board) - 1, c)

        ## right
        for r in range(len(board)):
            if board[r][len(board[0]) - 1] == 'O':
                dfs(r, len(board[0]) - 1)


        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'C':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        
