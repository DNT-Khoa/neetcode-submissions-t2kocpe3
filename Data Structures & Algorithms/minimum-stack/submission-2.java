class MinStack {

    record Item(int val, int min) {}
    private Deque<Item> stack;

    public MinStack() {
        stack = new ArrayDeque<>();
    }
    
    public void push(int val) {
        if (stack.isEmpty()) {
            stack.offerFirst(new Item(val, val));
        } else {
            stack.offerFirst(new Item(val, Math.min(val, stack.peek().min)));
        }
    }
    
    public void pop() {
        stack.pollFirst();
    }
    
    public int top() {
        return stack.peek().val;
    }
    
    public int getMin() {
        return stack.peek().min;
    }
}
