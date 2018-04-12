class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0:
            return max(nums)
        global_max, local_max = 0, 0
        for i in nums:
            local_max = max(0, local_max + i)
            global_max = max(global_max, local_max)
        return global_max
