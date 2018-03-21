class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # ord('A') = 65
        result = 0
        for i, j in enumerate(reversed(s)):
            result += (ord(j) - 65 + 1) * (26 ** i)
        return result

    def titleToNumber1(self, s):
        # 列表推导求和
        cnt = len(s)
        return sum((ord(j) - 64) * 26 ** (cnt - i - 1) for i, j in enumerate(s))
