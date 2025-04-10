"""
constraints:

- integers / floats
- negative values
- no need for strings, etc.
- exactly two numbers
- return 0 if the list is empty
"""

class Sum:
    def __init__(self):
        self.nums = []

    def setnums(self, nums):
        self.nums = nums

    def sumList(self):
        res = 0

        if len(self.nums) == 0:
            return 0
        else:
            for num in self.nums:
                res += num
        return res

if __name__ == "__main__":
    sum = Sum()
    sum.setnums([1, 2, 3, 8, 10, -2.2])
    print(sum.sumList())