class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> stackMin;
    
    public MinStack() {
        stack = new Stack<>();
        stackMin = new Stack<>(); 
    }
    
    public void push(int val) {
        stack.push(val);
        if(!stackMin.isEmpty()){
            stackMin.push(Math.min(val, stackMin.peek()));
        }else{
            stackMin.push(val);
        }
    }
    
    public void pop() {
        stackMin.pop();
        stack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return stackMin.peek();
    }
}
