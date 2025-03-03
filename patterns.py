# Sample Input 1:
# 3
# Sample Output 1:
# * * *
# * * *
# * * *
# Explanation Of Sample Input 1 :
# For N = 3, fill all the rows and columns in 3x3 matrix with ‘*’.
# Sample Input 2 :
# 1
# Sample Output 2 :
# *
# Sample Input 3 :
# 4
# Sample Output 3 :
# * * * *
# * * * *
# * * * *
# * * * *

# ************ solution for this pattern ***************
def nForest(n:int) ->None:
    for i in range(n):
        for j in range(n):
            print("*",end=' ')
        print()


# Sample Input 1:
# 3
# Sample Output 1:
# * 
# * *
# * * *
# Explanation Of Sample Input 1 :
# For N = 3, fill all the rows and columns in the lower triangle of 3x3 matrix with ‘*’.
# Sample Input 2 :
# 1
# Sample Output 2 :
# * 


# ************ solution for this pattern ***************
def nForest(n:int) ->None:
    for row in range(0,n):
        for col in range(n-row,n+1):
            print("*",end=' ')
        print()


# Sample Input 1:
# 3
# Sample Output 1:
# 1
# 1 2 
# 1 2 3
# Sample Input 2 :
# 1
# Sample Output 2 :
# 1


# ************ solution for this pattern ***************
def nTriangle(n:int) ->None:
    
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=' ')
        print()