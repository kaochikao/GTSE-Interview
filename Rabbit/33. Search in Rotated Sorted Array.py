class Solution:
    def search(self, nums, target):
        return self.get(nums, target, 0, len(nums) - 1)


    # binary search
    # if start < mid, then left part is sorted
    # if mid < end, then right part is sorted
    def get(self, nums, target, start, end):

        if start > end:
            return -1

        mid = (start + end) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] >= nums[start]: # First half is sorted
            # 由於確定左邊是正確sorted, 可以正常看<>區間，一般binary search作法
            if target >= nums[start] and target < nums[mid]:
                return self.get(nums, target, start, mid - 1)
            
            # 這裡就無法用區間判斷，所以整個用else抓住
            # 這裡也會有 "target比現在start還小的情況" 的情況
            else:
                return self.get(nums, target, mid + 1, end)

        elif nums[mid] <= nums[end]: # Second half is sorted
            if target > nums[mid] and target <= nums[end]:
                return self.get(nums, target, mid + 1, end)
            else:
                return self.get(nums, target, start, mid - 1)


"""
自解，非常醜，但也pass
- 原本pivot初始值設為float('-inf)，但沒考慮到edge case(no pivot), 所以error
"""
class Solution:
    def search(self, nums, target) -> int:

        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        # find pivot point first
        pivot = len(nums)
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                pivot = i + 1

        l = nums[:pivot]
        r = nums[pivot:]
        is_left = True

        if target >= nums[0]:
            a = l
        else:
            a = r
            is_left = not is_left

        # binary search
        start = 0
        end = len(a)
        print(a)

        while start < end:

            mid = (start + end) // 2

            if a[mid] == target:
                if is_left:
                    return mid
                else:
                    return mid + len(l)
            elif a[mid] > target:
                end = mid
            else:
                start = mid + 1

        return -1