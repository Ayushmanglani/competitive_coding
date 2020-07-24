class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length<2:
            return 0
        
        profit = 0
        currentBuy = -1
        
        for i in range(length):
            current = prices[i]
            
            #Buy
            if currentBuy == -1 and i+1<length:
                nextVal = prices[i+1]
                if nextVal > current: #next greater is present
                    currentBuy = current
                    continue
                    
            #sell
            if currentBuy >= 0:
                if i == length - 1:
                    profit += (current - currentBuy)
                    break
                    
                nextVal = prices[i+1]
                if nextVal < current: #nextval is smaller, if next is greater sell at that
                    profit += (current-currentBuy)
                    currentBuy = -1
        return profit
                
            