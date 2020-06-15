class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        sorted_people = sorted(people, key=lambda x:(x[0], -x[1]))
        res = [[] for p in people]
        for p in sorted_people:
            i = 0
            l = p[1]
            while l > 0:
                if len(res[i]) > 0:
                    l += 1
                i += 1
                l -= 1
            while len(res[i]) > 0:
                i += 1
            res[i] = p
        return res

test = Solution()
print test.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]) # [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
print test.reconstructQueue([[2,4],[3,4],[9,0],[0,6],[7,1],[6,0],[7,3],[2,5],[1,1],[8,0]]) # [[6,0],[1,1],[8,0],[7,1],[9,0],[2,4],[0,6],[2,5],[3,4],[7,3]]