class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0
        elif len(prices) > 1:
            max_money = 0
            for price_idx in range(1, len(prices)):
                if prices[price_idx] > prices[price_idx - 1]:
                    max_money = max_money + prices[price_idx] - prices[price_idx - 1]
            return max_money
        else:
            return 0


if __name__ == '__main__':
    m = Solution()
    print(m.maxProfit( [7,6,4,3,1]))