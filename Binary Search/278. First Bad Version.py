# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    # Simulated function to represent the bad versions
    @staticmethod
    def isBadVersion(version):
        # Assume the first bad version is 4
        bad = 2
        return version >= bad

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        res = n

        if n == 1:
            return 1
        else:
            while left <= right:
                mid = (left + right) // 2
                if self.isBadVersion(mid):
                    right = mid - 1
                else:
                    left = mid + 1
            return left

if __name__ == "__main__":

    solution = Solution()

    n = 5
    print(solution.firstBadVersion(n))

