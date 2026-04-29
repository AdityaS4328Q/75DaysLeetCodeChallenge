import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create sets to track numbers seen in each row, column, and 3x3 box
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set) # key: (r//3, c//3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                
                # Check if value already exists in current row, col, or box
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in boxes[(r // 3, c // 3)]):
                    return False
                
                # Add value to the respective sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3, c // 3)].add(val)
                
        return True