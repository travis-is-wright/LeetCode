class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0

        for num in nums:
            cnt = 0
            num = str(num)
            for val in num:
                cnt += 1
            if cnt != 1:
                res += 1

        return res


if __name__ == "__main__":
    solution = Solution()
    nums = [12,345,2,6,7896]
    print(solution.findNumbers(nums))