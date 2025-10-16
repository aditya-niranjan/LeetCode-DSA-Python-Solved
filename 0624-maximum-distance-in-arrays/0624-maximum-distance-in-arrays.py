class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        min_so_far = arrays[0][0]
        max_so_far = arrays[0][-1]
        max_distance = 0 

        for i in range(1,len(arrays)):
            current = arrays[i]

            max_distance = max(
                max_distance,
                abs(current[-1] - min_so_far),
                abs(max_so_far - current[0])
            )

            min_so_far = min(min_so_far, current[0])
            max_so_far = max(max_so_far, current[-1])
        
        return max_distance