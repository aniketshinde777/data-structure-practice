class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])

        path = set()
       
        def dfs(row, col, idx):

            if idx == len(word):
                return True

            if (row >= ROW or row < 0 or
                col >= COL or
                col < 0 or 
                word[idx] != board[row][col] or
                (row, col) in path):
                    return False

            path.add((row, col))
            res = (dfs(row + 1, col, idx + 1) or 
            dfs(row - 1, col, idx + 1) or
            dfs(row, col + 1, idx + 1) or
            dfs(row, col - 1, idx + 1))
            path.remove((row, col))
            return res

        for i in range(ROW):
            for j in range(COL):
                if dfs(i, j, 0):
                    return True
        return False



            
