impl Solution {
    pub fn num_teams(rating: Vec<i32>) -> i32 {
        Self::check_valid(rating.as_slice(), -1, true, 3) + Self::check_valid(rating.as_slice(), -1, false, 3) 
    }
    fn check_valid(rating: &[i32], v: i32, asc: bool, remain: i32) -> i32 {
        // print!("{:?}, {}, {}, {}\n", rating, v, asc, remain);
        if remain > 1 {
            let mut i = 0;
            // find the first valid next number
            if v != -1 { // ratings[i] >= 1, so -1 means no prev value, so we just pick the 0th.
                while i < rating.len() {
                    if asc {
                        if rating[i] > v {
                            break;
                        }
                    } else {
                        if rating[i] < v {
                            break;
                        }
                    }
                    i += 1;
                }
            }
            if i+1 >= rating.len() {
                return 0; // cannot find next or no remaining array after next
            }
            let has_first = Self::check_valid(&rating[i+1..], rating[i], asc, remain - 1);
            let has_no_first = Self::check_valid(&rating[i+1..], v, asc, remain);
            return has_first + has_no_first;
        } else if remain == 1 {
            let mut res = 0;
            for i in 0..rating.len() {
                if asc {
                    if rating[i] > v {
                        res += 1;
                    }
                } else {
                    if rating[i] < v {
                        res += 1;
                    }
                }
            }
            return res;
        }
        0
    }
}
