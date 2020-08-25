class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        _1day_pass, _7day_pass, _30day_pass = 0, 1, 2
        # Predefined constant to represent not-traverling day
        NOT_Traveling_Day = -1
        maxdays = days[-1]
        # DP Table, record for minimum cost of ticket to travel
        dp_cost = [NOT_Traveling_Day for _ in range(maxdays+1)]
        # base case:
        # no cost before travel
        dp_cost[0] = 0
        for day in days:
            # initialized to 0 for traverling days
            dp_cost[day] = 0
        # Solve min cost by Dynamic Programming
        for day_i in range(1, maxdays+1):
            if dp_cost[day_i] == NOT_Traveling_Day:
                # today is not traveling day
                # no extra cost
                dp_cost[day_i] = dp_cost[day_i - 1]
            else:
                # today is traveling day
                # compute optimal cost by DP
                dp_cost[day_i] = min(   dp_cost[ day_i - 1 ]  + costs[ _1day_pass ],
                                        dp_cost[ max(day_i - 7, 0) ]  + costs[ _7day_pass ],
                                        dp_cost[ max(day_i - 30, 0) ] + costs[ _30day_pass ]     )
        # Cost on last day of this year is the answer
        return dp_cost[maxdays]