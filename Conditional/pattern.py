'''
for n = 3
  *
 ***
*****

'''


n = int(input("Enter the value of n"))
for i in range(1, n+1):
    print(" " * (n-i),end="")
    print("*" * (2*i-1),end="")
    print("")


for i in range(1 , n+1):
    print("*" * i)


for i in range(1,n+1):
    if(i==1 or i==n):
        print("*" * n , end="")
    else:
        print("*" , end="")
        print(" " * (n-2),end="")
        print("*" , end="")
    print("")        

    n = 5

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or j == 1 or i == n or j == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
