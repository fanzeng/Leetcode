class Solution {
    public List<String> getLongestSubsequence(String[] words, int[] groups) {
        List<String> res = new ArrayList<>();
        int i = 0;
        res.add(words[0]);
        int prev = groups[0];
        while (++i < groups.length) {
            if (groups[i] != prev) {
                res.add(words[i]);
                prev = groups[i];
            }
        }
        return res;
    }
}
