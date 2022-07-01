class Solution {
    public boolean isOpening(char c) {
		if(c == '(' || c =='{' || c == '[')
			return true;
		else
			return false;
	}
	
	public boolean isClosing(char c) {
		if(c == ')' || c =='}' || c == ']')
			return true;
		else
			return false;
	}
	
	public boolean typeCheck(char c, char d) {
		if(c == '(' && d == ')')
			return true;
		if(c == '[' && d == ']')
			return true;
		if(c == '{' && d == '}')
			return true;
		return false;
	}
	
	public boolean isValid(String s) {
		
		char[] stack = new char[s.length()];
		
		int indx = -1;
		
		for(int i = 0; i < s.length(); i++) {
			
			if (isOpening(s.charAt(i))) stack[++indx] = s.charAt(i);
			if (isClosing(s.charAt(i))) {
				if(indx < 0) return false;
				else if(typeCheck(stack[indx], s.charAt(i))) indx--;
				else return false;
			}
			
		}
		
		
		if(indx < 0)
			return true;
		else
			return false;
		
	}
}