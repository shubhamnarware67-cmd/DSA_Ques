"""
Q250: Best Time to Buy and Sell Stock with Transaction Fee (DP/Greedy)
=======================================================================
Problem: Maximize profit with unlimited transactions but a fee per transaction.

Example:
    prices=[1,3,2,8,4,9], fee=2 -> 8
    (buy@1,sell@3:profit=0, buy@2,sell@8:profit=4, buy@4,sell@9:profit=3 = 0+4+4=8? No: 
     buy@1,sell@8:6-2=6, buy@4,sell@9:5-2=3 -> 6+3=no... 
     optimal: buy@1,sell@8(fee=2)->6, buy@4,sell@9(fee=2)->3, total=8-wait
     buy@1,sell@3->0; actually [1,3,2,8,4,9] fee=2: buy1 sell8=5, buy4 sell9=3 = 8)
"""

def max_profit_fee(prices, fee):
    hold = -prices[0]  # Cost of holding stock
    cash = 0           # Profit when not holding
    for price in prices[1:]:
        hold = max(hold, cash - price)
        cash = max(cash, hold + price - fee)
    return cash

if __name__ == "__main__":
    print(max_profit_fee([1,3,2,8,4,9], 2))   # 8
    print(max_profit_fee([1,3,7,5,10,3], 3))  # 6
