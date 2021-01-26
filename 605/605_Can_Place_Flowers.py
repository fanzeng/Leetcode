class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        return self.canPlaceFlowersRecursive(flowerbed, n)

    def canPlaceFlowersRecursive(self, flowerbed, n):
        if n == 0:
            return True
        if len(flowerbed) == 0:
            return False
        if len(flowerbed) == 1:
            return flowerbed[0] == 0
        i = 0
        while i < len(flowerbed):
            if self.canPlace(flowerbed, i):
                flowerbed_new = flowerbed[i:]
                flowerbed_new[0] = 1
                # print flowerbed_new
                return self.canPlaceFlowersRecursive(flowerbed_new, n-1)
            i += 1
        return False

    # this function assumes len(flowerbed) >= 2
    def canPlace(self, flowerbed, i):
        if i < 0 or i >= len(flowerbed):
            return False
        if flowerbed[i] == 1:
            return False
        if i == 0:
            return flowerbed[1] == 0
        elif i == len(flowerbed)-1:
            return flowerbed[i-1] == 0
        else:
            return flowerbed[i-1] == 0 and flowerbed[i+1] == 0

test = Solution()
print test.canPlaceFlowers([1,0,0,0,1], 1) # True
print test.canPlaceFlowers([1,0,0,0,1], 2) # False
print test.canPlaceFlowers([1,0,0,0,0,0,1], 2) # True
print test.canPlaceFlowers([1], 1) # False

