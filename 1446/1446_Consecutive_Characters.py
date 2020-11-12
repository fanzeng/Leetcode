class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        last_char = s[0]
        max_count = 1
        count = 1
        for char in s[1:]:
            if char == last_char:
                count += 1
                if max_count < count:
                    max_count = count
            else:
                last_char = char
                count = 1
        return max_count

test = Solution()
print test.maxPower("leetcode") # 2
print test.maxPower("abbcccddddeeeeedcba") # 5
print test.maxPower("triplepillooooow") # 5
print test.maxPower("hooraaaaaaaaaaay") # 11
print test.maxPower("tourist") # 1
print test.maxPower("cc") # 2