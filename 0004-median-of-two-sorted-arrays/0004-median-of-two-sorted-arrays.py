class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        i = j = 0
        result = []

        # Merge both arrays
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        while i < n:
            result.append(nums1[i])
            i += 1

        while j < m:
            result.append(nums2[j])
            j += 1

        total = len(result)
        mid = total // 2

        # Find median
        if total % 2 == 0:
            return (result[mid - 1] + result[mid]) / 2.0
        else:
            return result[mid]
