use rand::seq::SliceRandom;
impl Solution {
    pub fn sort_array(nums: Vec<i32>) -> Vec<i32> {
        let mut nums_mut: Vec<i32> = nums.into_iter().collect();
        nums_mut.shuffle(&mut rand::thread_rng());
        return Self::quick_sort(nums_mut.iter().collect()).iter().map(|&x| *x).collect();
    }
    fn quick_sort(nums: Vec<&i32>) -> Vec<&i32> {
        if nums.len() < 2 {
            return nums;
        }
        if nums.len() == 2 {
            if nums[0] < nums[1] {
                return nums;
            } else {
                return nums.into_iter().rev().collect();
            }
        }
            
        let minimum = nums.clone().into_iter().min().unwrap();
        let maximum = nums.clone().into_iter().max().unwrap();
        if minimum == maximum {
            return nums;
        }
        let mut i = 0;
        while i < nums.len() && (*nums[i] == *minimum || *nums[i] == *maximum) {
            i += 1;
        }
        if (i == nums.len()) {
            return Self::sort_min_max_only(nums, minimum, maximum);
        }
        let p = nums[i];
        let mut left: Vec<&i32> = vec![];
        let mut right: Vec<&i32> = vec![];
        for num in nums {
            if *num < *p {
                left.push(num);
            } else {
                right.push(num);
            }
        }
        left = Self::quick_sort(left);
        right = Self::quick_sort(right);
        
        left.append(&mut right);
        left
    }
    fn sort_min_max_only<'a>(nums: Vec<&'a i32>, minimum: &'a i32, maximum: &'a i32) -> Vec<&'a i32> {
        let mut v_min = vec![];
        let mut v_max = vec![];
        for num in nums {
            if num == minimum {
                v_min.push(num);
            } else {
                v_max.push(num);
            }
        }
        v_min.append(&mut v_max);
        v_min
    }
}
