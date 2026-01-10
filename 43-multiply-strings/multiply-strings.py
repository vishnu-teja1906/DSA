class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        def mult(a,b):
            res=""
            carry = 0
            for i in range(len(b)-1,-1,-1):
                res=str((carry+int(list(b)[i])*int(a))%10)+res
                carry = (carry+int(list(b)[i])*int(a))//10
            if carry:
                res = str(carry) + res
            return res
        def add(num1,num2):
            #print(num1,num2)
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
                res = str(carry) + res
            return res

        res=""
        carry,val = "0","0"
        num1,num2 = num1 if len(num1)<len(num2) else num2,num1 if len(num1)>=len(num2) else num2
        for i in range(len(num1)-1,-1,-1):
            val = mult(num1[i],num2)
            res = str((int(val[-1])+int(carry[-1]))%10)+res
            car1 = str((int(val[-1])+int(carry[-1]))//10)
            if len(val[:len(val)-1])==0 and len(carry[:len(carry)-1])==0:
                carry = "0"
            elif len(val[:len(val)-1])==0:
                carry = add(carry[:len(carry)-1],car1)
            elif len(carry[:len(carry)-1]) ==0:
                carry = add(val[:len(val)-1],car1)
            else:
                #print("car1:",carry,val[:len(val)-1],carry[:len(carry)-1])
                carry = add(val[:len(val)-1],carry[:len(carry)-1])
                carry = add(carry,car1)
                #print("car:",carry)
            #print(val,res,carry)
        if carry != "0":
            res=carry+res
            
        return res
'''

'''