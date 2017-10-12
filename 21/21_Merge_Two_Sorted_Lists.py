# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None



def print_list_node(node):
	if node != None:

		while node.next != None:
			print node.val, '->',
			node = node.next
		print node.val

def init_list_node(list):
	if not len(list) > 0:
		return None
	i = 0
	node = ListNode(list[0])
	head = node
	i += 1
	while i < len(list):
		node.next = ListNode(list[i])
		node = node.next
		i += 1
	return head


class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		reverse = False
		l1_0 = l1
		l2_0 = l2
		while True:
			if l1_0 != None and l1_0.next != None:
				if l1_0.val > l1_0.next.val:
					reverse = True
					break
				else:
					l1_0 = l1_0.next
			elif l2_0 != None and l2_0.next != None:
				if l2_0.val > l2_0.next.val:
					reverse = True
					break
				else:
					l2_0 = l2_0.next
			else:
				break



		result = []
		if not reverse:
			while True:
				if l1 == None:
					if l2 == None:
						break
					else:
						result.append(l2.val)
						l2 = l2.next

				elif l2 == None:
					result.append(l1.val)
					l1 = l1.next

				else:

					if l1.val<l2.val:
						result.append(l1.val)
						l1 = l1.next
					else:
						result.append(l2.val)
						l2 = l2.next
		else:
			while True:
				if l1 == None:
					if l2 == None:
						break
					else:
						result.append(l2.val)
						l2 = l2.next

				elif l2 == None:
					result.append(l1.val)
					l1 = l1.next

				else:

					if l1.val > l2.val:
						result.append(l1.val)
						l1 = l1.next
					else:
						result.append(l2.val)
						l2 = l2.next

		return init_list_node(result)


l1 = init_list_node([1, 3, 5, 7, 9])
l2 = init_list_node([2, 4, 6, 8, 10])
l1 = init_list_node([1, 3, 5, 7, 9])
l2 = init_list_node([2, 4, 5, 6, 8, 10])
l1 = init_list_node([1, 3, 5, 7, 9])
l2 = init_list_node([2, 4, 5, 6, 8, 10, 11])
l1 = init_list_node([])
l2 = init_list_node([2, 4, 6, 8, 10])
l1 = init_list_node([])
l2 = init_list_node([])
l1 = init_list_node([9, 7, 5, 3, 1])
l2 = init_list_node([10, 8, 6, 4, 2, 0])
print_list_node(l1)
print_list_node(l2)
test = Solution()
print_list_node(test.mergeTwoLists(l1, l2))
