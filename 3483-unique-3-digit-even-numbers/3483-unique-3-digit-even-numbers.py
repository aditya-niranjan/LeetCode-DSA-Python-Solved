class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        d = digits
        seen = set()

        for i in range(len(d)):
            for j in range(len(d)):
                for k in range(len(d)):
                    
                    if d[i] == 0:
                        continue

                    if i == j or j == k or i == k:
                        continue

                    num = int(str(d[i]) + str(d[j]) + str(d[k]))

                    if num % 2 == 0:
                        seen.add(num)

        return len(seen)