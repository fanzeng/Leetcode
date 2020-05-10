class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        source = set([t[0] for t in trust])
        d = {}
        for t in trust:
            if d.get(t[0]) is None:
                d[t[0]] = [t[1]]
            else:
                d[t[0]].append(t[1])
        for i in xrange(1, N+1):
            if i not in source:
                all_trust = True
                for j in xrange(1, N+1):
                    if j == i:
                        if d.get(j) is not None and i in d[j]:
                            all_trust = False
                    else:
                        if d.get(j) is None or i not in d[j]:
                            all_trust = False
                if all_trust:
                    return i
        return -1

test = Solution()
print test.findJudge(2, [[1,2]]) # 2
print test.findJudge(3, [[1,3],[2,3]]) # 3
print test.findJudge(3, [[1,3],[2,3],[3,1]]) # -1
print test.findJudge(3, [[1,2],[2,3]]) # -1
print test.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]) # 3

