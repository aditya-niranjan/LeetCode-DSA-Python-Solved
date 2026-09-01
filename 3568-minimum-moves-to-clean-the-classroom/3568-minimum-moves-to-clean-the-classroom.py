from collections import deque

class Solution(object):

    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """

        m = len(classroom)
        n = len(classroom[0])

        start_r = 0
        start_c = 0

        # litter_id[r][c] = litter number
        # -1 means this cell is not litter
        litter_id = [[-1] * n for _ in range(m)]

        litter_count = 0

        for r in range(m):
            for c in range(n):

                if classroom[r][c] == 'S':
                    start_r = r
                    start_c = c

                elif classroom[r][c] == 'L':
                    litter_id[r][c] = litter_count
                    litter_count += 1

        if litter_count == 0:
            return 0

        # All bits set means all litter collected
        target = (1 << litter_count) - 1

        # best[r][c][mask] =
        # maximum energy with which we have reached
        # (r, c) having collected 'mask'
        #
        # Flatten it into one list for speed.
        states = m * n * (1 << litter_count)

        best = [-1] * states

        def get_id(r, c, mask):
            return ((r * n + c) << litter_count) | mask

        start_id = get_id(start_r, start_c, 0)

        best[start_id] = energy

        # Store:
        # r, c, mask, remaining_energy
        q = deque()
        q.append((start_r, start_c, 0, energy))

        moves = 0

        directions = (
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        )

        while q:

            size = len(q)

            for _ in range(size):

                r, c, mask, curr_energy = q.popleft()

                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    # Outside grid
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    # Obstacle
                    if classroom[nr][nc] == 'X':
                        continue

                    # No energy
                    if curr_energy == 0:
                        continue

                    # Spend 1 energy
                    new_energy = curr_energy - 1

                    new_mask = mask

                    # Collect litter
                    lid = litter_id[nr][nc]

                    if lid != -1:
                        new_mask |= (1 << lid)

                    # Reset area
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    # All litter collected
                    if new_mask == target:
                        return moves + 1

                    idx = get_id(nr, nc, new_mask)

                    # If we have already reached this exact
                    # position + mask with MORE energy,
                    # this state is useless.
                    if best[idx] >= new_energy:
                        continue

                    # We found a better state
                    best[idx] = new_energy

                    q.append(
                        (nr, nc, new_mask, new_energy)
                    )

            moves += 1

        return -1