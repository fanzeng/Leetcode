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
    public TreeNode lcaDeepestLeaves(TreeNode root) {
        int d = getDepth(root);
        if (d == 1) return root;
        int[] depths = new int[1001];
        assignDepth(depths, root, 1);
        return find(root, depths, d);
    }
    private int getDepth(TreeNode n) {
        if (n.left == null && n.right == null) return 1;
        int l = -1, r = -1;
        if (n.left != null) l = 1 + getDepth(n.left);
        if (n.right != null) r = 1 + getDepth(n.right);
        return Math.max(l, r);
    }
    private void assignDepth(int[] depths, TreeNode n, int d) {
        depths[n.val] = d;
        if (n.left != null) assignDepth(depths, n.left, d+1);
        if (n.right != null) assignDepth(depths, n.right, d+1);
    }
    private TreeNode find(TreeNode n, int[] depths, int d) {
        if (n == null) return null;
        if (depths[n.val] == d-1) {
            if (n.left != null && n.right == null) return n.left;
            if (n.right != null && n.left == null) return n.right;
            if (n.left != null && n.right != null) return n;
            return null;
        }
        TreeNode l = find(n.left, depths, d);
        TreeNode r = find(n.right, depths, d);
        if (l != null && r == null) return l;
        if (r != null && l == null) return r;
        if (l != null && r != null) return n;
        return null;
    }
}
