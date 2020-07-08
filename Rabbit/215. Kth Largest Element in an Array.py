
"""
algo思路：
- 目標是要找到一個partition完後的"partition point"是等於k的 (也就是原pivot會確定是第幾大)
- 這無法只透過一次partition就知道，因為pivot是用end, 無法確定partition完，會有多少smaller/ larger = 無法確定pivot位置
- rec只需挑左或右，不用兩邊都做
"""


class Solution(object):


    def findKthLargest(self, nums, k):
        # shuffle nums to avoid n*n
        random.shuffle(nums)

        # 這邊把k變成"len(nums) - k", 也就是第k小，而非第k大
        return self.quickSelection(nums, 0, len(nums) - 1, len(nums) - k)

    def quickSelection(self, nums, start, end, k):
        if start > end:
            return float('inf')

        pivot = nums[end]
        left = start

        for i in range(start, end):
            if nums[i] <= pivot:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        nums[left], nums[end] = nums[end], nums[left]

        # nums[left]此時是原pivot. 此時這個left是第幾大是可以確定的
        if left == k:
            return nums[left]
        elif left < k:
            return self.quickSelection(nums, left + 1, end, k)
        else:
            return self.quickSelection(nums, start, left - 1, k)