class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        left = 0
        dominoes = list(dominoes)

        for right in range(len(dominoes)):
            if dominoes[right] == 'L' and dominoes[left] != 'R':
                while left != right:
                    dominoes[left] = 'L'
                    left += 1
            elif dominoes[right] == 'R':
                left = right
                for right in range(right + 1, len(dominoes)):
                    if right == len(dominoes) - 1:
                        return "".join(dominoes)
                    elif dominoes[right] == 'R':
                        while left != right:
                            dominoes[left] = 'R'
                            left += 1
                    elif dominoes[right] == 'L':
                        origSpan = (right - left) - 1
                        span = (right - left) - 1
                        # if the span is even
                        if not origSpan & 1:
                            left += 1
                            for left in range(left, right + 1):
                                if span > (origSpan / 2):
                                    dominoes[left] = 'R'
                                    span -= 1
                                else:
                                    dominoes[left] = 'L'
                        # if odd
                        else:
                            startLeft = left
                            for left in range(left, right):
                                if left == (startLeft + 1) + (origSpan // 2):
                                    dominoes[left] = '.'
                                elif span > (origSpan // 2):
                                    dominoes[left] = 'R'
                                    span -= 1
                                else:
                                    dominoes[left] = 'L'
                        left = right + 1
                        right + 1
        return "".join(dominoes)

if __name__ == "__main__":
    solution = Solution()
    strDominoes = "RR.L"  # -> LL.RRRRRL..
    print(solution.pushDominoes(strDominoes))