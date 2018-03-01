class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        decimal = 0
        for i, j in enumerate(s):
            if i > 0 and n_map[j] > n_map[s[i - 1]]:
                decimal += n_map[j] - 2 * n_map[s[i - 1]]
            else:
                decimal += n_map[j]
        return decimal


if __name__ == "__main__":
    print(Solution().romanToInt("IIVX"))
    print(Solution().romanToInt("MMMCMXCIX"))
