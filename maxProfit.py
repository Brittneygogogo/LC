# def maxProfit(prices):
#     """
#     :type prices: List[int]
#     :rtype: int
#     """
    # p_min = 0
    # p_max = len(prices) - 1
    # s = 0
    # for i in range(len(prices)):
    #     if prices[i] < prices[p_min]:
    #         p_min = i
    #     if prices[p_max - i] > prices[p_max]:
    #         p_max = p_max - i
    #     if  prices[p_max] - prices[p_min] > s:
    #         s = prices[p_max] - prices[p_min]
    #     if i == p_max:
    #         return s
    #return 0


# maxprofit录的总是最大解，不论min如何变化，因为maxprofit是根据当前的min值和它之后的max值的差得出的。maxprofit取得值也是一直取最大的
def maxProfit(prices):
    inf = int(1e9)
    minprice = inf
    maxprofit = 0
    for price in prices:
        maxprofit = max(price - minprice, maxprofit)
        minprice = min(price, minprice)
    return maxprofit



# print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([2,5,1,3]))
# print(maxProfit([7,6,5,4,3,2,1]))
# print(maxProfit([2,1]))
# print(maxProfit([1,4,2]))