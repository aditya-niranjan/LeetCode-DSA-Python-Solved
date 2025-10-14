class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)<=1:
            return nums

        mid = len(nums) // 2
        left= nums[:mid]
        right= nums[mid:]

        left = self.sortArray(left)
        right = self.sortArray(right)

        return  self.merge_array(left,right)
    
        
    def merge_array(self,left,right):
        result = []
        i = j = 0
        n,m = len(left),len(right)

        while i < n and j < m:
            if left[i] <= right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        if i < n:
            while i<n:
                result.append(left[i])
                i+=1
        
        if j < m:
            while j<m:
                result.append(right[j])
                j+=1
        return result

s1 = Solution()
n = [5,2,3,1]
result = s1.sortArray(n)
print(result)