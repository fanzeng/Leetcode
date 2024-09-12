func countConsistentStrings(allowed string, words []string) int {
    count := 0
    m := make(map[rune]bool)
    for _, a := range allowed {
        m[a] = true
    }
    for _, w := range(words) {
        allowed := true
        for _, c := range(w) {
            // fmt.Printf("%c\n", c)
            if m[c] == false {
                allowed = false
                break
            }
        }
        if allowed {
            count += 1
        }
    }
    return count
}
