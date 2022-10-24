func findErrorNums(nums []int) []int {
    m := make(map[int]int)
    var dup int
    for _, num := range nums {
        if _, ok := m[num]; ok {
            dup = num
        } else {
            m[num] = 1
        }
    }
    miss := 0
    for i := 1; i <= len(nums); i++ {
        if _, ok := m[i]; !ok {
            return []int{dup, i}
        }
    }
    return []int{dup, miss}
}
