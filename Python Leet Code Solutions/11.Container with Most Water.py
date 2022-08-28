#https://www.geeksforgeeks.org/container-with-most-water/
def maxArea(A, Len) :
    area = 0
    for i in range(Len) :
        for j in range(i + 1, Len) :
           
            # Calculating the max area ; i=beg and j=end ; Len of height is ur array; j-i is width - height
            area = max(area, min(A[j], A[i]) * (j - i))
    return area
 
# Driver code
a = [ 1,1 ]
b = [ 4,3,2,1,4 ]
c = [1,2,1]
 
len1 = len(a)
print(maxArea(a, len1))
 
len2 = len(b)
print(maxArea(b, len2))

len3 = len(c)
print(maxArea(c,len3))
