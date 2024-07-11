func minOperations(logs []string) int {
    depth := 0
    for _, path := range(logs) {
        if path == "./" {
            continue
        }
        if path == "../" && depth > 0 {
            depth--
        } else if path != "../" {
            depth++
        }
    }
    return depth
}
