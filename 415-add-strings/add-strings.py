class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1)<len(num2):
            while(len(num1)!=len(num2)):
                num1="0"+num1
        else:
            while(len(num1)!=len(num2)):
                num2="0"+num2
        #print(num1,num2)
        res=""
        carry = 0
        for i in range(len(num1)-1,-1,-1):
            res=str((int(num1[i])+int(num2[i])+carry)%10)+res
            carry = (int(num1[i])+int(num2[i])+carry)//10
        if carry:
            while(carry):
                res=str(carry%10)+res
                carry = carry//10
        return res
