class StockSpanner:
    def __init__(self):
        self.stack = []    
    def next(self, price: int) -> int:
        stack = self.stack
        k = 1
        while stack and price>=stack[-1][0]:
            k += stack.pop()[1]
        stack.append((price,k))
        return k
    
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)