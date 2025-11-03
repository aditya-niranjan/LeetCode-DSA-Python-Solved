class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        total_time = 0
        n = len(colors)
        
        # Iterate through consecutive balloons
        for i in range(1, n):
            # If two consecutive colors are same
            if colors[i] == colors[i-1]:
                # Remove the one that takes less time
                total_time += min(neededTime[i], neededTime[i-1])
                # Keep the max time (the one not removed)
                neededTime[i] = max(neededTime[i], neededTime[i-1])
        
        return total_time
