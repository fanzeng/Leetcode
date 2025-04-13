class Solution {
    long m = (long)(1e9 + 7);
    public int countGoodNumbers(long n) {
        return (int)(fastExp(5, (n+1) / 2) * fastExp(4, n / 2) % m);
    }

    private long fastExp(long a, long n) {
        long res = 1;
        while (n > 0) {
            if (n % 2 == 1) {
                res = (res * a) % m;
            }
            a = (a*a) % m;
            n /= 2;
        }
        return res;
    }
}
