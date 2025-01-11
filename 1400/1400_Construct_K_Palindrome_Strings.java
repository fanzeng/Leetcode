class Solution {
    public boolean canConstruct(String s, int k) {
        if (s.length() < k) return false;
        HashMap<Character, Integer> h = new HashMap<>();
        for (char c : s.toCharArray()) {
            h.put(c, h.getOrDefault(c, 0) + 1);
        }
        int oddCount = 0;
        for (char c : h.keySet()) {
            int count = h.get(c);
            oddCount += count % 2;
        }
        return oddCount <= k;
    }
}
