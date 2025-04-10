"""
1. TWO SUM

Given an array of integers 'nums' and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

The answer can be return in any order.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dictionary = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in num_dictionary:
                return [num_dictionary[diff], i]
            num_dictionary[n] = i

def main():
    solution = Solution()

    nums = [2,3,11,3,22]
    target = 6
    result = solution.twoSum(nums, target)
    print(f"Test Case 1 - Expected: [0, 1], Got: {result}")

if __name__ == "__main__":
    main()