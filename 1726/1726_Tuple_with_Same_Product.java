class Solution {
    public int tupleSameProduct(int[] nums) {
        HashMap<Integer, Integer> h = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            for (int j = i+1; j < nums.length; j++) {
                int p = nums[i]*nums[j];
                h.put(p, h.getOrDefault(p, 0) + 1);
            }
        }
        int res = 0;
        for (Map.Entry<Integer, Integer> entry : h.entrySet()) {
            // System.out.printf("%d: %d\n", entry.getKey(), entry.getValue());
            int v = entry.getValue();
            if (v < 2) continue;
            res += v*(v - 1)/2*8;
        }
        return res;
    }
}
