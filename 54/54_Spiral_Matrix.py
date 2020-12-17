class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        l_direc = [(0,1), (1,0), (0,-1), (-1,0)]
        id_direct = 0
        direct = l_direc[id_direct%4]
        loc = [0, 0]
        count = 0
        w = len(matrix[0])
        h = len(matrix)
        visited = [[0 for i in xrange(w)] for j in xrange(h)]
        total = w*h
        res = []
        while count < total:
            res.append(matrix[loc[0]][loc[1]])
            visited[loc[0]][loc[1]] = 1
            if loc[0] + direct[0] < 0 or loc[1] + direct[1] < 0 or loc[0] + direct[0] == h or loc[1] + direct[1] == w or visited[loc[0]+direct[0]][loc[1]+direct[1]] == 1:
                id_direct += 1
                direct = l_direc[id_direct % 4]
            loc[0] += direct[0]
            loc[1] += direct[1]
            count += 1
        return res

test = Solution()
print test.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) # [1,2,3,6,9,8,7,4,5]
print test.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) # [1,2,3,4,8,12,11,10,9,5,6,7]