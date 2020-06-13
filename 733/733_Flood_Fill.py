class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        init_color = image[sr][sc]
        q = [(sr, sc)]
        d = {}
        w = len(image[0])
        while len(q) > 0:
            p = q.pop(0)
            self.fillColor(image, p, newColor)
            d[p[0]*w + p[1]] = 1
            nb = self.getNeighbors(image, p)
            for n in nb:
                if image[n[0]][n[1]] == init_color and d.get(n[0]*w + n[1]) is None:
                    q.append(n)
        return image


    def fillColor(self, image, p, newColor):
        image[p[0]][p[1]] = newColor

    def getNeighbors(self, image, p):
        h = len(image)
        w = len(image[0])
        nb = []
        r = p[0]
        c = p[1]
        if r-1 >= 0:
            nb.append([r-1, c])
        if r+1 < h:
            nb.append([r+1, c])
        if c-1 >= 0:
            nb.append([r, c-1])
        if c+1 < w:
            nb.append([r, c+1])
        return nb


image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]
test = Solution()
print test.floodFill(image, 1, 1, 2)
'''
[
    [2,2,2],
    [2,2,0],
    [2,0,1]
]
'''