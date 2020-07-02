class NumArray(object):
    def __init__(self, nums):
        """
        algo:
            - 累加一個list

        實現：
            - 這裡是先宣告一個"array", 用於lookup
        """
        self.res = [0] * (len(nums) + 1)
        self.data = list(nums)
        for i in range(len(self.data)):
            self.res[i + 1] = self.res[i] + nums[i]

    def sumRange(self, i, j):
        """
        algo:
            - key: 直接扣掉 end為i時的總和, interesting.
        """
        return self.res[j + 1] - self.res[i]
