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
    // For node, store the sum of direct children on the next level
    // 2nd pass, replace value by retrieving parent on the level above
    // Give each parent node an id for the look up
    int id;
    HashMap<Integer, Integer> hmNodeSum = new HashMap<>(); // id -> sum of direct children of a node
    HashMap<Integer, Integer> hmLevelSum = new HashMap<>(); // depth -> sum of all direct children of level d
    HashMap<Integer, Integer> hmParent = new HashMap<>(); // id -> id of parent
    public TreeNode replaceValueInTree(TreeNode root) {
        id = 0;
        traverse(root, 0, -1);
        id = 0;
        update(root, 0);
        root.val = 0;
        return root;
    }
    // traverse(node, depth, parentID)
    public void traverse(TreeNode n, int d, int pid) {
        if (n == null) return;
        int sum = 0;
        if (n.left != null) sum += n.left.val;
        if (n.right != null) sum += n.right.val;
        hmParent.put(id, pid);
        hmNodeSum.put(id, sum);
        hmLevelSum.put(d, hmLevelSum.getOrDefault(d, 0) + sum);
        pid = id;
        id++;
        traverse(n.left, d+1, pid);
        traverse(n.right, d+1, pid);
    }
    // update(node, depth)
    public void update(TreeNode n, int d) {
        if (n == null) return;
        int pid = hmParent.get(id++);
        if (pid >= 0) {
            n.val = hmLevelSum.get(d-1) - hmNodeSum.get(pid);
        }
        update(n.left, d+1);
        update(n.right, d+1);
    }
}
