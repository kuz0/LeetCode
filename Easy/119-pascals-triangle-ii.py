class Solution:

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]
        for i in range(1, rowIndex + 1):
            result = [1] + [result[j - 1] + result[j] for j in range(1, i)] + [1]
        return result


if __name__ == "__main__":
    print(Solution().getRow(3))
