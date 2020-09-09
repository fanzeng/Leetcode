class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        self.res = []
        total = len(A)
        for i in xrange(total):
            flip_loc = self.getFlipLoc(A, len(A))
            if flip_loc == total - i:
                continue
            if flip_loc != 0:
                self.res.append(flip_loc)
            A = self.pancakeFlip(A, flip_loc)
            flip_loc = len(A)-1
            self.res.append(flip_loc)
            A = self.pancakeFlip(A, flip_loc)
            # print i, A
            A = A[:-1]
        # return self.res
        return [res+1 for res in self.res] # need to add 1 because the flip location k defined by the example is 1 larger than the index (flip_loc) here


    def getFlipLoc(self, A, num):
        for i, n in enumerate(A):
            if A[i] == num:
                return i

    def pancakeFlip(self, A, loc):
        return A[:loc+1][::-1] + A[loc+1:]

    def testPancakeSort(self, A, flip_locs):
        for flip_loc in flip_locs:
            A = self.pancakeFlip(A, flip_loc)
            # print 'flip_loc =', flip_loc, 'A =', A
        return A

test = Solution()
print test.pancakeSort([3,2,4,1]) # [4,2,4,3]
print test.testPancakeSort([3,2,4,1], test.pancakeSort([3,2,4,1]))
print test.pancakeSort([1,2,3]) # []
print test.testPancakeSort([1,2,3], test.pancakeSort([1,2,3]))
print test.pancakeSort([4,3,1,2])
print test.testPancakeSort([4,3,1,2], test.pancakeSort([4,3,1,2])) # []
