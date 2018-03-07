class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 1
        for i in range(n):
            a, b = b, a + b
        return a

    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs1(n - 1) + self.climbStairs1(n - 2)


if __name__ == "__main__":
    print(Solution().climbStairs(5))
