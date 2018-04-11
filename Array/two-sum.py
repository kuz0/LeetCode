class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, j in enumerate(nums):
            if target - j in lookup:
                return [lookup[target - j], i]
            lookup[j] = i
