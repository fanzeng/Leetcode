class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for str in strs:
            l = list(str)
            l.sort()
            key = ''.join(l)
            if d.get(key) is None:
                d[key] = [str]
            else:
                d.get(key).append(str)
        return d.values()
test = Solution()
print test.groupAnagrams([])
print test.groupAnagrams(["eat"])
print test.groupAnagrams(["tee", "eet", "ete", "ata"])
print test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]