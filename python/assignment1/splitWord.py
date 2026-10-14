#Take a sentence from the user, split it into words, and store them in a list. Print the longest word.
sentence=input("enter a sentence:")
words=sentence.split()
longest=""
for i in words:
    if len(i)>len(longest):
        longest=i
print("list of words:",words) 
print("longest word:",longest)       