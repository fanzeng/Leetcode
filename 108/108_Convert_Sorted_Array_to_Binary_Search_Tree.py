# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums is None or len(nums) == 0:
            return None
        m = len(nums)/2
        n = TreeNode(nums[m])
        if m == 0:
            n.left = None
        else:
            n.left = self.sortedArrayToBST(nums[:m])
        if m + 1 == len(nums):
            n.right = None
        else:
            n.right = self.sortedArrayToBST(nums[m+1:])
        return n

def tree2Str(root):
    n = root
    s = ''
    if n is not None:
        s += str(n.val) + '\n'
        s_left = tree2Str(root.left)
        if s_left is not None and len(s_left) > 0:
            s += 'left = ' + s_left
        s_right = tree2Str(root.right)
        if s_right is not None and len(s_right) > 0:
            s += 'right = ' + s_right
    return s

test = Solution()
print tree2Str(test.sortedArrayToBST([-10,-3,0,5,9]))
