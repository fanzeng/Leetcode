class Solution {
    public int minimizeXor(int num1, int num2) {
        int[] a1 = toBinaryArr(num1);
        int[] a2 = toBinaryArr(num2);
        int[] x = new int[a1.length];
        // System.out.println(Arrays.toString(a1));
        // System.out.println(Arrays.toString(a2));
        int ones = Arrays.stream(a2).sum();
        // System.out.printf("ones = %d\n", ones);
        int i = 0;
        while (ones > 0) {
            while (i < a1.length && a1[i] == 0) i++;
            if (i == a1.length) break;
            a1[i] = 0;
            x[i] = 1;
            ones--;
        }
        if (ones > 0) {
            int[] res = new int[ones + x.length];
            System.arraycopy(x, 0, res, ones, x.length);
            // System.out.println(Arrays.toString(res));
            int j = res.length-1;
            while (ones > 0) {
                while (res[j] == 1) j--;
                res[j] = 1;
                j--;
                ones--;
            }
            return arrToInt(res);
        } else {
            return arrToInt(x);
        }
    }
    private int[] toBinaryArr(int num) {
        String s = Integer.toBinaryString(num);
        int[] arr = new int[s.length()];
        for (int i = 0; i < s.length(); i++) {
            arr[i] = Character.getNumericValue(s.charAt(i));
        }
        return arr;
    }
    private int arrToInt(int[] arr) {
        StringBuilder sb = new StringBuilder();
        for (int bit : arr) {
            sb.append(bit);
        }
        return Integer.parseInt(sb.toString(), 2);
    }
}
