class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        al = m + n - 1
        m = m - 1
        n = n - 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[al] = nums1[m]
                m -= 1
                al -= 1
            else:
                nums1[al] = nums2[n]
                n -= 1
                al -= 1
        while n >= 0:
            nums1[al] = nums2[n]
            n -= 1
            al -= 1
