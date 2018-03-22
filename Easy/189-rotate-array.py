class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 切片操作
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 将前 n-k 个原地反转，将后 k 个原地反转，再将整个数组原地反转
        k = k % len(nums)
        nums[:] = (nums[:-k][::-1] + nums[-k:][::-1])[::-1]
