class FooBar {
    private int n;
    private boolean hasFooPrinted;
    private boolean hasBarPrinted;

    public FooBar(int n) {
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            synchronized(this) {
                while (i > 0 && !hasBarPrinted) wait();
        	// printFoo.run() outputs "foo". Do not change or remove this line.
        	printFoo.run();
                hasFooPrinted = true;
                hasBarPrinted = false;
                notifyAll();
            }
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            synchronized(this) {
                while (!hasFooPrinted) wait();
            // printBar.run() outputs "bar". Do not change or remove this line.
        	printBar.run();
                hasBarPrinted = true;
                hasFooPrinted = false;
                notifyAll();
            }
        }
    }
}
