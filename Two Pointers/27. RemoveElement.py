class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0  # Tracks the position to place elements not equal to `val`

        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1

        return left  # `left` is the count of elements not equal to `val`

if __name__ == "__main__":
    solution = Solution()

    nums = [3, 2, 2, 3]
    val = 3

    print(f" {solution.removeElement(nums, val)}")
    print(f" {nums}")