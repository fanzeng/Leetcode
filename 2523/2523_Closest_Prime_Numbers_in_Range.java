class Solution {
    public int[] closestPrimes(int left, int right) {
        List<Integer> primes = sieve(right+1);
        int[] res = new int[]{-1, -1};
        int diff = right - left + 1;
        int i = 0, j = 1;
        while (j < primes.size()) {
            if (primes.get(i) < left) {
                i++; j++;
                continue;
            }
            // System.out.printf("%d, %d\n", primes.get(i), primes.get(j));
            if (primes.get(j) - primes.get(i) < diff) {
                diff = primes.get(j) - primes.get(i);
                res[0] = primes.get(i);
                res[1] = primes.get(j);
            }
            if (diff == 2) break;
            i++; j++;
        }
        return res;
    }
    private List<Integer> sieve(int n) {
        boolean[] isPrime = new boolean[n];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i < n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j < n; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i < n; i++) {
           if (isPrime[i]) primes.add(i);
        }
        return primes;
    }
}
