class Solution {
    public boolean isOperand(String c) {
		if(c.equals("+") || c.equals("-") || c.equals("*") || c.equals("/"))
			return true;
		return false;
	}
	
	public int evalRPN(String[] tokens) {
        if(tokens.length == 1)
			return Integer.parseInt(tokens[0]);
        
		int stack[] = new int[tokens.length];
		int indx = -1;
		int val = 0;
		
		for(int i = 0; i < tokens.length; i++) {
			if(!isOperand(tokens[i]))
				stack[++indx] = Integer.parseInt(tokens[i]);
			else {
				int n2 = stack[indx--];
				int n1 = stack[indx--];
				
				switch(tokens[i]) {
				case "+" :
					val = n1 + n2;
					break;
				case "-" :
					val = n1 - n2;
					break;
				case "*" :
					val = n1 * n2;
					break;
				case "/" :
					val = n1 / n2;
					break;
				}
				
				stack[++indx] = val; 
				
				
			}
		}
		
		return val;
	}
}