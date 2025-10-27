class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        r = len(matrix)
        c = len(matrix[0])
        
        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j]==0:
                    self.Mark_infinity(matrix,i,j)

        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                  if matrix[i][j] == float("inf"):
                      matrix[i][j]=0
        return matrix
    
    
    def Mark_infinity(self,matrix,rows,cols):
      
        r =len(matrix)
        c = len(matrix[0])

        for i in range(0,r):
            if matrix[i][cols] != 0:
                matrix[i][cols]=float("inf")

        for j in range(0,c):
            if matrix[rows][j] !=0:
                matrix[rows][j]=float("inf")