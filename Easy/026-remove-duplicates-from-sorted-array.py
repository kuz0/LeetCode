class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        count, i = 0, 1
        while i < len(nums):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
            i += 1

        return count + 1


if __name__ == "__main__":
    print(Solution().removeDuplicates([1, 1, 2]))
