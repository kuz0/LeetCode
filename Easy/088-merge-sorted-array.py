class Solution(object):
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
                m = m - 1
                al = al - 1
            else:
                nums1[al] = nums2[n]
                n = n - 1
                al = al - 1
        while n >= 0:
            nums1[al] = nums2[n]
            al = al - 1
            n = n - 1


if __name__ == "__main__":
    A = [1, 3, 5, 0, 0, 0, 0]
    B = [2, 4, 6, 7]
    Solution().merge(A, 3, B, 4)
    print(A)
