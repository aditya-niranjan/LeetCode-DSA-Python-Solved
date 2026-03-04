class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Traverse from right to left
        for i in range(len(digits) - 1, -1, -1):
            
            # If digit is less than 9 → just increment and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If digit is 9 → make it 0 and carry to next position
            digits[i] = 0
        
        # If all digits were 9 (e.g., 9,9,9)
        return [1] + digits