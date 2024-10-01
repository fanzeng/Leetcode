class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for n in arr:
            i = ((n % k) + k) % k
            if d.get(i) is None:
                d[i] = 1
            else:
                d[i] += 1
        # print d
        if d.get(0) is not None:
            if d[0] % 2 == 1:
                return False
        for i in range(1, k):
            if d.get(i) is None:
                d[i] = 0
            if d.get(k-i) is None:
                d[k-i] = 0
            if i == k - i:
                if d[i] % 2 == 1:
                    return False
            if d[i] != d[k-i]:
                return False
        return True
