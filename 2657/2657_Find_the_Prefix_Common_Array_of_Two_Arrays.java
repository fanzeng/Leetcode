class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        int n = A.length;
        int[] count = new int[51];
        int res = 0;
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            count[A[i]]++;
            if (count[A[i]] == 2) res++;
            count[B[i]]++;
            if (count[B[i]] == 2) res++;
            ans[i] = res;
        }
        return ans;
    }
}
