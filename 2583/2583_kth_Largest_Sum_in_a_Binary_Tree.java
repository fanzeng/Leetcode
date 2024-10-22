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
    HashMap<Integer, Long> levelSum = new HashMap<>();
    public long kthLargestLevelSum(TreeNode root, int k) {
        traverse(root, 1);
        ArrayList<Map.Entry<Integer, Long>> entries = new ArrayList<>(levelSum.entrySet());
        Collections.sort(entries, (a, b) -> b.getValue().compareTo(a.getValue()));
        if (k > entries.size()) return -1;
        return entries.get(k-1).getValue();
    }
    private void traverse(TreeNode n, int d) {
        if (n == null) return;
        if (!levelSum.containsKey(d)) {
            levelSum.put(d, (long)n.val);
        } else {
            levelSum.put(d, levelSum.get(d) + n.val);
        }
        traverse(n.left, d+1);
        traverse(n.right, d+1);
    }
}
