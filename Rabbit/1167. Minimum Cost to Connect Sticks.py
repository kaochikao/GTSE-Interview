
# first attempt, 半對，超時
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        sticks.sort()
        return self.rec(sticks, 0)
        

    def rec(self, sticks, cost):
        
        if len(sticks) == 1:
            return cost
        
        # sticks.sort()
        curr_cost = sticks[0] + sticks[1]
        cost += curr_cost
        sticks = sticks[2:]
        
        # insert (to prevent sorting each time)
        prev = 0
        pos = 0
        while pos < len(sticks):
            if curr_cost > prev and curr_cost <= sticks[pos]:
                break
            else:
                prev = sticks[pos]
                pos += 1
                
        sticks = sticks[:pos] + [curr_cost] + sticks[pos:]        
        

        
        return self.rec(sticks, cost)