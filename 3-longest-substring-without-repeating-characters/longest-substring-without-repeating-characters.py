class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        itr = 0
        maxi = 0
        while itr < len(s):
            st = set()
            k=itr
            while k<len(s) and s[k] not in st :
                st.add(s[k])
                k+=1
            maxi = max(maxi,k-itr)
            itr+=1
        return maxi