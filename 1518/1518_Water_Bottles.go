func numWaterBottles(numBottles int, numExchange int) int {
    consumed := numBottles
    empty := numBottles
    for empty >= numExchange {
        delta := empty / numExchange
        consumed += delta
        empty += delta - delta * numExchange
    }
    return consumed
}
