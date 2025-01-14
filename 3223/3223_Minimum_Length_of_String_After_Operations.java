class Solution {
    public int minimumLength(String s) {
        HashMap<Character, Integer> h = new HashMap<>();
        for (char c : s.toCharArray()) {
            h.put(c, h.getOrDefault(c, 0) + 1);
        }
        int count = 0;
        for (char c : h.keySet()) {
            // System.out.printf("h[%c] = %d\n", c, h.get(c));
            if (h.get(c) % 2 == 0) {
                count += 2;
            } else {
                count += 1;
            }
        }
        return count;
    }
}
