class Solution {
    public long countOfSubstrings(String word, int k) {
        char[] arr = word.toCharArray();
        int[][] counts = new int[word.length()][6];
        int countA = 0, countE = 0, countI = 0, countO = 0, countU = 0, countC = 0;
        for (int i = 0; i < arr.length; i++) {
            char c = arr[i];
            if (c == 'a') {
                countA++;
            } else if (c == 'e') {
                countE++;
            } else if (c == 'i') {
                countI++;
            } else if (c == 'o') {
                countO++;
            } else if (c == 'u') {
                countU++;
            } else {
                countC++;
            }
            counts[i][0] = countA; 
            counts[i][1] = countE; 
            counts[i][2] = countI; 
            counts[i][3] = countO; 
            counts[i][4] = countU; 
            counts[i][5] = countC; 
        }
        return atLeast(counts, k) - atLeast(counts, k+1);
    }
    // Check if substr from i to j (included) satisfy having all vowels and at least k consonants.
    private boolean satisfy(int[][] counts, int i, int j, int k) {
        int countA = counts[j][0];
        int countE = counts[j][1];
        int countI = counts[j][2];
        int countO = counts[j][3];
        int countU = counts[j][4];
        int countC = counts[j][5];
        if (i > 0) {
            countA -= counts[i-1][0];
            countE -= counts[i-1][1];
            countI -= counts[i-1][2];
            countO -= counts[i-1][3];
            countU -= counts[i-1][4];
            countC -= counts[i-1][5];
        }
        return countA > 0 && countE > 0 && countI > 0 && countO > 0 && countU > 0 && countC >= k;
    }
    private long atLeast(int[][] counts, int k) {
        int n = counts.length;
        long res = 0;
        int i = -1, j = -1;
        // Find first j so that substr from i to j (included) satisfy.
        while (++i < n) {
            // i+4+k is the shortest possible length to satisfy.
            j = Math.max(j, (i + 4 + k) - 1);
            while (j < n && !satisfy(counts, i, j, k)) j++;
            if (j == n) break;
            res += n - j;
        }
        return res;
    }
}
