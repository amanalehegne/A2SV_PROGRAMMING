class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        st = []
        for char in s:
            if st and st[-1][0] == char:
                st[-1][1] += 1
            else:
                st.append([char,1])

            if st and st[-1][1] == k:
                st.pop()
        
        ans = ""
        for char,count in st:
            ans += char*count
        
        return ans