class Solution {
    public int minimumIndex(List<Integer> nums) {
        int n = nums.size();
        int dom = nums.get(0);
        Map<Integer, Integer> h = new HashMap<>();
        for (int num : nums) {
            h.put(num, h.getOrDefault(num, 0) + 1);
            if (h.get(num) > n/2) {
                dom = num;
                break;
            }
        }
        int total = 0;
        for (int num : nums) {
            if (num == dom) total++;
        }
        // System.out.printf("dominant = %d\n", dom);
        int res = -1;
        int count = 0;
        while (++res < n) {
            if (nums.get(res) == dom) count++;
            if (isValid(count, total, res, n)) return res;
        }
        return -1;
    }
    private boolean isValid(int count, int total, int i, int n) {
        return count > (i+1)/2 && total - count > (n-1-i)/2;
    }
}
