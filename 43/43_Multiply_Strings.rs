impl Solution {
    pub fn multiply(num1: String, num2: String) -> String {
        if num1 == "0" || num2 == "0" {
            return "0".to_string()
        }
        Self::big_multiply(num1, num2)
    }
    fn big_multiply(num1: String, num2: String) -> String {
        let mut v = Vec::new();
        let long: String;
        let short: String;
        if num1.len() > num2.len() {
            long = num1;
            short = num2;
        } else {
            long = num2;
            short = num1;
        }
        for digit in short.chars().rev() {
            v.push(Self::single_digit_multiply(&long, digit));
        }
        // println!("v = {:?}", v);
        let mut s = String::new();
        let mut carry = 0_i8;
        // find the total length of the product string
        let mut t = 0;
        for (k, w) in v.clone().into_iter().enumerate() {
            if k + w.len() > t {
                t = k + w.len();
            }
        }
        // println!("t = {}", t);
        for i in 0..t {
            let mut sum: i64 = carry as i64;
            for j in 0..i+1 {
                if j < v.len() && i - j < v[j].len() {
                    sum += Self::ctoi(&(v[j].chars().nth(i-j).unwrap())) as i64;
                }
            }
            // println!("sum = {}", sum);
            s.push(Self::itoc((sum % (10 as i64)) as i8));
            carry = (sum / (10 as i64)) as i8;
        }
        if carry > 0 {
            s.push(Self::itoc(carry));
        }
        s.chars().rev().collect()
    }
    fn single_digit_multiply(num: &String, digit: char) -> String {
        // println!("{} * {}", num, digit);
        let mut s = String::new();
        let i = Self::ctoi(&digit);
        let mut carry = 0;
        for c in (*num).chars().rev() {
            let j = Self::ctoi(&c);
            let prod = i*j + carry;
            carry = prod / 10;
            s.push(Self::itoc(prod % 10));
        }
        if carry > 0 {
            s.push(Self::itoc(carry));
        }
        // s.chars().rev().collect()
        s
    }
    fn small_multiply(num1: String, num2: String) -> String {
        println!("atoi(nums1) = {}", Self::atoi(&num1));
        println!("atoi(nums2) = {}", Self::atoi(&num2));
        println!("product = {}", Self::atoi(&num1)*Self::atoi(&num2));
        Self::itoa(Self::atoi(&num1)*Self::atoi(&num2))
    }
    fn ctoi(c: &char) -> i8 {
        match *c {
            '0'..='9' => *c as i8 - ('0' as i8),
            _ => -1,
        }
    }
    fn itoc(i: i8) -> char {
        match i {
            0..=9 => ('0' as u8 + i as u8) as char,
            _ => '-',
        }
    }
    fn atoi(s: &String) -> i64 {
        let mut b = 1_i64;
        let mut n = 0_i64;
        for c in s.chars().rev() {
            println!("c = {}", c);
            n += b*(Self::ctoi(&c) as i64);
            b *= 10;
        }
        n
    }
    fn itoa(n: i64) -> String {
        let mut s = String::new();
        let mut b = 1_i64;
        let mut n = n;
        while b*10 < n {
            b *= 10;
        }
        println!("b = {}", b);
        while b >= 1_i64 {
            println!("n/b = {}", n/b);
            s.push(Self::itoc((n/b) as i8));
            n = n % b;
            b /= 10;
        }
        s
    }
}
