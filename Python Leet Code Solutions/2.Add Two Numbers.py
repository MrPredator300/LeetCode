l1 = [2,4,3]
l2 = [5,6,4]
res = []
ListNode = []
sum = 0

def addTwoNumbers(l11,l12):
    carry = 0
    for i in range(len(l11)):
        for j in range(len(l12)):
            if(i==j):
                sum = l11[i]+l12[j] + carry
                if(sum/10!=0):
                    carry =int(sum/10)
                    print(carry)
                    res.append(int(sum % 10))
                else:
                   res.append(sum)
                   carry=0
    if(len(l11)!=len(l12)):
        if(len(l11)>len(l12)):
            for i in range(len(l12),len(l11)):
                sum = l11[i] + carry
                if (sum / 10 != 0):
                    carry = int(sum / 10)
                    print(carry)
                    res.append(int(sum % 10))
                else:
                    res.append(sum)
                    carry = 0
            if(carry):
                res.append(carry)
        else:
            for i in range(len(l11),len(l12)):
                sum = l12[i] + carry
                if (sum / 10 != 0):
                    carry = int(sum / 10)
                    print(carry)
                    res.append(int(sum % 10))
                else:
                    res.append(sum)
                    carry = 0
            if(carry):
                res.append(carry)


    print(res)

addTwoNumbers(l1,l2)





