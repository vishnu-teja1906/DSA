class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=len(digits)-1
        c=0
        while(l>=0 and len(digits)!=1):
            #print(l,c)
            v=digits[l]
            if l==len(digits)-1:
                digits[l]=(digits[l]+1+c)%10
                c=(v+c+1)//10
            else:
                #print(1)
                digits[l]=(digits[l]+c)%10
                c=(v+c)//10
            
            l-=1
        if len(digits)==1:
            v=digits[0]
            digits[l]=(v+1+c)%10
            c=(v+1)//10
        if c!=0:
            digits.insert(0,c)
        return digits