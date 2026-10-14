f=open("python/assignment1/read.text","r")
data=f.read()
words=data.split()
print("total number of vowels:",len(words))
unique=[]
for i in words:
    if i not in unique:
        unique.append(i)
print("all unique words:",unique)
f.close()        