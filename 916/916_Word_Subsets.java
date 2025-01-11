class Solution {
    public List<String> wordSubsets(String[] words1, String[] words2) {
        HashMap<Character, Integer> h = new HashMap<>();
        for (String word2 : words2) {
            HashMap<Character, Integer> h2 = count(word2);
            for (char c : h2.keySet()) {
                int v2 = h2.get(c);
                h.put(c, Math.max(h.getOrDefault(c, 0), v2));
            }
        }
        return Arrays.stream(words1).filter(w -> isSubset(w, h)).collect(Collectors.toList());
    }
    private boolean isSubset(String w, HashMap<Character, Integer> h) {
        HashMap<Character, Integer> h1 = count(w);
        for (char c : h.keySet()) {
            int v1 = h1.getOrDefault(c, 0);
            if (v1 < h.get(c)) return false;
        }
        return true;
    }
    private HashMap<Character, Integer> count(String w) {
        HashMap<Character, Integer> h = new HashMap<>();
        for (char c : w.toCharArray()) {
            h.put(c, h.getOrDefault(c, 0)+1);
        }
        return h;
    }
}
