class Substring:
    def has_substring(self, word, string):
        l = 0

        if len(word) > len(string):
            return False

        for i in range(len(string)):
            if word[l] == string[i]:
                l += 1
            elif word[l] != string[i]:
                l = 0
            if l == len(word):
                return True
        return False
z
if __name__ == "__main__":

    substring = Substring()
    a = "car"
    b = "racecar"
    c = "car"

    print(substring.has_substring(a, b))