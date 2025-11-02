class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """

        # Step 1: create an m x n grid with '.'
        grid = [["." for _ in range(n)] for _ in range(m)]

        # Step 2: place guards and walls
        for r, c in guards:
            grid[r][c] = "G"
        for r, c in walls:
            grid[r][c] = "W"

        # Step 3: for each guard, mark visible cells in all 4 directions
        for gr, gc in guards:

            # Move UP
            i = gr - 1
            while i >= 0 and grid[i][gc] not in ["W", "G"]:
                if grid[i][gc] == ".":
                    grid[i][gc] = "#"
                i -= 1  # move one step up

            # Move DOWN
            i = gr + 1
            while i < m and grid[i][gc] not in ["W", "G"]:
                if grid[i][gc] == ".":
                    grid[i][gc] = "#"
                i += 1  # move one step down

            # Move LEFT
            j = gc - 1
            while j >= 0 and grid[gr][j] not in ["W", "G"]:
                if grid[gr][j] == ".":
                    grid[gr][j] = "#"
                j -= 1  # move one step left

            # Move RIGHT
            j = gc + 1
            while j < n and grid[gr][j] not in ["W", "G"]:
                if grid[gr][j] == ".":
                    grid[gr][j] = "#"
                j += 1  # move one step right

        # Step 4: count all unguarded cells (still ".")
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == ".":
                    count += 1

        return count
