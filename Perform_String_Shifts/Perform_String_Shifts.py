class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """

        for sft in shift:
            direction = sft[0]
            amount = sft[1]
            for i in xrange(amount):
                s = self.shift(s, direction)
        return s


    def shift(self, s, direction):
        l = list(s)
        if direction == 0:
            new_l = l[1:]
            new_l.append(l[0])
            return ''.join(new_l)
        elif direction == 1:
            new_l = l[:-1]
            new_l.insert(0, l[-1])
            return ''.join(new_l)
# You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:
#
# direction can be 0 (for left shift) or 1 (for right shift).
# amount is the amount by which string s is to be shifted.
# A left shift by 1 means remove the first character of s and append it to the end.
# Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
# Return the final string after all operations.
test = Solution()
print test.stringShift("abc", [[0,1],[1,2]]) # "cab
print test.stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]]) # "efgabcd"
# Explanation:
# [1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
# [1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
# [0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
# [1,3] means shift to right by 3. "abcdefg" -> "efgabcd"

# Constraints:
#
# 1 <= s.length <= 100
# s only contains lower case English letters.
# 1 <= shift.length <= 100
# shift[i].length == 2
# 0 <= shift[i][0] <= 1
# 0 <= shift[i][1] <= 100