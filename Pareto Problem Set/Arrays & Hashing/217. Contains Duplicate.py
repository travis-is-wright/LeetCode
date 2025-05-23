class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seenSet = set()

        for num in nums:
            if num in seenSet:
                return True
            else:
                seenSet.add(num)
        return False

if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,4,5,6,7]
    nums2 = [1,2,2,4,4,6,6]
    print(solution.containsDuplicate(nums))
    print(solution.containsDuplicate(nums2))

