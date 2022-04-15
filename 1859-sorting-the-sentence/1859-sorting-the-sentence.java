class Solution {
    public String sortSentence(String s) {
        String [] arr = s.split(" ");
        String [] newArray = new String [arr.length + 1];
        System.out.println(Arrays.toString(arr));
        for (int i = 0; i < arr.length; i++)
        {
        	int indx = Integer.parseInt(String.valueOf(arr[i].charAt(arr[i].length() - 1)));
        	String word = arr[i].substring(0, arr[i].length() - 1);
        	newArray[indx] = word;
        }
        String sorted = "";
        for (int i = 1; i < newArray.length; i++)
        {
        	sorted += newArray[i];
        	if (i < newArray.length - 1)
        		sorted += " ";
        }
        	
        return sorted;
    }
}