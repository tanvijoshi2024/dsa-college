#reversing the pattern
n=int(input("enter rows:"))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()    