"""

EASY

Given a 0-indexed integer array `nums` of length `n` and an integer `k`,
return the number of pairs (i, j) where 0 <= i < j < n, such that:

1. nums[i] == nums[j]
2. (i * j) is divisible by k

Examples:

Input:
    nums = [3, 1, 2, 2, 2, 1, 3]
    k = 2
Output:
    4

Explanation:
    There are 4 pairs that meet all the requirements:
    - nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
    - nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
    - nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
    - nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.

Input:
    nums = [1, 2, 3, 4]
    k = 1
Output:
    0

Explanation:
    Since no value in nums is repeated, there are no pairs (i, j)
    that meet all the requirements.
"""

class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and ((i * j) % k) == 0:
                    res += 1
        return res

# make sure indices i < j
# make sure that the values at indices i and j are equal to each other
# make sure that indices i * j are divisble by k