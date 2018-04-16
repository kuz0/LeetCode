class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums) // 2]


class Solution1:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = {}
        for i in nums:
            if i not in cnt:
                cnt[i] = 1
            else:
                cnt[i] += 1
        return max(cnt, key=cnt.get)
