class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # if version1 < version2:
        #     return -1
        # elif version1 > version2:
        #     return 1
        # return 0
        l_version1 = [int(v) for v in version1.split(".")]
        l_version2 = [int(v) for v in version2.split(".")]
        return self.compareRecursive(l_version1, l_version2)


    def compareRecursive(self, l_version1, l_version2):
        if len(l_version1) == 0 and len(l_version2) == 0:
            return 0
        if len(l_version1) == 0:
            if sum(l_version2) == 0:
                return 0
            else:
                return -1
        if len(l_version2) == 0:
            if sum(l_version1) == 0:
                return 0
            else:
                return 1
        if l_version1[0] > l_version2[0]:
            return 1
        if l_version1[0] < l_version2[0]:
            return -1
        return self.compareRecursive(l_version1[1:], l_version2[1:])

test = Solution()
print test.compareVersion("0.1", "1.1") # -1
print test.compareVersion("1.0.1", "1") # 1
print test.compareVersion("7.5.2.4", "7.5.3") # -1
print test.compareVersion("1.01", "1.001") # 0
print test.compareVersion("1.0", "1") # 0