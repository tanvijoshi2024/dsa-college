arr=[33,76,99,1,2,23,65,90,]
search=int(input("enter the no to search:"))
found=False
for num in arr:
    if num==search:
        print("No found at position:",num+1)
        found=True
        break
if found==False:
    print("no not found in array")