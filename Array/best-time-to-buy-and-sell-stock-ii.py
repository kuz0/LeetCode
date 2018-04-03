class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 贪心算法
        max_p, i = 0, 1
        while i < len(prices):
            max_p += max(0, prices[i] - prices[i - 1])
            i += 1
        return max_p

    def maxProfit1(self, prices):
        return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))
