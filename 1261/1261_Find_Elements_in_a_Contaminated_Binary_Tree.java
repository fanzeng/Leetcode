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
class FindElements {
    HashSet<Integer> h = new HashSet<>();
    public FindElements(TreeNode root) {
        root.val = 0;
        h.add(0);
        dfs(root);
    }
    
    private void dfs(TreeNode n) {
        if (n == null) return;
        if (n.left != null) {
            n.left.val = 2*n.val + 1;
            h.add(n.left.val);
            dfs(n.left);
        }
        if (n.right != null) {
            n.right.val = 2*n.val + 2;
            h.add(n.right.val);
            dfs(n.right);
        }
    }
    
    public boolean find(int target) {
        return h.contains(target);
    }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements obj = new FindElements(root);
 * boolean param_1 = obj.find(target);
 */
