class Solution(object):
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        result = ""
        carry, val, i = 0, 0, 0
        while i < max(len(a), len(b)):
            val = carry
            if i < len(a):
                val += int(a[-(i + 1)])
            if i < len(b):
                val += int(b[-(i + 1)])
            carry, val = divmod(val, 2)
            result += str(val)
            i += 1
        if carry:
            result += str(carry)
        return result[::-1]


if __name__ == '__main__':
    print(Solution().addBinary('11', '1'))
