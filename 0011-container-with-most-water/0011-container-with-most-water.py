class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        maxcount = 0
        while left < right:
            wid = right - left
            dens = min(height[left],height[right])
            result = wid * dens
            maxcount = max(maxcount,result)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1

        return maxcount