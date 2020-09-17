class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        self.l_binary = []
        for num in nums:
            self.l_binary.append(self.toBinaryStr(num))
        self.l_id_a = []
        msb = None
        for bit in xrange(32):
            for n in xrange(len(nums)):
                bit_val = self.getBitVal(n, bit)
                if bit_val == '1':
                    self.l_id_a.append(n)
            if len(self.l_id_a) > 0:
                msb = bit
                break
        max_possible = int('1'*(32-msb), 2)
        # print self.l_id_a
        max_xor = 0
        for id_a in self.l_id_a:
            l_id_b = [id for id in range(len(nums)) if id != id_a]
            for id_b in l_id_b:
                temp_xor = nums[id_a]^nums[id_b]
                if temp_xor > max_xor:
                    max_xor = temp_xor
                if max_xor == max_possible:
                    return max_possible
        return max_xor

    def toBinaryStr(self, num):
        return '{:b}'.format(num).zfill(32)

    def getBitVal(self, n, bit):
        return self.l_binary[n][bit]

test = Solution()
print test.findMaximumXOR([3,10,5,25,2,8]) # 28
print test.findMaximumXOR([8,10,2]) # 10
