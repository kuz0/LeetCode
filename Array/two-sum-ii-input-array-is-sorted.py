class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 1, len(numbers)
        while left < right:
            two_sum = numbers[left - 1] + numbers[right - 1]
            if two_sum == target:
                return left, right
            elif two_sum < target:
                left += 1
            else:
                right -= 1
