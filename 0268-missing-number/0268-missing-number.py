class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum_of_acutal_nums = sum(nums)
        total_sum_of_len_nums = 0 
        for i in range(0,n+1):
            total_sum_of_len_nums += i
        missing_number = total_sum_of_len_nums - total_sum_of_acutal_nums

        return missing_number
        

