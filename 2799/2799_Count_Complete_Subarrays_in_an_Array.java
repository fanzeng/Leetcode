class Solution {
    public int countCompleteSubarrays(int[] nums) {
        int min = 2001;
        int max = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < min) min = nums[i];
            if (nums[i] > max) max = nums[i];
        }
        int[] seen = new int[max-min+1];
        int distinct = 0;
        for (int i = 0; i < nums.length; i++) {
            if (seen[nums[i]-min]++ == 0) distinct++;
        }
        int res = 0;
        int[] count = new int[max-min+1];
        count[nums[0] - min] = 1;
        int uniq = 1;
        int i = 0, j = 0; // both inclusive
        while (j < nums.length) {
            while (uniq < distinct) {
                j++;
                if (j == nums.length) break;
                count[nums[j] - min]++;
                if (count[nums[j] - min] == 1) uniq++;
            }
            while (uniq == distinct) {
                res += nums.length-j;
                i++;
                count[nums[i-1] - min]--;
                if (count[nums[i-1] - min] == 0) uniq--;
            }
        }
        return res;
    }
}
