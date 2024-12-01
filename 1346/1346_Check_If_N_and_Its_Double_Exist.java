class Solution {
    public boolean checkIfExist(int[] arr) {
        HashSet<Integer> h = new HashSet<>();
        for (int i = 0; i < arr.length; i++) {
            h.add(arr[i]*2);
        }
        boolean zeroSeen = false;
        for (int i = 0; i < arr.length; i++) {
            if (h.contains(arr[i])) {
                if (arr[i] == 0) {
                    if (zeroSeen) return true;
                    zeroSeen = true;
                } else {
                    return true;
                }
            }
        }
        return false;
    }
}
