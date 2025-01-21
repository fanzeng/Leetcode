class Solution {
    public int firstCompleteIndex(int[] arr, int[][] mat) {
        int[] paintedR = new int[mat.length];
        int[] paintedC = new int[mat[0].length];
        HashMap<Integer, Integer> hr = new HashMap<>();
        HashMap<Integer, Integer> hc = new HashMap<>();
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[0].length; j++) {
                int v = mat[i][j];
                hr.put(v, i);
                hc.put(v, j);
            }
        }
        for (int i = 0; i < arr.length; i++) {
            int r = hr.get(arr[i]);
            int c = hc.get(arr[i]);
            paintedR[r]++;
            paintedC[c]++;
            if (paintedR[r] == mat[0].length || paintedC[c] == mat.length) return i;
        }
        return 0; 
    }
}
