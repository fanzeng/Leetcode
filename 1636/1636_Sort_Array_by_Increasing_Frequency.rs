use std::collections::HashMap;
use std::cmp::Ordering;

impl Solution {
    pub fn frequency_sort(nums: Vec<i32>) -> Vec<i32> {
        let mut counts = HashMap::new();
        nums.iter().for_each(|num| {
            let c = counts.entry(num).or_insert(0);
            *c += 1;
        });
        let mut res = Vec::new();
        let mut k = counts.keys().cloned().collect::<Vec<&i32>>();
        k.sort_by(|a, b| {
            if (counts.get(a) > counts.get(b)) {
                return Ordering::Greater;
            } else if ((counts.get(a) < counts.get(b))) {
                return Ordering::Less;
            }
            return (*b - *a).cmp(&0);
        });
        for key in k.iter() {
            let c = counts.get(key).unwrap();
            for i in 0..*c {
                res.push(**key);
            }
        }
        res
    }
}
