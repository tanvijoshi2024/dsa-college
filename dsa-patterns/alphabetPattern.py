#Alphabet pattern in the ab form
n=int(input("enter no of roes:"))
for i in range(n):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()    