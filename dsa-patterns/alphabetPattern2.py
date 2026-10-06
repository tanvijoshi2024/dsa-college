#Alphabet pattern in the ab form
n=int(input("enter no of roes:"))
for i in range(n):
    for j in range(i+1):
        print(chr(65+i),end=" ")
    print()