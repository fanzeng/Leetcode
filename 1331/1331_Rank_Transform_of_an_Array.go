func arrayRankTransform(arr []int) []int {
    if len(arr) == 0 {
        return arr
    }
    sorted := make([]int, len(arr))
    copy(sorted, arr)
    sort.Ints(sorted)
    count := 1
    ranks := make(map[int]int)
    ranks[sorted[0]] = 1
    for i := 1; i < len(sorted); i++ {
        if sorted[i] > sorted[i-1] {
            count++
            ranks[sorted[i]] = count
        }
    }
    for i := 0; i < len(arr); i++ {
        arr[i] = ranks[arr[i]]
    }
    return arr
}
