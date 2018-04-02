class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 双指针
        # 0, 1 的特殊情况
        if not nums:
            return 0

        cnt, i = 1, 1
        while i < len(nums):
            if nums[i] != nums[cnt - 1]:
                nums[cnt] = nums[i]
                cnt += 1
            i += 1
        return cnt
