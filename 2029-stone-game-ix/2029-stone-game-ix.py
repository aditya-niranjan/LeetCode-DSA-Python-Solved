class Solution(object):
    def stoneGameIX(self, stones):
        
        count = [0, 0, 0]

        # Count stones based on remainder when divided by 3
        for stone in stones:
            count[stone % 3] += 1

        count0 = count[0]
        count1 = count[1]
        count2 = count[2]

        # Even number of remainder-0 stones
        if count0 % 2 == 0:
            return count1 > 0 and count2 > 0

        # Odd number of remainder-0 stones
        return abs(count1 - count2) > 2