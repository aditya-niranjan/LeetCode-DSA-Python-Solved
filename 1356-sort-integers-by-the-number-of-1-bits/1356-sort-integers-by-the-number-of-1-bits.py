class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def count_bits(n):
            count = 0
            while n > 0:
                if n % 2 == 1:  
                    count += 1
                n = n // 2      
            return count

        temp = []

    
        for num in arr:
            bits = count_bits(num)
            temp.append((num, bits))

        temp.sort(key=lambda x: (x[1], x[0]))

   
        result = []
        for pair in temp:
            result.append(pair[0])

        return result