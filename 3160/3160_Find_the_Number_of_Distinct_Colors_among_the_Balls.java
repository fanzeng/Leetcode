class Solution {
    public int[] queryResults(int limit, int[][] queries) {
        int[] ans = new int[queries.length];
        // Keeps track of what color each ball has
        HashMap<Integer, Integer> bc = new HashMap<>();
        // Keeps track of how many balls have a certain color
        HashMap<Integer, Integer> h = new HashMap<>();
        int count = 0;
        for (int i = 0; i < queries.length; i++) {
            int[] q = queries[i];
            int ball = q[0];
            int color = q[1];
            int oldColor = bc.getOrDefault(ball, -1);
            if (oldColor != color) {
                if (h.getOrDefault(color, 0) == 0) count++;
                if (h.containsKey(oldColor)) {
                    h.put(oldColor, h.get(oldColor) - 1);
                    if (h.get(oldColor) == 0) count--;
                }
                h.put(color, h.getOrDefault(color, 0) + 1);
                bc.put(ball, color);
            }
            ans[i] = count;
        }
        return ans;
    }
}
