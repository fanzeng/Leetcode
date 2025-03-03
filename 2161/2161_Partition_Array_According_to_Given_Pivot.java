class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int[] res = new int[nums.length];
        int j = 0;
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < pivot) {
                res[j++] = nums[i];
            } else if (nums[i] == pivot) {
                count++;
            }
        }
        while (count > 0) {
            res[j++] = pivot;
            count--;
        }
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > pivot) {
                res[j++] = nums[i];
            }
        }
        return res;
    }
}
