class Solution {
    public int countLargestGroup(int n) {
        int[] counts = new int[9*String.valueOf(n).length()+1];
        for (int i = 1; i <= n; i++) {
            char[] ca = String.valueOf(i).toCharArray();
            int s = 0;
            for (int j = 0; j < ca.length; j++) {
                s += ca[j] - '0';
            }
            counts[s]++;
        }
        int largest = 0;
        for (int i = 0; i < counts.length; i++) {
            // System.out.printf("counts[%d] = %d\n", i, counts[i]);
            if (counts[i] > largest) largest = counts[i];
        }
        int res = 0;
        for (int i = 0; i < counts.length; i++) {
            if (counts[i] == largest) res++;
        }
        return res;
    }
}
