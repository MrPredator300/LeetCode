class Solution:

    def isPalindrome(self,x: int) -> bool:
        num = x
        if num < 0:
            return False
        res = 0
        while res <=x:
            i = num % 10
            res += i
            if res==x:
                return True
            num -=i
            if num==0:
                return False
            res=res*10
            num=num/10
    
        return False

x = 121 
ob1 = Solution()             #object = Class_Name
print(ob1.isPalindrome(x))   #Object_Function_Name_(input)








