class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        # Convert list to string
        dig = "".join(str(x) for x in digits)

        # Add 1
        add = int(dig) + 1

        # Convert back to list of digits
        result = [int(x) for x in str(add)]


        return result