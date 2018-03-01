class Solution(object):

    def twoSum0(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = list(range(len(nums)))
        for i in index:
            for j in index:
                if i < j and nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i


if __name__ == '__main__':
    print(Solution().twoSum0([2, 7, 11, 15], 22))
