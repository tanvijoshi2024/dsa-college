enter=int(input("enter the no's:"))
arr =[]
for num in enter.split():
      arr.append(int (num))
sum=0
for num in arr:
    sum=sum+num
print(sum)        
