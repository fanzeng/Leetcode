use std::collections::HashSet;
use std::collections::HashMap;
impl Solution {
    pub fn combination_sum2(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        // note all numbers are positive
        let mut sorted = candidates.clone();
        sorted.sort();
        let mut sum = 0;
        let mut nums = Vec::new();
        for i in 0..sorted.len() {
            if i > 0 && sorted[i] != sorted[i-1] {
                nums.push(sorted[i]);
                sum = sorted[i];
                continue
            }
            if sum + sorted[i] <= target {
                nums.push(sorted[i]);
                sum += sorted[i];
            } else {
                continue
            }
        }
        // println!("nums = {:?}", nums);
        let mut visited: HashMap<(i32, i32), Vec<Vec<i32>>> = HashMap::new();
        match Self::find(nums, target, &mut visited) {
            None => Vec::new(),
            Some(res) => {
                let h: HashSet<_> = res.into_iter().collect();
                h.into_iter().collect()
            }
        }
    }
    fn find(nums: Vec<i32>, target: i32, visited: &mut HashMap<(i32, i32), Vec<Vec<i32>>>) -> Option<Vec<Vec<i32>>> {
        // println!("nums = {:?}, target = {}", nums, target);
        if nums.len() == 0 || target <= 0 {
            return None
        }
        if let Some(value) = visited.get(&(nums.len() as i32, target)) {
            return Some(value.clone())
        }
        if nums[0] == target {
            return Some(vec![vec![nums[0]]])
        }
        // deal with special case when whole array is the same number
        if nums.iter().min().unwrap() == nums.iter().max().unwrap() {
            let n = nums[0];
            if target % n == 0 && target/n <= nums.len() as i32 {
                return Some(vec![vec![n;(target/n) as usize]])
            } else {
                return None
            }
        }
        let mut v = Vec::new();
        let n = nums[0];
        if let Some(r) = Self::find(nums[1..].to_vec(), target - n, visited) {
            for a in r {
                let n = vec![n];
                v.push([n, a].concat());
            }
        }
        if let Some(r) = Self::find(nums[1..].to_vec(), target, visited) {
            for a in r {
                let n = vec![n];
                v.push(a);
            }
        }
        visited.insert((nums.len() as i32, target), v.clone());
        Some(v)
    }
}
