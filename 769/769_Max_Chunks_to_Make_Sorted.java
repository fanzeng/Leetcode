class Solution {
    public int maxChunksToSorted(int[] arr) {
        int[] arrMax = new int[arr.length];
        int maxFromStart = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > maxFromStart) maxFromStart = arr[i];
            arrMax[i] = maxFromStart;
        }
        // System.out.println(Arrays.toString(arrMax));
        int[] arrMin = new int[arr.length];
        int minFromEnd = maxFromStart;
        for (int i = arr.length-1; i > -1; i--) {
            if (arr[i] < minFromEnd) minFromEnd = arr[i];
            arrMin[i] = minFromEnd;
        }
        // System.out.println(Arrays.toString(arrMin));
        int count = 0;
        for (int i = 0; i < arr.length-1; i++) {
            if (arrMax[i] < arrMin[i+1]) count++;
        }
        return count+1;
    }
}
