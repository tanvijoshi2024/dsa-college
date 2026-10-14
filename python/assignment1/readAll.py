#Read all lines from a file into a list. Print the total number of lines and display the 2nd and 4th line.
f=open("python/assignment1/read.text","r")
lines=f.readlines()
print("total no. of lines:",len(lines))
if len(lines)>=2:
    print("2nd line:",lines[1].strip())
if len(lines)>=4:
    print("4th line:",lines[3].strip())
f.close()        