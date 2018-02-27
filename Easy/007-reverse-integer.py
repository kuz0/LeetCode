class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)
        result = 0
        while x:
            result = result * 10 + x % 10
            x //= 10
        return result if result < 0x7fffffff else 0

    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = (x > 0) - (x < 0)
        r = int(str(x * s)[::-1])
        return r * s if r < 0x7fffffff else 0


if __name__ == "__main__":
    print Solution().reverse2(123)
    print Solution().reverse2(-321)
