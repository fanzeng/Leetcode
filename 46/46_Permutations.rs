impl Solution {
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        if nums.len() == 0 {
            return vec![vec![]]
        }
        let mut v = Vec::new();
        let n = nums[0];
        let res = Self::permute(nums[1..].to_vec());
        // println!("{:?}", res);
        for p in res {
            for pos in 0..p.len() {
                // println!("{}", pos);
                let mut q = p.clone();
                q.insert(pos, n);
                v.push(q);
            }
            let mut q = p.to_vec();
            q.push(n);
            v.push(q);
        }
        v
    }
}
