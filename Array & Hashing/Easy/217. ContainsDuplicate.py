""""
217. Contains Duplicate

Given an integer array 'nums', return true if any value appears at least twice in teh array,
and return false if every element is distinct.
"""

class Solution():
    def containsDuplicate(self, nums):
        unique_vals = set()

        for i in nums:
            if i in unique_vals:
                return True
            else:
                unique_vals.add(i)
        return False

if __name__ == "__main__":
    solution = Solution()

    nums = [1,4,5,6,6,7]
    print(solution.containsDuplicate(nums))