class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.d = {}
        res = self.combinationSum3Recursive(k, n)
        return [r for r in res if len(r) > 0]

    def combinationSum3Recursive(self, k, n):
        if k == 0:
            return [[]]
        if k == 1:
            if n >= 1 and n <= 9:
                return [[n]]
            else:
                return [[]]
        d_res = self.d.get((k, n))
        if d_res is not None:
            return d_res
        l_combi = []
        for i in xrange(1, 10):
            l_combi_k_minus_1 = self.combinationSum3Recursive(k - 1, n - i)
            for combi in l_combi_k_minus_1:
                if len(combi) == 0:
                    continue
                if i in combi:
                    continue
                combi = [i] + combi
                combi = sorted(combi)
                if combi not in l_combi:
                    l_combi.append(combi)
        self.d[(k, n)] = l_combi
        return l_combi

test = Solution()
print test.combinationSum3(3, 7) # [[1,2,4]]
print test.combinationSum3(3, 9) # [[1,2,6], [1,3,5], [2,3,4]]
print test.combinationSum3(2, 18) # []
print test.combinationSum3(3, 15) # [[1,5,9],[1,6,8],[2,4,9],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6]]
print test.combinationSum3(9, 45) # [[1, 2, 3, 4, 5, 6, 7, 8, 9]]


