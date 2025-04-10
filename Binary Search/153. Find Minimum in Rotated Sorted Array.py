class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        if nums[left] < nums[right] or len(nums) == 1:
            return nums[left]
        else:
            while left <= right:
                mid = (left + right) // 2
                res = min(nums[left], nums[mid])
                if nums[mid] < nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            return res


if __name__ == "__main__":
    solution = Solution()

    nums = [3, 1, 2]
    print(solution.findMin(nums))

