class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                
                value = board[r][c]
                
                if value == ".":
                    continue
                
                # Calculate 3x3 box index
                box_index = (r // 3) * 3 + (c // 3)
                
                # Check if already exists
                if value in rows[r]:
                    return False
                if value in cols[c]:
                    return False
                if value in boxes[box_index]:
                    return False
                
                # Add value
                rows[r].add(value)
                cols[c].add(value)
                boxes[box_index].add(value)
        
        return True