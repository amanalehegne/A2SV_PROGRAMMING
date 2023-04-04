#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
        n = len(s)
        size = 2 ** n
        res = []
    
        for i in range(1, size):
            num = i
            idx = 0
            ans = []
            while num:
                val = num & 1
                if val:
                    ans.append(s[idx])
                num >>= 1
                idx += 1
            res.append("".join(ans))
    
        return sorted(res)
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends