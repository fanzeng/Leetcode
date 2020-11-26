class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        if K % 2 == 0:
            return -1
        remainder = 1
        count = 1
        visited = set()
        while remainder % K != 0:
            if remainder % K in visited:
                return -1
            visited.add(remainder % K)
            remainder = remainder*10 + 1
            count += 1
        return count

test = Solution()
print test.smallestRepunitDivByK(1) # 1
print test.smallestRepunitDivByK(2) # -1
print test.smallestRepunitDivByK(3) # 3
print test.smallestRepunitDivByK(49993) # 49992