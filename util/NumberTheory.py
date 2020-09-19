def gcd(a, b):
    if a == 1 or b == 1:
        return 1
    if a == b:
        return a
    bigger = max([a, b])
    smaller = min([a, b])
    if bigger % smaller == 0:
        return smaller
    return gcd(smaller, bigger % smaller)

def getPrimes(max_num):
    l_not_prime = set()
    for p in xrange(2, max_num+1):
        if p in l_not_prime:
            continue
        n = 2*p
        while n <= max_num:
            l_not_prime.add(n)
            n += p
        if p*p > max_num:
            break
    return [x for x in xrange(2, max_num+1) if x not in l_not_prime]

def primeFactorization(num, l_primes=None):
    if l_primes is None:
        l_primes = getPrimes(num)
    l_factor = []
    for prime in l_primes:
        if num % prime == 0:
            l_factor.append(prime)
            while num % prime == 0:
                num /= prime
    return l_factor

if __name__ == '__main__':
    prime_1000 = getPrimes(1000)
    print 'primes under 1000:', prime_1000
    print primeFactorization(666) # [2, 3, 37]
    print primeFactorization(1024) # [2]
    print primeFactorization(997) # [997]