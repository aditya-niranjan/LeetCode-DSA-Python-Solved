class Solution(object):
    def minMoves(self, target, maxDoubles):
        steps = 0
        
        while target > 1 and maxDoubles > 0:
            if target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            steps += 1
        
        # If no doubles left, just subtract remaining in one go
        if target > 1:
            steps += (target - 1)
        
        return steps