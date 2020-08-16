class Solution:
    def searchInsert(self, nums, target):
        
        l = 0
        r = len(nums)
        
        
        while l < r:
            
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m
            else:
                l = m + 1
                
        return m