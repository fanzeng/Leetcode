class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        res = []
        pow = len(str(high))
        seqs = self.gen_sequential(pow)
        return [n for n in seqs if n >= low and n <= high]

    def gen_sequential(self, n):
        if n == 2:
            return [12, 23, 34, 45, 56, 67, 78, 89]
        prev = self.gen_sequential(n - 1)
        return sorted(list(set(prev + [self.append(p) for p in prev if p % 10 < 9])))
        
    def append(self, p):
        last = p % 10
        if last < 9:
            return p*10 + last + 1

test = Solution()
print test.sequentialDigits(100, 300) # [123,234]
print test.sequentialDigits(1000, 13000) # [1234,2345,3456,4567,5678,6789,12345]
