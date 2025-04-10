class Solution(object):
    def isPalindrome(self, s):
        #     """
        #     :type s: str
        #     :rtype: bool
        #     """
        s_new = ""

        for char in s:
            if char.isalnum():
                s_new += char.lower()

        left = 0
        right = len(s_new) - 1

        while left < right:
            if s_new[left] != s_new[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

        #
    #     s_alnum = []

    #     for i in s:
    #         if i.isalnum():
    #             s_alnum.append(i.lower())

    #     return s_alnum == s_alnum[::-1]

    #     # t = ""
    #     # s_lower = s.lower()
    #     # s_replace = s_lower.replace(" ", "")

    #     # for i in range(len(s_replace)):
    #     #    if s_replace[-(i + 1)].isalnum():
    #     #         t += s_replace[-(i + 1)]

    #     # for i in range(len(s_replace)):
    #     #     if s_replace[i].isalnum():
    #     #         i -= 1
    #     #         if s_replace[i] != t[i]:
    #     #             return
    #     # return True


if __name__ == "__main__":
    solution = Solution()
    s = "AmanaplanacanalPanama"
    print(solution.isPalindrome(s))