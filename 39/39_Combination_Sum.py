class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.l_res = []
        self.combinationSumDP(sorted(candidates), target, [])
        return self.l_res

    def combinationSumDP(self, candidates, target, res_part):
        if len(res_part) > 0:
            candidates = [cand for cand in candidates if cand >= res_part[-1]]
        for cand in candidates:
            res = res_part + [cand]
            if cand == target:
                self.l_res.append(res)
            elif target-cand > 0:
                self.combinationSumDP(candidates, target - cand, res)

test = Solution()
print test.combinationSum([2,3,6,7], 7) # [[2,2,3],[7]]
print test.combinationSum([2,3,5], 8) # [[2,2,2,2],[2,3,3],[3,5]]
print test.combinationSum([2], 1) # []
print test.combinationSum([1], 1) # [[1]]