class Solution {
    public int[] vowelStrings(String[] words, int[][] queries) {
        int[] m = new int[words.length];
        for (int i = 0; i < words.length; i++) {
            if (isVowel(words[i])) {
                m[i] = 1;
            } else {
                m[i] = 0;
            }
        }
        // System.out.println(Arrays.toString(m));
        int[] sum = new int[m.length];
        int s = 0;
        for (int i = 0; i < m.length; i++) {
            s += m[i];
            sum[i] = s;
        }
        // System.out.println(Arrays.toString(sum));
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            if (queries[i][0] == 0) {
                ans[i] = sum[queries[i][1]];
            } else {
                ans[i] = sum[queries[i][1]] - sum[queries[i][0]-1];
            }
        }
        return ans;
    }
    private boolean isVowel(String word) {
        boolean begin = false;
        boolean end = false;
        for (char c : new char[]{'a', 'e', 'i', 'o', 'u'}) {
            if (word.charAt(0) == c) begin = true;
            if (word.charAt(word.length()-1) == c) end = true;
        }
        return begin && end;
    }
}
