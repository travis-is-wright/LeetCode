from collections import defaultdict

from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        anagramDict = defaultdict(list)

        for word in strs:
            anagramList = [0] * 26
            for char in word:
                anagramList[ord(char.lower()) - ord('a')] += 1
            anagramDict[tuple(anagramList)].append(word)

        return list(anagramDict.values())


if __name__ == "__main__":
    anagram = Solution()

    strs = ["Good", "pan", "nap", "Dog", "god"]

    print(anagram.groupAnagrams(strs))
