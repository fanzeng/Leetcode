class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        for c in s:
            if d.get(c) is None:
                d[c] = 1
            else:
                d[c] += 1
        res = ''
        for item in sorted(d.items(), reverse=True, key=lambda x: x[1]):
            res += item[0]*item[1]
        return res


test = Solution()
print test.frequencySort("tree")
print test.frequencySort("cccaaa")
print test.frequencySort("Aabb")