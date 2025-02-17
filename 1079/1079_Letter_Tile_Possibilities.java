class Solution {
    public int numTilePossibilities(String tiles) {
        int[] counts = new int[26];
        for (char c : tiles.toCharArray()) {
            counts[c - 'A']++;
        }
        for (int i = 0; i < 26; i++) {
            if (counts[i] > 0) {
                // System.out.printf("count[%d]=%d\n", i, counts[i]);
            } 
        }
        HashMap<Integer, Integer> memo = new HashMap<>();
        return dp(counts, memo);
    }
    private int dp(int[] counts, HashMap<Integer, Integer> memo) {
        int h = getHash(counts);
        if (memo.containsKey(h)) return memo.get(h);
        int total = 0;
        for (int i = 0; i < 26; i++) {
            if (counts[i] > 0) {
                int[] rest = new int[26];
                for (int j = 0; j < 26; j++) {
                    rest[j] = counts[j];
                }
                rest[i]--;
                total += 1+dp(rest, memo);
            }
        }
        memo.put(h, total);
        return total;
    }
    private static int getHash(int[] counts) {
        int h = 0;
        int b = 1;
        for (int i = 0; i < 26; i++) {
            h += counts[i]*b;
            b *= 26;
        }
        return h;
    }
}
