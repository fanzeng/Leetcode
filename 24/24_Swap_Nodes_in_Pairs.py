# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def swapPairs(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if head == None:
			return None
		if head.next == None:
			return head
		elif head.next.next == None:
			second = head.next
			second.next = head
			head.next = None
			return second
		else:
			second = head.next
			head_next_pair = second.next
			second.next = head
			head.next = self.swapPairs(head_next_pair)
			return second


	def make_list_node(self, val_list):
		node = ListNode(val_list[0])
		if len(val_list) > 1:
			node.next = self.make_list_node(val_list[1:])
		return node

	def print_list_node(self, head):
		if head.next == None:
			return str(head.val)
		else:
			return str(head.val) + '->' + self.print_list_node(head.next)

test = Solution()
head = test.make_list_node([1, 2, 3, 4])
print test.print_list_node(head)
print test.print_list_node( test.swapPairs(head) )

head = test.make_list_node([1])
print test.print_list_node(head)
print test.print_list_node( test.swapPairs(head) )
