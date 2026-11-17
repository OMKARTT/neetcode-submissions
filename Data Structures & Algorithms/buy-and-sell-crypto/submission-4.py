class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        for i in range(0,len(prices)):
            cp = prices[i]
            for j in range(i+1,len(prices)):
                if prices[j] > cp and maxProf < prices[j] - cp:
                    maxProf = prices[j] - cp
                    # print(j)
        return maxProf
        