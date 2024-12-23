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
    public int minimumOperations(TreeNode root) {
        List<List<Integer>> arrs = new ArrayList<>();
        traverse(root, arrs, 0);
        int count = 0;
        for (int i = 0; i < arrs.size(); i++) {
            count += swaps(arrs.get(i));
        }
        return count;
    }
    private void traverse(TreeNode n, List<List<Integer>> arrs, int d) {
        if (n == null) return;
        if (d >= arrs.size()) arrs.add(d, new ArrayList<>());
        arrs.get(d).add(n.val);
        traverse(n.left, arrs, d+1);
        traverse(n.right, arrs, d+1);
    }
    private int swaps(List<Integer> arr) {
        // System.out.println(arr);
        HashMap<Integer, Integer> h = new HashMap<>();
        for (int i = 0; i < arr.size(); i++) {
            h.put(arr.get(i), i);
        }
        int[] nums = arr.stream().mapToInt(Integer::intValue).toArray();
        Arrays.sort(nums);
        // System.out.println(Arrays.toString(nums));
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            if (arr.get(i) == nums[i]) continue;
            arr.set(h.get(nums[i]), arr.get(i));
            h.put(arr.get(i), h.get(nums[i]));
            count++;
        }
        return count;
    }
}
