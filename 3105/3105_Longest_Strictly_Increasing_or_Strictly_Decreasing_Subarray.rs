impl Solution {
    pub fn longest_monotonic_subarray(nums: Vec<i32>) -> i32 {
        let mut rnums = nums.clone();
        rnums.reverse();
        std::cmp::max(Self::max_ascend(nums), Self::max_ascend(rnums))
    }
    fn max_ascend(nums: Vec<i32>) -> i32 {
        let mut count = 1;
        let mut max_count = count;
        for i in 0..nums.len()-1 {
            if nums[i] < nums[i+1] {
                count += 1;
                if count > max_count {
                    max_count = count;
                }
            } else {
                count = 1;
            }
        }
        max_count
    }
}
