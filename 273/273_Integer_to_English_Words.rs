impl Solution {
    pub fn number_to_words(num: i32) -> String {
        if num == 0 {
            return String::from("Zero");
        }
        return Self::convert(num);
    }
    fn dtoa(num: i32) -> String {
        const digits: [&str; 11] = [
          "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"
        ];
        digits[num as usize].to_string()
    }
    fn less_than_100(num: i32) -> String {
        const teens: [&str; 10] = [
          "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty"
        ];
        const tens: [&str; 10] = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ];
        if num <= 10 {
            return Self::dtoa(num);
        }
        if num <= 20 {
            return teens[num as usize - 11].to_string();
        }
        let a = num / 10;
        let b = num % 10;
        if b == 0 {
            return tens[a as usize].to_string();
        } else {
            return format!("{} {}", tens[a as usize], Self::dtoa(b));
        }
        String::new()
    }
    fn less_than_1000(num: i32) -> String {
        let a = num / 100;
        let b = num % 100;
        if a == 0 {
            return Self::less_than_100(num);
        } else if b > 0 {
            return format!("{} Hundred {}", Self::dtoa(a), Self::less_than_100(b));
        } else {
            return format!("{} Hundred", Self::dtoa(a));
        }
        String::new()
    }
    fn convert(num: i32) -> String {
        let mut res = String::new();
        let mut n = num as i64;
        let mut base: i64 = 1;
        let mut log = 0; // log base 1000
        let v: [&str; 4] = ["", "Thousand", "Million", "Billion"];
        while n >= base*1000 {
            base *= 1000;
            log += 1;
        }
        // println!("base = {}, log = {}", base, log);
        while base > 1 {
            // println!("n = {}", n);
            let a = (n / base) as i32;
            if a == 0 {
                break;
            }
            res.push_str(&format!("{} {}", Self::less_than_1000(a), v[log as usize].to_string()));
            if n % base > 0 {
                res.push_str(" ");
            }
            n = n % base;
            base /= 1000;
            log -= 1;
        }
        let b = num % 1000;
        if b > 0 {
            res.push_str(&format!("{}", Self::less_than_1000(b)));
        }
        res
    }
}
