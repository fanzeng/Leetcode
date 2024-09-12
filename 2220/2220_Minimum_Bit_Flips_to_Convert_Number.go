func minBitFlips(start int, goal int) int {
   xor := start ^ goal 
   return strings.Count(strconv.FormatInt(int64(xor), 2), "1")
}
