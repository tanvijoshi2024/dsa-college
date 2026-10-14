# program to read a file and count how many vowels are present in its content.
f=open("python/assignment1/read.text","r")
data=f.read()
count=0
for i in data:
    if i in "aeiouAEIOU":
        count+=1
print("number of vowels:",count)
f.close()        
