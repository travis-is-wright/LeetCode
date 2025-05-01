from collections import defaultdict, Counter

class Substring2:
    def detect(self, chars, phrase):
        countPhraseOrig = Counter(phrase)
        res = []

        if not phrase:
            return 0 

        for word in chars:
            countPhrase = countPhraseOrig.copy()
            for char in word:
                if countPhrase[char] > 0:
                    countPhrase[char] -= 1
                else:
                    break
            else:
                res.append(word)
        return res



if __name__ == "__main__":
    substring = Substring2()

    chars_list = ["ja", "ahjpjau", "ahbwzgqnuk", "tnmlanowax"]
    phrase_string = ""
    print(substring.detect(chars_list, phrase_string))