impl Solution {
    pub fn lemonade_change(bills: Vec<i32>) -> bool {
        // for $10 there is only 1 option which is to consume a $5
        // for $20 there are 2 options, $5*3 or $10+$5
        // if there are only $20 we have no preference
        // but because there could be $10 for which we need $5
        // we prefer to use $10+$5 if possible
        let mut count5 = 0;
        let mut count10 = 0;
        for b in bills {
            match b {
                5 => count5 += 1,
                10 => {
                    if count5 > 0 {
                        count5 -= 1;
                        count10 += 1;
                    } else {
                        return false
                    }
                },
                _ => {
                    if count10 > 0 && count5 > 0 {
                        count10 -= 1;
                        count5 -= 1;
                    } else if count5 >= 3 {
                        count5 -= 3;
                    } else {
                        return false
                    }
                }
            }
        }
        true
    }
}
