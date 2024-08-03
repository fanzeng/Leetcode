impl Solution {
    pub fn min_swaps(nums: Vec<i32>) -> i32 {
        let mut count_one = 0;
        for n in &nums {
            if *n == 1 {
                count_one += 1;
            }
        }
        if count_one == nums.len() || count_one == 0 {
            return 0;
        }
        let mut count_zero = 0;
        for i in 0..count_one {
            if nums[i] == 0 {
                count_zero += 1;
            }
        }
        let mut res = count_zero;
        for start in 1..nums.len() {
            if nums[start-1] == 0 {
                count_zero -= 1;
            }
            if nums[(start + count_one - 1) % nums.len()] == 0 {
                count_zero += 1;
            }
            if count_zero < res {
                res = count_zero;
            }
            // println!("start = {}, count_zero = {}.", start, count_zero);
        }
        res
    }
}
