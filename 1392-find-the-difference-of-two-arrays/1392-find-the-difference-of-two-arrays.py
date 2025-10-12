class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        
        answer = []

        set1 = set(nums1)
        set2 = set(nums2)

        only_num1 = set1 - set2
        only_num2 = set2 - set1
        answer.append(list(only_num1))
        answer.append(list(only_num2))
    
        return answer



s1 = Solution()
n1 = [1,2,3]
n2 = [2,4,6]
result = s1.findDifference(n1,n2)
print(result)