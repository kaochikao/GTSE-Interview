


"""
自解brute force.
"""
class Solution:
    def rob(self, nums):
        return self.helper(nums, False, 0, 0)

    def helper(self, nums, prev_selected, curr_p, curr_total):

        if curr_p == len(nums):
            return curr_total

        if prev_selected:
            return self.helper(nums, False, curr_p + 1, curr_total)
        else:
            select = self.helper(nums, False, curr_p + 1, curr_total)
            not_select = self.helper(nums, True, curr_p + 1, curr_total + nums[curr_p])
            return max(select, not_select)


# [1,2,3,1]
class Solution:
	def rob(self, nums):
		if len(nums) == 0:
			return 0

		dp = [0] * (len(nums) + 1)
		dp[0] = 0
		dp[1] = nums[1]

		for i in range(1, len(nums)):
			dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])
		
		return dp[-1]