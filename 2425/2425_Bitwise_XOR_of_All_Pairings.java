class Solution {
    public int xorAllNums(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> h = new HashMap<>();
        for (int num : nums1) h.put(num, h.getOrDefault(num, 0) + nums2.length);
        for (int num : nums2) h.put(num, h.getOrDefault(num, 0) + nums1.length);
        int ans = 0;
        for (int key : h.keySet()) {
            int count = h.get(key);
            if (count % 2 == 1) ans ^= key;
        }
        return ans;
    }
}
