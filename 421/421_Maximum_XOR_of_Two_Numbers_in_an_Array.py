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
        # print self.l_id_a
        self.d_id_a = {}
        for id_a in self.l_id_a:
            l_id_b = [id for id in range(len(nums)) if id != id_a]
            for bit in xrange(msb, 32):
                bit_val_a = self.getBitVal(id_a, bit)
                next_l_id_b = []
                for id_b in l_id_b:
                    bit_val_b = self.getBitVal(id_b, bit)
                    if bit_val_a != bit_val_b:
                        next_l_id_b.append(id_b)
                if len(next_l_id_b) > 0:
                    l_id_b = next_l_id_b
                if bit == 31:
                    self.d_id_a[id_a] = l_id_b
                # print bit, next_l_id_b
        # print self.d_id_a
        max_xor = 0
        for id_a in self.l_id_a:
            id_b = self.d_id_a[id_a][0]
            temp_xor = nums[id_a]^nums[id_b]
            if temp_xor > max_xor:
                max_xor = temp_xor
        return max_xor

    def toBinaryStr(self, num):
        return '{:b}'.format(num).zfill(32)

    def getBitVal(self, n, bit):
        return self.l_binary[n][bit]

test = Solution()
print test.findMaximumXOR([3,10,5,25,2,8]) # 28
print test.findMaximumXOR([8,10,2]) # 10
