class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)
        for i, num in enumerate(nums):
            ans[i] = nums[nums[i]]
        return ans



nums = [5,0,1,2,3,4]
solution = Solution()
print(solution.buildArray(nums))
