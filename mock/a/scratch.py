# given a binary matrix, count all the islands; island >= size 1 (area)
# cell where sides (not diagonals) touching
# sometimes referred to as the 'connected components' problem in vision

# this example has 4 islands
matrix = [
	[0, 0, 1, 1, 0, 1],
	[1, 0, 1, 0, 0, 0],
	[1, 0, 1, 0, 0, 0],
	[0, 1, 0, 0, 0, 0]
]


# four islands itemized below
# {(1,0),(2,0)} , {(3,1)} , {(0,2),(0,3),(1,2),(2,2)} , {(0,5)}

class Point(object):
	def __init__(self, i, j, val):
		self.i = i
		self.j = j
		self.val = val
		self.group_id = -1  # unassigned group_id is -1

	def __str__(self):
		return '(' + str(self.i) + ',' + str(self.j) + ')'

	# return a list of tuples of neighbor positions
	def getNeighbors(self, mat_size):
		i = self.i
		j = self.j
		# print 'i, j, mat_size = ', i, j, mat_size
		list_n = []
		if i - 1 >= 0:
			list_n.append((i - 1, j))
		if i + 1 < mat_size[0]-1:
			list_n.append((i + 1, j))
		if j - 1 >= 0:
			list_n.append((i, j - 1))
		if j + 1 < mat_size[1]-1:
			list_n.append((i, j + 1))
		# print 'list_n = ', list_n
		return list_n


class UnionFind(object):
	def __init__(self, matrix):
		self.islands = {}  # dict of group_id => list of points, this stores the solution
		self.count = 0  # increment to label group_id for points
		self.matrix = matrix  # input matrix
		self.mat_size = self.getMatSize(matrix)  # size of input matrix, assume > 0
		self.initPoints()  # 2d array of processed/unprocess points
		print 'mat_size = ', self.mat_size
	# init self.points to correspond to input matrix, but no group_id assigned (all -1)
	def initPoints(self):
		self.points = []
		for i in range(self.mat_size[0]):
			self.points.append([])
			for j in range(self.mat_size[1]):
				self.points[i].append(Point(i, j, self.matrix[i][j]))

	def getPoint(self, i, j):
		if i < 0 or i >= self.mat_size[0]:
			print 'i = ', i , 'is out of range'
		if j < 0 or j >= self.mat_size[1]:
			print 'j = ', j , 'is out of range'
		else:
			return self.points[i][j]

	def getMatSize(self, matrix):
		return (len(matrix), len(matrix[0]))

	def union(self, p, q):  # p and q order matters, p is the one being processed
		# print 'union p, q: ', p, q, 'group_ids = ', p.group_id, q.group_id
		if p.group_id == -1:  # p is unassigned
			p.group_id = q.group_id
			# print 'assigned to p: ', q.group_id
		elif q.group_id == -1:
			# print 'assigning to q', p.group_id
			q.group_id = p.group_id
			self.points[q.i][q.j] = q
			# This elif block could be unnecessary
		elif p.group_id != q.group_id:  # p has been assigned, this means we need to merge p and q's groups
		    # Big TODO: implement weighted quickUnion by selecting whether to merge p into q or vice versa
			q_island = self.islands.get(q.group_id)
			# remove q.group_id because now it's captured by p's group_id
			self.islands[q.group_id] = None
			for point in q_island:
				# change group_id of every member in q'group to be the same as p
				point.group_id = p.group_id
				# add each of them to p's group
				self.islands.get(p.group_id).append(point)
				self.points[point.i][point.j] = point  # update the self.point matrix
		self.islands[p.group_id].append(p)

	def createNewIsland(self, point):
		self.count += 1
		point.group_id = self.count
		self.islands[self.count] = [point]
		self.points[point.i][point.j] = point

	def getIslands(self):
		for i in range(self.mat_size[0]):
			for j in range(self.mat_size[1]):
				p = Point(i, j, self.matrix[i][j])
				# print 'p = ', p
				if p.val == 0:  # ignore zero elements
					continue
				all_neighbor_pos = p.getNeighbors(self.mat_size)
				for neighbor_pos in all_neighbor_pos:  # deal with each of p's neighbor
					n = self.getPoint(neighbor_pos[0], neighbor_pos[1])
					# only do valid and processed neighbors
					# because unprocessed ones will be processed later
					if n.val == 1 and n.group_id > 0:
						self.union(p, n)
					else:
						pass
						# print 'skipping: n = ', n, 'val = ', n.val, 'group_id = ', n.group_id
				# if after for loop, p still unassigned, this means p is a new island
				if p.group_id < 0:
					self.createNewIsland(p)
				self.points[i][j] = p

	###########################
	# Functions below are for printing
	###########################
	def printIslands(self):
		allIslands = self.getAllIslands()
		str_ = '{'
		if len(allIslands) <= 0:
			print str_ + '}'
			return
		for island in allIslands[:-1]:
			str_ += self.islandToStr(island) + ', '
		print str_ + self.islandToStr(allIslands[-1]) + '}'

	def islandToStr(self, island):
		str_ = '{'
		if island is None:
			return None
		if len(island) <= 0:
			return str_ + '}'
		set_island = set(island) # convert to set to dedup
		list_island = list(set_island)
		for point in list_island[:-1]:
			str_ += point.__str__() + ','
		str_ += list_island[-1].__str__() + '}'
		return str_

	def getAllIslands(self):
		return [self.islands.get(key) for key in self.islands.keys() if self.islands.get(key) is not None]


def solution(matrix):
	uf = UnionFind(matrix)
	uf.getIslands()
	uf.printIslands()

print 'Test 0:'
matrix = [
	[0, 0, 1, 1, 0, 1],
	[1, 0, 1, 0, 0, 0],
	[1, 0, 1, 0, 0, 0],
	[0, 1, 0, 0, 0, 0]
]
print 'input matrx = ', matrix
print 'solution below, for ultimate solution see last line of this section: '
solution(matrix)

print '\n\n\n\n\nTest 1:'
matrix = [
	[1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1]
]
print 'input matrx = ', matrix
print 'solution below, for ultimate solution see last line of this section: '
solution(matrix)

print '\n\n\n\n\nTest 2:'
matrix = [
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0]
]
print 'input matrx = ', matrix
print 'solution below, for ultimate solution see last line of this section: '
solution(matrix)

print '\n\n\n\n\nTest 3:'
matrix = [
	[1, 0, 0, 1, 0, 0],
	[0, 1, 1, 0, 0, 0],
	[0, 1, 1, 0, 0, 0],
	[1, 0, 0, 1, 0, 0]
]
print 'input matrx = ', matrix
print 'solution below, for ultimate solution see last line of this section: '
solution(matrix)

print '\n\n\n\n\nTest 4:'
matrix = [
	[1, 1, 1, 1, 1, 1],
	[1, 1, 1, 0, 1, 1],
	[1, 1, 1, 0, 1, 1],
	[1, 1, 0, 1, 1, 1]
]
print 'input matrx = ', matrix
print 'solution below, for ultimate solution see last line of this section: '
solution(matrix)

print '\n\n\n\n\nTest 5:'
matrix = [
	[1, 1, 1, 0, 1, 1],
	[1, 1, 1, 0, 1, 1],
	[1, 1, 1, 0, 1, 1],
	[1, 1, 1, 0, 1, 1]
]
print 'input matrx = ', matrix
print 'solution below, for ultimate solution see last line of this section: '
solution(matrix)

print '\n\n\n\n\nTest 6:'
matrix = [
	[1, 1, 1, 0, 1, 1],
]
print 'input matrx = ', matrix
print 'solution below, for ultimate solution see last line of this section: '
solution(matrix)

print '\n\n\n\n\nTest 7:'
matrix = [
	[1],
]
print 'input matrx = ', matrix
print 'solution below, for ultimate solution see last line of this section: '
solution(matrix)

print '\n\n\n\n\nTest 8:'
matrix = [
	[0],
]
print 'input matrx = ', matrix
print 'solution below, for ultimate solution see last line of this section: '
solution(matrix)

print '\n\n\n\n\nTest 9:'
matrix = [
	[0, 1],
	[1, 0]
]
print 'input matrx = ', matrix
print 'solution below, for ultimate solution see last line of this section: '
solution(matrix)

print '\n\n\n\n\nTest 10:'
matrix = [
	[0, 1],
	[1, 1]
]
print 'input matrx = ', matrix
print 'solution below, for ultimate solution see last line of this section: '
solution(matrix)