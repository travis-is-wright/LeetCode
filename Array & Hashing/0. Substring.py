"""
desc:

- return True if word is found in given string
- string will only contain alphabet chars
- make the function case-sensitive
"""

def containsWord(word, string):
    j = 0

    if len(word) == 0:
        return False
    else:
        for char in string:
            if j == len(word) - 1:
                return True
            elif char.lower() != word[j].lower():
                j = 0
            else:
                j += 1
        return False

word = "cat"
string = "dog"

print(containsWord(word, string))