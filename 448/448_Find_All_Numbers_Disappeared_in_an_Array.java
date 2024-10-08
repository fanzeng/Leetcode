class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        boolean[] a = new boolean[nums.length];
        ArrayList<Integer> r = new ArrayList();
        for (int i = 0; i < nums.length; i++) {
            a[nums[i] - 1] = true;
        }
        for (int i = 0; i < nums.length; i++) {
            if (!a[i]) {
                r.add(i + 1);
            }
        }
        return r;
    }
}
