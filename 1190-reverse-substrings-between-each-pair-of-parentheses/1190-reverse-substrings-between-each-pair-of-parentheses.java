class Solution {
    public String reverseParentheses(String s) {
		Stack<Character> stack = new Stack();
		Queue<Character> queue = new LinkedList();
		
		for(int i = 0; i < s.length(); i++) {
			if(s.charAt(i) == ')') {
				while(stack.peek() != '(') {
					queue.add(stack.pop());
				}
				stack.pop();
				while(queue.size() > 0) {
					stack.push(queue.remove());
				}
			} else {
				stack.push(s.charAt(i));
			}
		}
		
		char ans[] = new char[stack.size()];
		int indx = stack.size() - 1;
		
		while (stack.size() > 0) {
			ans[indx] = stack.pop();
			indx--;
		}
		
		String word = new String(ans);
		return word;		
	}
}