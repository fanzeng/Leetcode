import (
    "slices"
    "fmt"
)

func minSubArrayLen(target int, nums []int) int {
    // Note that all numbers are positive.
    // If sum of an interval [a, b) >= target,
    // then we know [a, b+i) where i > 0 cannot be the solution,
    // so we don't need to check them.
    // However, if we increment a without decrementing b,
    // we could miss [a+j, b-k), where j, k > 0,
    // but this can be covered if we do the check again from right to left
    l2r := checkL2R(target, nums)
    slices.Reverse(nums)
    r2l := checkL2R(target, nums)
    if l2r < r2l {
        return l2r
    } else {
        return r2l
    }
}

func checkL2R(target int, nums []int) int {
    a, b := 0, 1
    s := nums[a]
    res := 0 
    for {
        if s >= target {
            if res == 0 || b - a < res {
                res = b - a
            }
            for a + 1 < b && s - nums[a] >= target {
                s -= nums[a]
                a++
                if b - a < res {
                    res = b - a
                }
            }
        }
        if b >= len(nums) {
            break
        }
        s += nums[b]
        b++
    }
    return res
}
