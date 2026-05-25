class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[row])):
                pointer = board[row][col]

                if pointer == '.':
                    continue

                innerGrid = (row // 3, col // 3)

                if pointer in rows[row] or pointer in cols[col] or pointer in boxes[innerGrid]:
                    return False
                
                rows[row].add(pointer)
                cols[col].add(pointer)
                boxes[innerGrid].add(pointer)
        
        return True

