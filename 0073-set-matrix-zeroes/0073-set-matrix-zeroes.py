class Solution(object):
    def setZeroes(self, matrix):
        r = len(matrix)
        c = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check if first row has zero
        row0 = matrix[0]
        for j in range(c):
            if row0[j] == 0:
                first_row_zero = True
                break

        # Check if first column has zero
        for i in range(r):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Mark rows and columns
        for i in range(1, r):
            row = matrix[i]
            for j in range(1, c):
                if row[j] == 0:
                    matrix[i][0] = 0
                    row0[j] = 0

        # Apply zeroes using markers
        for i in range(1, r):
            row = matrix[i]
            if row[0] == 0:
                for j in range(1, c):
                    row[j] = 0
            else:
                for j in range(1, c):
                    if row0[j] == 0:
                        row[j] = 0

        # Zero out first row
        if first_row_zero:
            for j in range(c):
                row0[j] = 0

        # Zero out first column
        if first_col_zero:
            for i in range(r):
                matrix[i][0] = 0

        return matrix
