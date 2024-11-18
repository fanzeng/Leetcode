class Solution {
    public int[] decrypt(int[] code, int k) {
        int sz = code.length;
        int[] decode = new int[sz];
        if (k == 0) return decode;
        int dir;
        if (k > 0) {
            dir = 1;
        } else {
            dir = -1;
        }
        int sum = 0;
        for (int i = 0; i < Math.abs(k); i++) {
            sum += code[((i+1)*dir+sz) % sz];
        }
        decode[0] = sum;
        for (int i = 1; i < sz; i++) {
            if (k > 0) {
                sum += code[(i+k)%sz] - code[i];
            } else {
                sum += code[i-1] - code[(i-1+k+sz) % sz];
            }
            decode[i] = sum;
        }
        return decode;
    }
}
