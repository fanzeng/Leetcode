func xorQueries(arr []int, queries [][]int) []int {
    // Store the xors from the beginning of arr til current index
    xors := make([]int, len(arr))
    x := arr[0]
    xors[0] = x
    for i, a := range arr[1:] {
        xors[i+1] = xors[i] ^ a 
    }
    // fmt.Printf("%v", xors)
    res := make([]int, len(queries))
    for i, q := range queries {
        l := q[0]
        r := q[1]
        if l == 0 {
            res[i] = xors[r]
        } else {
            res[i] = xors[l-1] ^ xors [r]
        }
    }
    return res
}
