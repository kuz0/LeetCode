class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # return False if you are doing this on interview else True
        ori_bin = '{0:032b}'.format(n)
        rev_bin = ori_bin[::-1]
        return int(rev_bin, 2)

    def reverseBits1(self, n):
        res = 0
        for _ in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1
        return res
