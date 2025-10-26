class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        resultArr = []
        nums2_copy = nums2[:]  # make a copy so we can remove matched values

        for x in nums1:
            if x in nums2_copy:
                resultArr.append(x)
                nums2_copy.remove(x)  # remove one occurrence

        return resultArr


s1 = Solution()
n1 = [1,2,2,1]
n2 = [2,2]
result = s1.intersect(n1,n2)
print(result)
