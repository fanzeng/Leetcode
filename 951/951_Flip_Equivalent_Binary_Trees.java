/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean flipEquiv(TreeNode root1, TreeNode root2) {
        return checkFlipEquiv(root1, root2);
    }
    // Subtree n1 is "flip equivalent" to n2 iff
    // val equals, and
    // children "flip equivalent", or flipped children "flip equivalent"
    boolean checkFlipEquiv(TreeNode n1, TreeNode n2) {
       if (n1 == null) return n2 == null;
       if (n2 == null) return false;
       if (n1.val != n2.val) return false;
       boolean direct = checkFlipEquiv(n1.left, n2.left) && checkFlipEquiv(n1.right, n2.right);
       boolean flipped = checkFlipEquiv(n1.left, n2.right) && checkFlipEquiv(n1.right, n2.left);
       return direct || flipped;
    }
}
