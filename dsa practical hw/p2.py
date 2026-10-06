arr=[2,5,4,33,77,55,10]
max=min=arr[0]
smin=smax=arr[0]
for num in arr:
    if num>max:
        smax=max
        max=num
    elif(num>smax and num!=max):
        smax=num

    if num<min:
        smin=min
        min=num
    elif(num<smin and num!=min):
        smin=num
print("second max is",smax)
print("second min is",smin)
print("max is",max)
print("min is",min)


