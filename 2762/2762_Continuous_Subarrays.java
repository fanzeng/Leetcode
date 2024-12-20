class Solution {
    public long continuousSubarrays(int[] nums) {
        int i = 0;
        long count = 0;
        HashMap<Integer, Integer> h = new HashMap<>();
        for (int j = 0; j < nums.length; j++) {
            h.put(nums[j], h.getOrDefault(nums[j], 0) + 1);
            while (!isCont(h)) {
                h.put(nums[i], h.get(nums[i]) - 1);
                i++;
            }
            // System.out.printf("i = %d, j = %d\n", i, j);
            count += j-i+1;
        }
        return count;
    }
    private boolean isCont(HashMap<Integer, Integer> h) {
        if (h.isEmpty()) return true;
        Map.Entry<Integer, Integer> minEntry = null, maxEntry = null;
        for (Map.Entry<Integer, Integer> entry : h.entrySet()) {
            if (entry.getValue() == 0) continue;
            // System.out.printf("Key = %d, Value = %d\n", entry.getKey(), entry.getValue());
            if (minEntry == null || entry.getKey() < minEntry.getKey()) minEntry = entry;
            if (maxEntry == null || entry.getKey() > maxEntry.getKey()) maxEntry = entry;
        }
        // System.out.printf("maxEntry.key = %d, maxEntry.value = %d\n", maxEntry.getKey(), maxEntry.getValue());
        // System.out.printf("minEntry.key = %d, minEntry.value = %d\n", minEntry.getKey(), minEntry.getValue());
        return Math.abs(maxEntry.getKey() - minEntry.getKey()) < 3;
    }
}
