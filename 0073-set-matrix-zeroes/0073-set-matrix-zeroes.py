class Solution(object):
    def setZeroes(self, matrix):
        r = len(matrix)
        c = len(matrix[0])

        # Flags for first row/column
        fr = fc = False

        # Check first row
        first_row = matrix[0]
        for j in range(c):
            if first_row[j] == 0:
                fr = True
                break

        # Check first column
        for i in range(r):
            if matrix[i][0] == 0:
                fc = True
                break

        # Mark zeros using first row & column
        for i in range(1, r):
            row = matrix[i]
            for j in range(1, c):
                if row[j] == 0:
                    row[0] = 0
                    first_row[j] = 0

        # Zero out cells based on markers
        for i in range(1, r):
            row = matrix[i]
            marker_i = (row[0] == 0)
            for j in range(1, c):
                if marker_i or first_row[j] == 0:
                    row[j] = 0

        # Zero first row if needed
        if fr:
            for j in range(c):
                first_row[j] = 0

        # Zero first column if needed
        if fc:
            for i in range(r):
                matrix[i][0] = 0
