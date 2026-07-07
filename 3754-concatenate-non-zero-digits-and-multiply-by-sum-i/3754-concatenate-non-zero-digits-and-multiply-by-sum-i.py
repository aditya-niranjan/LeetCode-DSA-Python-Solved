class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """

        n = str(n)

        summ = 0
        X = 0
        for i in range(len(n)):
            if n[i] != '0':
                summ += int(n[i])
                X = X * 10 + int(n[i])

        return X * summ