class Solution {
    public int countPalindromicSubsequence(String s) {
        int[] first = new int[26];
        int[] last = new int[26];
        for (int i = 0; i < 26; i++) {
            first[i] = -1;
        }
        for (int i = 0; i < s.length(); i++) {
            int c = s.charAt(i) - 'a';
            if (first[c] == -1) first[c] = i;
            last[c] = i;
        }
        int[][] arr = new int[26][26];
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                arr[i][j] = 0;
            }
        }
        for (int i = 0; i < s.length(); i++) {
            int m = s.charAt(i) - 'a';
            for (int j = 0; j < 26; j++) {
                if (arr[m][j] == 1) continue;
                if (first[m] == -1) continue;
                if (first[j] < i && last[j] > i) arr[m][j] = 1;
            }
        }
        int count = 0;
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                count += arr[i][j];
            }
        }
        return count;
    }
}
