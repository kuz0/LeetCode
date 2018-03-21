class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 能被5整除，有1个0
        # 能被5*5整除，有2个0
        # ......
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)
