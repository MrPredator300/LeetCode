from typing import List
class Solution:

    def twosum(self,nums: List[int],target: int) -> List[int]:
        List=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    List.append(i)
                    List.append(j)
                    break
        
        return(List)

nums = [2,7,11,15] 
ob1 = Solution()
print(ob1.twosum(nums))







