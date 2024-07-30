impl Solution {
    pub fn minimum_deletions(s: String) -> i32 {
        if s.len() < 2 {
            return 0;
        }
        let mut count_a = 0;
        let mut count_b = 0;
        for c in s.chars() {
            match(c) {
                'a' => count_a += 1,
                'b' => count_b += 1,
                _ => ()
            }
        }
        // println!("count_a = {}, count_b = {}", count_a, count_b);
        if count_a == 0 || count_b == 0 {
            return 0;
        }
        let total_a = count_a;
        let total_b = count_b;
        let mut remain_a: i32;
        let mut remain_b: i32;
        count_a = 0;
        count_b = 0;
        let mut res = s.len() as i32;
        // turn all b before the cursor to a,
        // and turn all a after the cursor to b.
        // What's at the cursor does not need to change.
        for c in s.chars() {
            if c == 'a' {
                count_a += 1;
            }
            remain_a = total_a - count_a;
            remain_b = total_b - count_b;
            // println!("count_b = {}, remain_a = {}", count_b, remain_a);
            if count_b > res {
                break; // one part of sum already > res and will not improve.
            }
            if count_b + remain_a < res {
                res = count_b + remain_a;
            }
            if c == 'b' {
                count_b += 1;
            }
        }
        res
    }
}
