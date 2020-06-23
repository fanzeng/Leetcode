import math

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max([abs(n) for n in nums])
        magic_num_bit_len = 2048
        magic_num_bit_len_half = magic_num_bit_len/2

        magicNumbers = [0]*(max_num/magic_num_bit_len_half+1)
        for n in nums:
            magicNumber = magicNumbers[abs(n)/magic_num_bit_len_half]
            four_to_n = 4**(abs(n)%magic_num_bit_len_half)
            carry = magicNumber & (four_to_n*2)
            if carry != 0:
                magicNumber &= 2**magic_num_bit_len-1 - four_to_n*2
            else:
                if magicNumber & four_to_n == 0:
                    magicNumber |= four_to_n
                else:
                    magicNumber &= 2**magic_num_bit_len-1 - four_to_n
                    magicNumber |= (four_to_n*2)
            magicNumbers[abs(n)/magic_num_bit_len_half] = magicNumber
        for i, magicNumber in enumerate(magicNumbers):
            if magicNumber != 0:
                res_abs = magic_num_bit_len_half*i + long(math.log(magicNumber, 4))
                break
        if res_abs == 0:
            return 0
        pos = 0
        neg = 0
        for n in nums:
            if abs(n) == res_abs:
                if n > 0:
                    pos += 1
                else:
                    neg += 1

        if pos == 1:
            return res_abs
        else:
            return -res_abs

test = Solution()
print test.singleNumber([2,2,3,2]) # 3
print test.singleNumber([0,0,0,99]) # 99

print test.singleNumber([40,40,40,-27]) # -27
print test.singleNumber([27,27,27,-27]) # -27

print test.singleNumber([-19,-46,-19,-46,-9,-9,-19,17,17,17,-13,-13,-9,-13,-46,-28]) # -28

print test.singleNumber([43,16,45,89,45,-2147483648,45,2147483646,-2147483647,-2147483648,43,2147483647,-2147483646,-2147483648,89,-2147483646,89,-2147483646,-2147483647,2147483646,-2147483647,16,16,2147483646,43]) # 2147483647
