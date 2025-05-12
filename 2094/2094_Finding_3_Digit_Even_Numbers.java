class Solution {
    public int[] findEvenNumbers(int[] digits) {
        int[] counts = new int[10];
        for (int i = 0; i < digits.length; i++) {
            counts[digits[i]] += 1;
        }
        List<Integer> res = new ArrayList<>();
        for (int i = 1; i < 10; i++) {
            if (counts[i] == 0) continue;
            counts[i]--;
            for (int j = 0; j < 10; j++) {
                if (counts[j] == 0) continue;
                counts[j]--;
                for (int k = 0; k < 9; k+=2) {
                    if (counts[k] == 0) continue;
                    res.add(100*i + 10*j + k);
                }
                counts[j]++;
            }
            counts[i]++;
        }
        return res.stream().mapToInt(Integer::intValue).toArray();
    }
}
