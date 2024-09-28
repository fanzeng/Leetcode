type MyCircularDeque struct {
    k int
    a []int
    h int
    t int
    s int
}


func Constructor(k int) MyCircularDeque {
    a := make([]int, k)
    return MyCircularDeque{k, a, 0, 0, 0}
}


func (this *MyCircularDeque) InsertFront(value int) bool {
    if this.IsFull() {
        return false
    }
    if this.s > 0 {
        this.h = (this.h + this.k - 1) % this.k
    }
    this.a[this.h] = value
    this.s++
    return true
}


func (this *MyCircularDeque) InsertLast(value int) bool {
    if this.IsFull() {
        return false
    }
    if this.s > 0 {
        this.t = (this.t + 1) % this.k
    }
    this.a[this.t] = value
    this.s++
    return true
}


func (this *MyCircularDeque) DeleteFront() bool {
    if this.IsEmpty() {
        return false
    }
    if this.s > 1 {
        this.h = (this.h + 1) % this.k
    }
    this.s--
    return true
}


func (this *MyCircularDeque) DeleteLast() bool {
    if this.IsEmpty() {
        return false
    }
    if this.s > 1 {
        this.t = (this.t + this.k - 1) % this.k
    }
    this.s--
    return true
}


func (this *MyCircularDeque) GetFront() int {
    if this.IsEmpty() {
        return -1
    }
    return this.a[this.h]
}


func (this *MyCircularDeque) GetRear() int {
    if this.IsEmpty() {
        return -1
    }
    return this.a[this.t]
}


func (this *MyCircularDeque) IsEmpty() bool {
    return this.s == 0
}


func (this *MyCircularDeque) IsFull() bool {
    return this.s == this.k
}


/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * obj := Constructor(k);
 * param_1 := obj.InsertFront(value);
 * param_2 := obj.InsertLast(value);
 * param_3 := obj.DeleteFront();
 * param_4 := obj.DeleteLast();
 * param_5 := obj.GetFront();
 * param_6 := obj.GetRear();
 * param_7 := obj.IsEmpty();
 * param_8 := obj.IsFull();
 */
