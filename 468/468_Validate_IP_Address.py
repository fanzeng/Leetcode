class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if IP is None or len(IP) == 0:
            return "Neither"
        if self.isValidIPv4(IP):
            return "IPv4"
        elif self.isValidIPv6(IP):
            return "IPv6"
        else:
            return "Neither"

    def isValidIPv4(self, s):
        l = s.split('.')
        if len(l) != 4:
            return False
        for n in l:
            if not self.isValidIPv4Octet(n):
                return False
        return True

    def isValidIPv4Octet(self, s):
        if s is None or len(s) == 0:
            return False
        for c in s:
            if not (ord(c) >= ord('0') and ord(c) <= ord('9')):
                return False
        n = int(s)
        if n < 0 or n > 255:
            return False
        if n > 0:
            if s[0] == '0':
                return False
        if n == 0:
            if s != '0':
                return False
        return True

    def isValidIPv6(self, s):
        l = s.split(':')
        if len(l) != 8:
            return False
        for n in l:
            if not self.isValidIPv6Group(n):
                return False
        return True

    def isValidIPv6Group(self, s):
        if s is None or len(s) == 0 or len(s) > 4:
            return False
        for c in s:
            if not self.isValidHexChar(c):
                return False
        if len(s) > 1:
            if s[0] == '0' and s[1] == '0':
                for c in s[2:]:
                    if c != '0':
                        return False
        return True

    def isValidHexChar(self, c):
        if ord(c) >= ord('0') and ord(c) <= ord('9'):
            return True
        if ord(c) >= ord('A') and ord(c) <= ord('F'):
            return True
        if ord(c) >= ord('a') and ord(c) <= ord('f'):
            return True
        return False

test = Solution()
print test.validIPAddress("172.16.254.1") # IPv4
print test.validIPAddress("0.0.0.0") # IPv4
print test.validIPAddress("255.255.255.255") # IPv4

print test.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334") # IPv6
print test.validIPAddress("2001:db8:85a3:0:0:8A2E:0370:7334") # IPv6

print test.validIPAddress("256.256.256.256") # Neither
print test.validIPAddress("172.16.254.01") # Neither
print test.validIPAddress("2001:0db8:85a3::8A2E:0370:7334") # Neither
print test.validIPAddress("02001:0db8:85a3:0000:0000:8a2e:0370:7334") # Neither







