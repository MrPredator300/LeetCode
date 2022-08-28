class Solution:

    def romantoint(self,s: str) ->int:
        dicto = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum = 0
        last = 1001
        for i in s:
            if dicto[i]>last:
                sum+=dicto[i]-(last*2)
            else:
                sum+=dicto[i]
            last=dicto[i]
            if sum<0:
                sum=-sum
        return sum

s = "III"
ob1 = Solution()
print(ob1.romantoint(s))



