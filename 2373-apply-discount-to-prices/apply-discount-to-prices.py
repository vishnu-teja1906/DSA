class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        def contains_only_digits(input_str):
            for char in input_str:
                if not char.isdigit():
                    return False
            return True
        ls=list(sentence.split(" "))
        #print(ls)
        for i in range(len(ls)):
            if ls[i][0]=="$" and len(ls[i])>1 and contains_only_digits(ls[i][1:]):
                val=str(int(ls[i][1:])*(1-(discount/100)))
                #print(int(val[val.index(".")+1:]))
                if "." in val:
                    #print("%.2f" % round(int(ls[i][1:])*(1-(discount/100)),2))
                    ls[i] = "$"+str("%.2f" % round(int(ls[i][1:])*(1-(discount/100)),2))
                else:
                    ls[i] = "$"+str(int(ls[i][1:])*(1-(discount/100)))
        return " ".join(ls)