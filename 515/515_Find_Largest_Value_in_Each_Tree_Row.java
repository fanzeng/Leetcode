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
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        traverse(root, list, 0);
        return list;
    }
    private void traverse(TreeNode n, List<Integer> list, int d) {
        if (n == null) return;
        if (list.size() > d) {
            list.set(d, Math.max(list.get(d), n.val));
        } else {
            list.add(n.val);
        }
        traverse(n.left, list, d+1);
        traverse(n.right, list, d+1);
    }
}
