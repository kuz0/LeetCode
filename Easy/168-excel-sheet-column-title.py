class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 二十六进制，注意Z的值
        result = ''
        a = n
        while a:
            result += chr((a - 1) % 26 + ord('A'))
            a = (a - 1) // 26
        return result[::-1]
