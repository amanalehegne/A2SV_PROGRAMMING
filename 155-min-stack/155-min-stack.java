class MinStack {

    public MinStack() {
        
    }
    
   Stack<Integer> stack = new Stack();
	Stack<Integer> minStack = new Stack();
	
	    public void push(int val) {
	        if(!stack.isEmpty()) minStack.push(Math.min(minStack.peek(), val));
	        else minStack.push(val);
	        stack.push(val);
	    }
	    
	    public void pop() {
	        stack.pop();
	        minStack.pop();
	    }
	    
	    public int top() {
	        return stack.peek();
	    }
	    
	    public int getMin() {
	        return minStack.peek();
	    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */