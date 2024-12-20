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
    public TreeNode reverseOddLevels(TreeNode root) {
        HashMap<Integer, Stack<Integer>> h = new HashMap<>();
        int d = 0;
        traverse(root, h, d);
        // printHashMap(h);
        traverseUpdate(root, h, d);
        return root;
    }
    private void traverse(TreeNode n, HashMap<Integer, Stack<Integer>> h, int d) {
        if (n == null) return;
        if (d % 2 == 1) {
            h.get(d).add(n.val);
        } else if (h.get(d+1) == null) {
            h.put(d+1, new Stack<>());
        }
        traverse(n.left, h, d+1);
        traverse(n.right, h, d+1);
    }
    private void traverseUpdate(TreeNode n, HashMap<Integer, Stack<Integer>> h, int d) {
        if (n == null) return;
        if (d % 2 == 1) {
            n.val = h.get(d).pop();
        }
        traverseUpdate(n.left, h, d+1);
        traverseUpdate(n.right, h, d+1);
    }
    private void printHashMap(HashMap<Integer, Stack<Integer>> h) {
        for (Map.Entry<Integer, Stack<Integer>> entry : h.entrySet()) {
            Integer key = entry.getKey();
            Stack<Integer> stack = entry.getValue();
            System.out.println("Key: " + key + ", Stack: " + stack);
        }
    }
}
