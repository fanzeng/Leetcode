use std::cmp;
impl Solution {
    pub fn spiral_matrix_iii(rows: i32, cols: i32, r_start: i32, c_start: i32) -> Vec<Vec<i32>> {
        let mut v = Vec::new();
        let mut r = r_start;
        let mut c = c_start;
        let mut l = 0;
        let mut d = 0_u8;
        while (v.len() as i32) < rows*cols {
            if d % 2 == 0 {
                l += 1;
            }
            let n = Self::next(r, c, d, l);
            println!("n = {:?}", n);
            if (d % 2 == 0 && r >= 0 && r < rows) || (d % 2 == 1 && c >= 0 && c < cols) {
                v.extend(Self::fill(
                    r, c, n[0], n[1], rows, cols, d
                ));
            }
            r = n[0];
            c = n[1];
            d = (d + 1_u8) % 4;
            // if l > 50 {
            //     break;
            // }
        } 
        v
    }
    fn next(r: i32, c: i32, d: u8, l: i32) -> Vec<i32> {
        let (nr, nc) = match d {
            0_u8 => {
                let nr = r;
                let nc = c + l;
                (nr, nc)
            },
            1_u8 => {
                let nr = r + l;
                let nc = c;
                (nr, nc)
            },
            2_u8 => {
                let nr = r;
                let nc = c - l;
                (nr, nc)
            },
            3_u8 => {
                let nr = r - l;
                let nc = c;
                (nr, nc)
            },
            _ => (-1, -1)
        };
        vec![nr, nc]
    }
    fn fill(r0: i32, c0: i32, r1: i32, c1: i32, rows: i32, cols: i32, d: u8) -> Vec<Vec<i32>> {
        let mut v = Vec::new();
        match d {
            0_u8 => {
                let mut c = cmp::max(c0, 0);
                while c < cmp::min(c1, cols) {
                    v.push(vec![r0, c]);
                    c += 1;
                }
            },
            1_u8 => {
                let mut r = cmp::max(r0, 0);
                while r < cmp::min(r1, rows) {
                    v.push(vec![r, c0]);
                    r += 1;
                }
            },
            2_u8 => {
                let mut c = cmp::min(c0, cols);
                if c >= cols {
                    c = cols - 1;
                }
                while c > cmp::max(c1, -1) {
                    v.push(vec![r0, c]);
                    c -= 1;
                }
            },
            3_u8 => {
                let mut r = cmp::min(r0, rows - 1);
                while r > cmp::max(r1, -1) {
                    v.push(vec![r, c0]);
                    r -= 1;
                }
            },
            _ => ()
        };
        v
    }
}
