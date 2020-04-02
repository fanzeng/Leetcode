class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return True
        s = s.upper()
        i = 0
        j = len(s)-1
        while i < j:
            i, j = self.nextAlphaNumeric(s, i, j)
            if s[i].isalnum() and s[j].isalnum() and s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
    def nextAlphaNumeric(self, s, i, j):
        k = i
        l = j
        while i < l and not s[i].isalnum():
            i += 1
        while j > k and not s[j].isalnum():
            j -= 1
        return i, j

test = Solution()
print test.isPalindrome("A man, a plan, a canal: Panama") # T
print test.isPalindrome("race a car") # F
print test.isPalindrome("abcdefg hijklmn nmlkjih gfedcba") # T
print test.isPalindrome("a;b@c<d!e#f$g h,i^j%k(l)m/n n/m)l(k%j^i,h g%f#e!d<c@b;a") # T
print test.isPalindrome("a;b@c<d!e#f$g h,i^j%k(l)m/n n/m)l(k%j^i,h g%f#e!d>c@b;a") # T
print test.isPalindrome("a;b@c<d!e#f$g h,i^j%k(l)m/nXn/m)l(k%j^i,h g%f#e!d>c@b;a") # T
print test.isPalindrome("a;b@c<d!e#f$g h,i^j%k(l)m/nXXn/m)l(k%j^i,h g%f#e!d>c@b;a") # T
print test.isPalindrome("a;b@c<d!e#f$g h,i^j%k(l)m/nXYn/m)l(k%j^i,h g%f#e!d>c@b;a") # F
print test.isPalindrome(".,") # T

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.
#
# Example 1:
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:
#
# Input: "race a car"
# Output: false