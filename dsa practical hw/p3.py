arr=[3,7,6,4,5,2,9,8,1]
even=0
odd=0
for num in arr:
    if num%2==0:
        even+=1
    else:
        odd+=1
print("even:",even)
print("odd:",odd)