#Alphabet pattern in the ab form
n=int(input("enter no of roes:"))
num=0
for i in range(n):
    for j in range(i):
        print(chr(65+num),end=" ")
        num=num+1
    print()    