func findTheWinner(n int, k int) int {
    // handle k == 1
    // in this case, the order of removal is always 1, 2, 3, ..., n
    // so return n
    if k == 1 {
        return n
    }
    nxt := make(map[int]int) // map of who is next
    for i := range(n) {
        nxt[i + 1] = (i + 2) % n
    }
    nxt[n - 1] = n
    i := 1
    for n > 1 {
        for j := 0; j < k-2; j++ {
            i = nxt[i]
        }
        // nxt[i] is the next out
        // fmt.Printf("%d is out.", nxt[i])
        nxt[i] = nxt[nxt[i]]
        // fmt.Println(nxt)
        i = nxt[i]
        n--
    } 
    return i
}
