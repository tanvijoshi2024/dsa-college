#alphabet pyramid
n=int(input("enter no of rows:"))

for i in range(n):
    print(' '*(n-i+1),end="")
    for j in range(2*i+1):
        if (j==0 or j==2*i or i==n-1):#j=0 means first character,j=2 last character,i=n-1 means last line
            print (chr(65+j), end=" ")
        else:
            print(" ",end=" ")    
        

        
  
    print()
     