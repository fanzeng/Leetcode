class Solution {
    public String addStrings(String num1, String num2) {
        // Make num1 the longer of the 2
        if (num1.length() < num2.length()) {
            var temp = num2;
            num2 = num1;
            num1 = temp;
        }
        var r = "";
        var carry = 0;
        for (int i = num1.length() - 1, j = num2.length() - 1; i >= 0; i--) {
            char d1 = num1.charAt(i);
            char d2;
            if (j >= 0) {
                d2 = num2.charAt(j);
            } else {
                d2 = '0';
            } 
            // System.out.printf("d1 = %c, d2 = %c\n", d1, d2);
            var sum = d1 - '0' + d2 - '0' + carry;
            // System.out.printf("sum = %d\n", sum);
            carry = sum / 10;
            // System.out.printf("digit = %s\n",  sum % 10);
            carry = sum / 10;
            r = sum % 10 + r;
            if (j >= 0) {
                j--;
            }
        }
        if (carry > 0) {
            r = carry + r;
        }
        return r;
    }
}
