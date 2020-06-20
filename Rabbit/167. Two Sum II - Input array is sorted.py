# JK Implementation
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1
        
        while i < j:

            tmp = numbers[i] + numbers[j]

            if tmp == target:
                return i + 1, j + 1
            elif tmp < target:
                i += 1
            else:
                j -= 1

"""
- 解答一樣
- 常用技巧: "while i < j: " = when the 2 pointers collapse

"""