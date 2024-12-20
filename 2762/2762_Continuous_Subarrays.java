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
            count += j-i+1;
        }
        return count;
    }
    private boolean isCont(HashMap<Integer, Integer> h) {
        if (h.isEmpty()) return true;
        Map.Entry<Integer, Integer> minEntry = null, maxEntry = null;
        for (Map.Entry<Integer, Integer> entry : h.entrySet()) {
            if (entry.getValue() == 0) continue;
            if (minEntry == null || entry.getKey() < minEntry.getKey()) minEntry = entry;
            if (maxEntry == null || entry.getKey() > maxEntry.getKey()) maxEntry = entry;
        }
        return Math.abs(maxEntry.getKey() - minEntry.getKey()) < 3;
    }
}
