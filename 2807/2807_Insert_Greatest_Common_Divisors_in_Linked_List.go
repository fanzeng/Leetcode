/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func insertGreatestCommonDivisors(head *ListNode) *ListNode {
    n := head
    for n.Next != nil {
        g := gcd(n.Val, n.Next.Val)
        n.Next = &ListNode{Val: g, Next: n.Next}
        n = n.Next
        // fmt.Printf("%v, %v", n, n.Next)
        n = n.Next
    }
    return head
}

func gcd(a, b int) int {
    if a < b {
        return gcd(b, a)
    }
    if b == 0 {
        return a 
    }
    return gcd(b, a % b)
}
