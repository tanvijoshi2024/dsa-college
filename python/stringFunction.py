#python examples for string Function
text = "  Welcome to IMCC  "
print("Upper Case :", text.upper())#to make all letter in upper case

print("remove space:", text.strip())#Strip spaces from both ends

print("Lower case:", text.lower())#to make all letter in lower letter

text=text.strip()
print("Capitalize first letter", text.capitalize())#capitalize first letter

print(text.title())#capitalize each word

print("Letter C occurs", text.count("C"), "times the text")#count occurance of a substring

print("Position of IMCC in text is", text.find("INCC"))#find the position of a substring (-1 if not found)

print(text.replace("IMCC", "Python Magic")) #replacing a substring

print(text.startswith(" We"))
print(text.endswith("! "))#check if string starts or ends with certain substring

print("simple split", text.split())#split strings into list

words=["Python", "is", "fun"]
print("" . join("words"))#join the list of string with a seperator