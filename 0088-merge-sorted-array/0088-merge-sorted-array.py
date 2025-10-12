class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        answer = []
        i=j=0

        while i<m and j<n:
            if nums1[i] <= nums2[j]:
                answer.append(nums1[i])
                i+=1
            else:
                answer.append(nums2[j])
                j+=1

        if i<m:
            while i<m:
                answer.append(nums1[i])
                i+=1
            
        if j<n:
            while j<n:
                answer.append(nums2[j])
                j+=1
        for idx in range(len(answer)):
            nums1[idx] = answer[idx]

 
s1 = Solution()
n1 = [1,2,3,0,0,0]
n2 = [2,5,6]

result = s1.merge(n1,3,n2,3)
print(result)
