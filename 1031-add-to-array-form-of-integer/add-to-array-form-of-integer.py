class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ls = []
        for i in range(len(num)-1,-1,-1):
            k+=num[i]
            ls.insert(0,k%10)
            k=k//10
        if k:
            while(k):
                ls.insert(0,k%10)
                k=k//10
        return ls