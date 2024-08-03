impl Solution {
    pub fn can_be_equal(target: Vec<i32>, arr: Vec<i32>) -> bool {
        let mut t = target.clone();
        let mut a = arr.clone();
        t.sort();
        a.sort();
        t == a
    }
}
