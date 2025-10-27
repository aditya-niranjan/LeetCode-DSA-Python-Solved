class Solution(object):
    def setZeroes(self, matrix):
        r = len(matrix)
        c = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check if first row has zero
        for j in range(c):
            if matrix[0][j] == 0:
                first_row_zero = True

        # Check if first column has zero
        for i in range(r):
            if matrix[i][0] == 0:
                first_col_zero = True

        # Mark zeros in first row/col for the rest of matrix
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set zeroes except first row & col
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle first row
        if first_row_zero:
            for j in range(c):
                matrix[0][j] = 0

        # Handle first column
        if first_col_zero:
            for i in range(r):
                matrix[i][0] = 0

        return matrix
