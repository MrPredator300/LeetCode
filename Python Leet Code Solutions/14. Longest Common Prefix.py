#https://www.tutorialspoint.com/longest-common-prefix-in-python

class Solution(object):
    def lcp(self,strs):

        if len(strs) == 0:
            return ""
        current = strs[0]
        for i in range(1,len(strs)):
            temp = ""
            if len(current) == 0:
                break
            for j in range(len(strs[i])):
                if j<len(current) and current[j] == strs[i][j]:
                    temp+=current[j]
                else:
                    break
                current = temp
            return current

input_list = ["flower","flow","flight"]
input_list_2 = ["dog","racecar","car"] 
ob1 = Solution()
print(ob1.lcp(input_list))
print(ob1.lcp(input_list_2))


