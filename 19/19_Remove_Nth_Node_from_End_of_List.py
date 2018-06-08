# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def __repr__(self):
		repr_str = ''
		head = self
		while(head != None):
			repr_str += str(head.val) + '->'
			head = head.next
		repr_str += 'None'
		return repr_str

def init_with_list(self, integer_list):
	if len(integer_list) == 0:
		return None
	elif len(integer_list) == 1:
		self.val = integer_list[0]
		self.next = None
		return self
	else:
		self.val = integer_list[0]
		self.next = ListNode(integer_list[1]).init_with_list(integer_list[1:])
		return self
ListNode.init_with_list = init_with_list

class Solution(object):

	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		rest = [head]
		visited = [head.val]

		count = 0
		while(head.next != None):
			rest.append(head.next)
			head = head.next
			visited.append(head.val)

			count += 1
		# print rest
		# print visited, visited[:count-n+1]
		res = ListNode(0).init_with_list(visited[:count-n+1]+visited[count-n+2:])
		# print res
		return res

test = Solution()
temp = ListNode(0)
head = temp.init_with_list([1, 2, 3, 4, 5])
print head
print test.removeNthFromEnd(head, 3)

head = temp.init_with_list([1, 2])
print head
print test.removeNthFromEnd(head, 2)
print test.removeNthFromEnd(head, 1)

head = temp.init_with_list([1])
print head
print test.removeNthFromEnd(head, 1)