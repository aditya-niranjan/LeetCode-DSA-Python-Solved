class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        
        rows = len(mat)
        cols = len(mat[0])

        # Count 1s in each row
        row_count = [0] * rows
        for i in range(rows):
            for j in range(cols):
                row_count[i] += mat[i][j]

        # Count 1s in each column
        col_count = [0] * cols
        for j in range(cols):
            for i in range(rows):
                col_count[j] += mat[i][j]

        # Check for special positions
        special = 0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    special += 1

        return special