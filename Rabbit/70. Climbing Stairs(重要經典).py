
# 自解，iteration
class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 0 or n == 1:
            return n
        
        dmap = [0] * (n + 1)
        dmap[1] = 1
        dmap[2] = 2
        
        for i in range(3, n + 1):
            dmap[i] = dmap[i - 1] + dmap[i - 2]
            
        return dmap[n]

# 第一次DP題解那麼順，iter & rec都直接寫出來
class Solution:
    def climbStairs(self, n: int) -> int:

        def helper(n, dmap):
            
            if n in dmap:
                return dmap[n]
            
            dmap[n] = helper(n-1, dmap) + helper(n-2, dmap)
            return dmap[n]
            

        dmap = {}
        dmap[1] = 1
        dmap[2] = 2
        return helper(n, dmap)

# 排列組合法
class Solution(object):
    #if there are 13 stairs
    #the max two steps are 6, so there can be 
    #6 two step, 1 one step -> case1
    #5 two step, 3 one step -> case2
    # ...
    #0 two step, 13 one step -> case7
    
    #each case may have more than one way to arrange
    #take case2 as example, 22222111. how many combination can it be?
    #you can think this as, there are 8 seats you have to choose 3 seats for number 1 to sit on it.
    
    #we call this combination m choose n, thus
    #case1 is combination 7 choose 1
    #case2 is combination 8 choose 3
    # ...
    #case7 is combination 13 choose 13
    #the calculation of combination is m!/(n!*(m-n)!)
    #https://en.wikipedia.org/wiki/Combination
    
    #Efficaiency is O(N), N is the stairs count.
    #Space is O(1)
    
    def climbStairs(self, n):
        counter = 0
        max_two_step = n/2
        for two_step in range(max_two_step+1):
            one_step = n-two_step*2
            combination = self.combination(two_step+one_step, one_step)
            counter+=combination
        return counter
            
            
    #combination m choose n
    def combination(self, m, n):
        def factorial(int_num):
            if int_num<0: return None
            if int_num==0: return 1
            counter = 1
            while int_num>=1:
                counter*=int_num
                int_num-=1
            return counter
        
        return factorial(m)/(factorial(n)*factorial(m-n))