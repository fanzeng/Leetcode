impl Solution {
    pub fn sort_jumbled(mapping: Vec<i32>, nums: Vec<i32>) -> Vec<i32> {
        let mut v = Vec::new();
        for num in nums.clone() {
            let digits = Self::get_digits(num);
            let unjumbled = digits.iter().map(|d| mapping[*d as usize]).collect();
            // println!("{}", Self::get_num(unjumbled));
            v.push(Self::get_num(unjumbled));
        } 
        let mut zipped: Vec<_> = nums.iter().zip(v).collect();
        zipped.sort_by_key(|a| a.1);
        zipped.iter().map(|a| *a.0).collect()
    }
    fn get_digits(mut num: i32) -> Vec<i32> {
        let mut digits = Vec::new();
        let mut scale = 1;
        while scale * 10 <= num {
            scale *= 10;
        }
        while scale > 0 {
            // println!("{}", num / scale);
            digits.push(num / scale); 
            num = num % scale;
            scale /= 10;
        }
        digits
    }
    fn get_num(digits: Vec<i32>) -> i32 {
        let mut res = 0;
        let mut scale = 1;
        digits.iter().rev().for_each(|d| {
            // println!("d = {}", d);
            res += d * scale;
            scale *= 10;
        });
        res
    }
}
