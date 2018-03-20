class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 排序，取中位数
        return sorted(nums)[len(nums) // 2]

    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 遍历列表，统计元素出现的次数，得到字典
        # max(iterable, key, default)
        # 返回最值对应的键
        a = {}
        for i in nums:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1
        return max(a, key=a.get)
