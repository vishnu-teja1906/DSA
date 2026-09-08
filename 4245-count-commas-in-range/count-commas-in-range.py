class Solution:
    def countCommas(self, n: int) -> int:
        if len(str(n)) <4:
            return 0
        res=0
        
        return n-999