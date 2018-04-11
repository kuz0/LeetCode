class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cnt = 0
        for i in nums:
            if i != val:
                nums[cnt] = i
                cnt += 1
        return cnt
