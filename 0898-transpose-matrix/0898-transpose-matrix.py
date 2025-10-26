class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        rows = len(matrix)
        cols = len(matrix[0])
        result = [[0]* rows for _ in range(cols)]

     
        for i in range(0,rows):
            for j in range(0,cols):
                result[j][i] = matrix[i][j]
        
        return result