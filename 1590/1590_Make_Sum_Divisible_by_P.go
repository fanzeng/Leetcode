func minSubarray(nums []int, p int) int {
    s := 0
    for _, n := range nums {
        s += n
    }
    if s % p == 0 {
        return 0
    }
    t := s % p // target congruence value
    // fmt.Printf("t = %d\n", t)
    res := -1
    s = 0 // Partial sum
    m := make(map[int]int) // Map latest congruence group location
    for i := 0; i < len(nums); i++ {
        if nums[i] == t {
            return 1
        }
        s = (s + nums[i]) % p
        m[s] = i
        pair := (s + p - t) % p
        // fmt.Printf("i = %d, s = %d, pair = %d\n", i, s, pair)
        start, exists := m[pair]
        var r int
        if exists {
            // fmt.Printf("m[%d] = %d\n", pair, start)
            r = i - start
        } else if s == t {
            r = i + 1
        } else {
            continue
        }
        if res > 0 {
            res = min(res, r)
        } else {
            res = r
        }
    }
    if res == len(nums) {
        return -1
    }
    return res
}
