class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        set1 = set(nums1)
        set2 = set(nums2)

        answer = list(set1 & set2)

        return answer
        

        


n1 = [1,2,2,1]
n2 = [2,2]
s1 = Solution()
result = s1.intersection(n1,n2)
print(result)

