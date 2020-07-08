
"""
自解，用多餘空間，沒有cyclic sort技巧
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # 這裡一開始寫錯，因為nums本身就缺一個element, len會少1
        # d = [0] * (len(nums) - 1)
        # d = [0] * len(nums)
        d = [0] * (len(nums) + 1)
        
        for i in range(len(nums)):
            d[nums[i]] = 1
            
            
        for i in range(len(d)):
            if d[i] == 0:
                return i

  



class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # cyclic sort
        i = 0
        while i < len(nums):
            j = nums[i]

            if j < len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        # sort 完之後，missing value的位置會是len(nums), 因為這個val其實沒有他自己的位子(nums短一格)，如果swap會index out of range
        for i in range(len(nums)):
            if nums[i] != i:
            # if nums[i] == len(nums): # 這樣也可以
                return i

        return len(nums)



# Cyclic Sort 練習

"""
swap 完之後，nums[curr]會是正確的值，但自己不一定拿到正確的，繼續swap, pointer不走

Cyclic Sort教學
https://blog.techbridge.cc/2020/02/16/leetcode-%E5%88%B7%E9%A1%8C-pattern-cyclic-sort/
"""
def cyclic_sort(nums):

    i = 0

    while i < len(nums):
        curr_val = nums[i]

        # array中不一定沒有duplicate
        if curr_val < len(nums) and nums[i] != nums[curr_val]:
            # 關鍵在這，pointer不動，會持續去swap
            nums[i], nums[curr_val] = nums[curr_val], nums[i]

        else:
            i += 1
