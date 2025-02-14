class ProductOfNumbers {

    int productAll;
    ArrayList<Integer> products;

    public ProductOfNumbers() {
        this.productAll = 1;
        this.products = new ArrayList<>();
    }

    public void add(int num) {
        if (num == 0) {
            this.productAll = 1;
            this.products = new ArrayList<>();
        } else {
            this.productAll *= num;
            this.products.add(this.productAll);
        }
    }

    public int getProduct(int k) {
        if (k > this.products.size()) return 0;
        int p = 1;
        if (k == this.products.size()) return this.productAll;
        p = this.products.get(this.products.size() - k - 1);
        // System.out.printf("productAll = %d, p = %d\n", this.productAll, p);
        return this.productAll/p;
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.add(num);
 * int param_2 = obj.getProduct(k);
 */
