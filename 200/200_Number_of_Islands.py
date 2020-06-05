class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.group_id = 1
        self.d = {}
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                # print i,j
                if grid[i][j] == '0':
                    continue
                if self.d.get(self.getid([i, j])) is None:
                    self.group_id += 1
                    self.d[self.getid([i, j])] = self.group_id
                    q = [[i,j]]
                    self.labelAllNeighbors(grid, q)
        return self.group_id-1

    def labelAllNeighbors(self, grid, q):
        while len(q) > 0:
            n = q.pop(0)
            neighbors = self.getNeighbors(grid, n[0], n[1])
            # print neighbors
            for n in neighbors:
                if grid[n[0]][n[1]] == '1' and self.d.get(self.getid(n)) is None:
                    self.d[self.getid(n)] = self.group_id
                    q.append(n)

    def getNeighbors(self, grid, i, j):
        l = []
        if i-1 >= 0:
            l.append([i-1, j])
        if i+1 < len(grid):
            l.append([i+1, j])
        if j-1 >= 0:
            l.append([i, j-1])
        if j+1 < len(grid[0]):
            l.append([i, j+1])
        return l


    def getid(self, n):
        return str(n[0]) + '_' + str(n[1])


def str2ListofList(s):
    return [list(x) for x in s.strip().split('\n')]

s0 = '''
0
'''
# Output: 0

s1 = '''
11110
11010
11000
00000
'''
# Output: 1

s2 = '''
11111
11000
00110
01111
'''
# Output: 2

s3 = '''
11000
11000
00100
00011
'''
# Output: 3


s4 = '''
110011
111010
001001
101110
'''
# Output: 4

s5 = '''
110011
101010
001001
101110
'''
# Output: 5

s58 = '''
10011101100000000000
10011001000101010010
00011110101100001010
00011001000111001001
00000001110000000000
10000101011000000101
00010001010101010101
00010100110101101110
00001001100001000101
00100100000100100010
10010000000100101010
01000101011011101100
11010000100000010001
01001110001111101000
00111000110001010000
10010100001000101011
10100000010001010000
01100011101010111100
01000011001010010011
00000011110100011000
'''

test = Solution()
# print test.numIslands(str2ListofList(s0))
# print test.numIslands(str2ListofList(s1))
# print test.numIslands(str2ListofList(s2))
# print test.numIslands(str2ListofList(s3))
# print test.numIslands(str2ListofList(s4))
# print test.numIslands(str2ListofList(s5))
print test.numIslands(str2ListofList(s58))